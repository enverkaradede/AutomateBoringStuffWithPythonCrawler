from urllib.request import urlretrieve as down
from file_operations import FileKit

class DownloadKit:
    def __init__(self):
        self.output_folder = None
        self.file_name = None
        self.file_extension = None
        self.output_location = None

    def SetOutputPath(self, output_folder):
        self.output_folder = output_folder

    def GetOutputFolder(self):
        return self.output_folder

    def SetFileName(self, file_name):
        self.file_name = file_name
    
    def GetFileName(self):
        return self.file_name
    
    def SetFileExtension(self, file_extension):
        self.file_extension = file_extension

    def GetFileExtension(self):
        return self.file_extension
    
    def SetOutputLocation(self, output_location):
        self.output_location = output_location

    def GetOutputLocation(self):
        return self.output_location

    def DownloadFromLink(self, url):
        fk = FileKit

        fk.SetFileLocation(f'{self.GetOutputFolder()}/{self.GetFileName()}.{self.GetFileExtension()}')
        self.SetOutputLocation(fk.GetUserFolderPath())
        down(url, self.GetOutputLocation())
        
        return self.output_location