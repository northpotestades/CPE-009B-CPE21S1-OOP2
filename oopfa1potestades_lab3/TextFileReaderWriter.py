from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self,filepath):
        with open(filepath,'r') as read_file:
            data=read_file.read()
            print(data)
            read_file.close()
            return data

    def write(self,filepath,data):
        with open(filepath,'w') as write_file:
            write_file.write(data)
            write_file.close()