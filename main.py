from file_operations import FileKit
from pdf_operations import PdfKit
from web_operations import WebKit

wk = WebKit()
fk = FileKit()

folder_name = 'Automate Boring Stuff with Python (Book)'
file_location = f'Desktop/{folder_name}'
fk.SetFileLocation(file_location)
fk.SetOutputFolder(fk.GetUserFolderPath())

print(f'Your selected folder is {fk.GetOutputFolder()}')

print('We are checking if the folder exists or not')
if not fk.CheckIsDir():
    print(f'Folder does not exist. Creating the {folder_name}')
    fk.CreateFolder()
    print(f'Folder is created at {fk.GetOutputFolder()}')
else:
    print('Folder is already exist. Using the existed folder.')

pdf_list = []
chapter_list = []

url = 'https://automatetheboringstuff.com/'
wk.SetUrl(url)

raw_html = wk.ScrapHTMLFromLink()
wk.SetHtmlString(raw_html)
parsed_html = wk.ParseRawHTMLToHTMLTags()
wk.SetParsedHtml(parsed_html)

wk.SetHtmlTag('ul')
ul_list = wk.FindResultsByHTMLTagAndAttribute()
wk.SetParsedHtml(ul_list[1])

wk.SetHtmlTag('a')
chapters = wk.FindResultsByHTMLTagAndAttribute()

for chapter in chapters:
    chapter_link = chapter['href']
    chapter_name = chapter.get_text()
    chapter_list.append({'name': chapter_name, 'link': chapter_link})

fk.SetOutputFolder(f'{fk.GetOutputFolder()}/Chapters')
for chapter in chapter_list:
    url = f'https://automatetheboringstuff.com{chapter["link"]}'
    
    wk.SetUrl(url)
    raw_html = wk.ScrapHTMLFromLink()
    wk.SetHtmlString(raw_html)
    parsed_html = wk.ParseRawHTMLToHTMLTags()
    wk.SetParsedHtml(parsed_html)

    wk.SetHtmlTag('div')
    wk.SetHtmlAttributeObject({'class': 'calibre'})
    result = wk.FindResultsByHTMLTagAndAttribute()
    result = str(result[0]).replace('src="..', 'src="https://automatetheboringstuff.com/2e')

    if not fk.CheckIsDir():
        print(f'Folder does not exist. Creating the Chapters')
        fk.CreateFolder()
        print(f'Folder is created at {fk.GetOutputFolder()}')
    else:
        print('Folder is already exist. Using the existed folder.')

    fk.SetFileInput(result.encode(encoding='ascii', errors='xmlcharrefreplace'))
    fk.SetFileName(chapter['name'])
    fk.SetFileType('html')
    fk.SaveInputAsFile()
    html_file_path = f'{fk.GetOutputFolder()}/{fk.GetFileName()}.{fk.GetFileType()}'
    print(f'File is written in {html_file_path}')

    fk.SetFileType('pdf')
    pk = PdfKit()
    pk.SetInputFilePath(html_file_path)
    pk.SetOutputFilePath(f'{fk.GetOutputFolder()}/{fk.GetFileName()}.{fk.GetFileType()}')
    pk.ConvertHtmlToPdf()
    print(f'File is written in {pk.GetOutputFilePath()}')
    pdf_list.append(pk.GetOutputFilePath())

pk.SetPdfList(pdf_list)
fk.SetOutputFolder(fk.GetUserFolderPath())
pk.SetOutputFilePath(f'{fk.GetOutputFolder()}/{folder_name}.{fk.GetFileType()}')
pk.CombineMultiPDF()
print(f'Merged PDF file is created in {pk.GetOutputFilePath()}')