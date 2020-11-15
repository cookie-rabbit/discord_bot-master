import requests
import pinzhuang
from bs4 import BeautifulSoup
from urllib import parse


main_url = 'https://www.xivmodarchive.com'


def search(content):
    content = content.replace('!bot search ', '')
    x = 0
    result_data = []

    content = content.replace('\n', '')
    content = parse.quote(content)

    url_hash = "{}/search/{}?page=1".format(main_url, content)

    content = parse.unquote(content)
    response = requests.request("GET", url_hash)
    soup = BeautifulSoup(response.text, features="html.parser")
    try:
        names = soup.find_all(class_='card-title')
        href_collect = soup.find_all(class_='mod-card bg-dark text-light card my-2')[0:]
        modders = soup.find_all(class_='card-text mx-2')[0::2]
        count = soup.find("code", class_='text-light').text.split("Results over")[0].replace(" ", "")
        for i, j, z in zip(names, modders, href_collect):
            href = "https://www.xivmodarchive.com" + z.contents[1].attrs['href']
            name = i.attrs['title'] if i.attrs.get('title') else i.next
            modder = j.text
            tex = {"name": name, "href": href, "modder": modder}
            result_data.append(tex)
            x = x + 1
            if x >= 5:
                break
        result = {"search_content": content, "url": url_hash, "count": count, "data": result_data}
    except Exception as e:
        print(e)
        result = {"search_content": content, "url": url_hash, "count": 0, "data": ''}

    embed = pinzhuang.data_load(result)
    print("ok")
    return embed


search("!bot search Traveler's")
