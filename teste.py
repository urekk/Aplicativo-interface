import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload


CLIENTE_SECRET_FILE = 'cliente_secret_GoogleCloudDemo.json'
API_Name = "drive"
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENTE_SECRET_FILE, API_Name, API_VERSION, SCOPES)
file_ids = ['19XyzNNrNCI4u1MBqQVJUodcU02UHWVZK', '1ayhDeUfpa1n5IdLatIusawbLuMavq8s6']
file_names = ['test.xlsm', 'retriever.jpge']

for file_id, file_name in zip(file_ids,file_names)
    service.file().get_media(fileId=file_id)

    io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status, done = downloader.next_chunk()
        print('Download progress {0}', format(status.progress() * 100))
    fh.seek(0)

    with open (os.path.join('./Random files', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
