from bs4 import BeautifulSoup as bs
from urllib.request import Request as req
from urllib.request import urlopen as uo

class WebKit:
    def __init__(self):
        self.url = None
        self.html_string = None
        self.parsed_html = None
        self.html_tag = None
        self.html_attribute_object = None
        self.req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    def SetUrl(self, url):
        self.url = url

    def GetUrl(self):
        return self.url

    def SetHtmlString(self, html_string):
        self.html_string = html_string

    def GetHtmlString(self):
        return self.html_string

    def SetParsedHtml(self, parsed_html):
        self.parsed_html = parsed_html

    def GetParsedHtml(self):
        return self.parsed_html

    def SetHtmlTag(self, html_tag):
        self.html_tag = html_tag

    def GetHtmlTag(self):
        return self.html_tag

    def SetHtmlAttributeObject(self, html_attribute_object):
        self.html_attribute_object = html_attribute_object

    def GetHtmlAttributeObject(self):
        return self.html_attribute_object

    def SetRequestHeader(self, req_header):
        self.req_header = req_header
    
    def GetRequestHeader(self):
        return self.req_header

    def ScrapHTMLFromLink(self):
        request = req(self.url, headers=self.req_header)
        page = uo(request)
        site_html = page.read()
        page.close()
        
        return site_html


    def ParseRawHTMLToHTMLTags(self):
        return bs(self.html_string, 'html.parser')


    def FindResultsByHTMLTagAndAttribute(self):
        return self.parsed_html.findAll(self.html_tag, self.html_attribute_object) if self.html_attribute_object is not None else self.parsed_html.findAll(self.html_tag)
