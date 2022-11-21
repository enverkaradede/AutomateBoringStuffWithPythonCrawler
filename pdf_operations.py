import pdfkit
from PyPDF2 import PdfMerger

class PdfKit:
    def __init__(self):
        self.pdf_list = None
        self.input_file_path = None
        self.output_file_path = None
        self.config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    def SetPdfList(self, pdf_list):
        self.pdf_list = pdf_list

    def GetPdfList(self):
        return self.pdf_list

    def SetInputFilePath(self, input_file_path):
        self.input_file_path = input_file_path

    def GetInputFilePath(self):
        return self.input_file_path

    def SetOutputFilePath(self, output_file_path):
        self.output_file_path = output_file_path

    def GetOutputFilePath(self):
        return self.output_file_path

    def ConvertHtmlToPdf(self):
        pdfkit.from_file(self.input_file_path, self.output_file_path, configuration=self.config)
    
    def CombineMultiPDF(self):
        merger = PdfMerger()

        for pdf in self.pdf_list:
            merger.append(pdf)

        merger.write(self.output_file_path)
        merger.close()