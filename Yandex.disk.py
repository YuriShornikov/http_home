import requests

# from settings import TOKEN

class YaUploader:
    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'v1/disk/resources/'
        request_url = self.base_host + url
        params = {'href': 'string', 'method': 'string', 'templated': True}
        responce = requests.put(request_url, params=params)
        print(responce.json())
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)