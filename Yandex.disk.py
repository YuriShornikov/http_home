import requests

class YaUploader:
    # base_host = 'https://cloud-api.yandex.net:443/'
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_uri = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_uri, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload(self, local_path, file_path: str):
        upload_url = self._get_upload_link(file_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка успешна')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 't2.jpg'
    token = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, '/t2.jpg')
    # result = uploader.upload(path_to_file, '/t2.jpg')