import requests

# Hulk_id = '332'
# Cap_id = '149'
# Thanos_id = '655'


class Superheroes:
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'

    # def __init__(self, heroes_id):
    #     self.heroes_id = heroes_id

    def get_all_superheroes(self):
        url_all = '/all.json'
        request_url = self.base_url + url_all
        response = requests.get(request_url)
        res = response.json()
        for keys, values in res[0].items():
            if values == "Captain America":
                print(values)
        # print(res)

if __name__ == '__main__':
    Sh = Superheroes()
    Sh.get_all_superheroes()



