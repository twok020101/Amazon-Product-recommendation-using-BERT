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
    path = (f"D:/Mini-project(V sem)/Amazon_product_review_system/.idea/{name}.csv") #Change to your system path where csv file is stored
    print('Started!!')
    file_list = drive.ListFile({'q': "'1zH0L2gDTC9tZTdrz49j3BmtgnAe0M9QW' in parents and trashed=False"}).GetList()
    f = drive.CreateFile({'title': f"{name}", 'parents': [{'id': '1zH0L2gDTC9tZTdrz49j3BmtgnAe0M9QW'}]})
    file_name = f['title']
    print('File name read....\n')

    try:
        for f1 in file_list:
            if f1['title'] == file_name:
                f1.Delete()
                print('Match found and file deleted....\n')
    except:
        print('Unable to get file.')

    x = os.path.join(path).replace("\\", r"/")
    f.SetContentFile(x)
    f.Upload()
    print(f'{file_name} uploaded successfully!!')
    f = None
