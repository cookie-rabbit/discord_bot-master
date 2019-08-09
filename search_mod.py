import requests
import pinzhuang
from bs4 import BeautifulSoup
from urllib import parse

main_url = 'https://www.xivmodarchive.com'


def search(content):
    z = 0
    result_data = []

    content = content.replace('\n', '').replace(' ', '')
    content = parse.quote(content)

    url_hash = "{}/search/{}?page=1".format(main_url, content)
    response = requests.request("GET", url_hash)
    soup = BeautifulSoup(response.text, features="html.parser")
    # try:
    names = soup.find_all(class_='card-title')
    href_collect = soup.find_all(class_='mod-card card bg-dark text-light my-3')[0:]
    modders = soup.find_all(class_='card-text mx-2')[0::2]
    count = soup.find("code", class_='text-light').text.split("Results over")[0].replace(" ", "")
    for i, j, z in zip(names, modders, href_collect):
        href = "https://www.xivmodarchive.com/mod" + z.contents[1]['href']
        name = i.text
        modder = j.text
        tex = {"name": name, "href": href, "modder": modder}
        result_data.append(tex)
        z = z + 1
        if z >= 5:
            break
    result = {"search_content": content, "url": url_hash, "count": count, "data": result_data}
    # except:
    #     result = {"search_content": content, "url": url_hash, "count": 0, "data": ''}

    embed = pinzhuang.data_load(result)
    print("ok")
    return embed


search('sweater')
