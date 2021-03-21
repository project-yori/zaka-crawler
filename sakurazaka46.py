import requests
import downloader
from bs4 import BeautifulSoup

URL = 'https://sakurazaka46.com'
DEFAULT_SIZE_URL = '/400_320_102400'

response = requests.get(f'{URL}/s/s46/search/artist?ima=0348')
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

groups = soup.find_all(class_='col2-wrap')

group_info = {}

for group in groups:
    group_name = group.find(class_='com-title-type0').getText()
    
    members = group.find_all(class_='box')
    member_list = []
    for member in members:
        member_info = {'name': member.find(class_='name').getText(),
                       'kana': member.find(class_='kana').getText()}
        img_url = member.find('img')['src']
        member_info['img'] = img_url.replace(DEFAULT_SIZE_URL, '')
        member_list.append(member_info)
        file_name = f'{member_info["name"]}.jpg'
        print(f'{file_name} is downloading')
        downloader.download_file(f'{URL}{member_info["img"]}', file_name)
        print(f'{file_name} download was finished')

    group_info[group_name] = member_list

