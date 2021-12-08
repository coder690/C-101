from os import access
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def  upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="sl.A9xOvYmlxBnN1N9Fr3FAl3L7-ufybNVm9ymuz6VzONRDQ9KBEUlBvRwG9WTDx3NIxCo_J6GpnLOvm5zuU1M9EFDH3a7iEFdqlFixm-ajrISQA2sbiGvFB4D6BvIgRcFcgG_vG3XQA0RR"
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer")
    file_to=input("enter the full path to upload to dropbox ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()
