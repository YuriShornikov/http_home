import requests

class Superheroes:
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'

    def get_all_superheroes(self):
        list_heroes = ['Hulk', 'Captain America', 'Thanos']
        list_intelligence = []
        url_all = '/all.json'
        request_url = self.base_url + url_all
        response = requests.get(request_url)
        res = response.json()
        for heroes in res:
            if heroes['name'] == 'Captain America' or heroes['name'] == 'Hulk' or heroes['name'] == 'Thanos':
                list_intelligence.append(heroes['powerstats']['intelligence'])
                max_num = max(list_intelligence)
        for heroes in res:
            for c in list_heroes:
                if heroes['powerstats']['intelligence'] == max_num and heroes['name'] == c:
                    the_cleverest = heroes['name']
                    print(f'Самый умный: {the_cleverest}')

if __name__ == '__main__':
    Sh = Superheroes()
    Sh.get_all_superheroes()



