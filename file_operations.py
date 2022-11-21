import os

class FileKit:
    def __init__(self):
        self.file_name = None
        self.file_type = None
        self.file_location = None
        self.output_folder = None
        self.file_input = None
        self.user_folder_location = None

    def SetFileName(self, file_name):
        self.file_name = file_name

    def GetFileName(self):
        return self.file_name

    def SetFileType(self, file_type):
        self.file_type = file_type
    
    def GetFileType(self):
        return self.file_type

    def SetFileLocation(self, file_location):
        self.file_location = file_location

    def GetFileLocation(self):
        return self.file_location

    def SetOutputFolder(self, output_folder):
        self.output_folder = output_folder

    def GetOutputFolder(self):
        return self.output_folder

    def SetFileInput(self, file_input):
        self.file_input = file_input

    def GetFileInput(self):
        return self.file_input

    def CheckIsDir(self):
        return os.path.isdir(self.output_folder)

    def CreateFolder(self):
        os.mkdir(self.output_folder)

    def GetUserFolderPath(self):
        return os.path.expanduser('~') if self.file_location is None else os.path.expanduser(f'~/{self.file_location}')

    def SaveInputAsFile(self):
        file = open(f'{self.GetOutputFolder()}/{self.file_name}.{self.file_type}', 'wb')
        file.write(self.file_input)