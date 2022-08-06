import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self, source, destination):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(source, "rb")
        dbx.files_upload(f.read(), destination)

def main():
    access_token = ""
    td = TransferData(access_token)

    source = input("Enter folder to Transfer : -")
    destination = input("Enter path to upload to dropbox : -") #File name once uploaded

    td.uploadFile(source, destination)
    print("File has been moved")

main()