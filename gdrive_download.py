from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os


def gg(name):
    settings_path = 'settings.yaml'
    gauth = GoogleAuth(settings_file=settings_path)

    gauth.LoadCredentialsFile("mycreds1.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds1.txt")

    drive = GoogleDrive(gauth)
    print('Started!!')
    file_list = drive.ListFile({'q': "'YOUR API KEY' in parents and trashed=False"}).GetList()
    f = drive.CreateFile({'title': f"{name}_final.csv", 'parents': [{'id': 'YOUR API KEY'}]}) #change to your drive id
    file_name = f['title']
    print('File name read....\n')

    try:
        for f1 in file_list:
            print(f1)
            if f1['title'] == file_name:
                print("Downloading")
                if os.path.exists(f"{name}_final.csv"):
                    os.remove(f"{name}_final.csv")
                f1.GetContentFile(f"{name}_final.csv")

    except:
        print('Unable to get file.')




