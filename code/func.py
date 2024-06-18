import time
import json
import requests
import data
from bs4 import BeautifulSoup

'''
получение данных и скаичвание файлов
'''
def pars_data(url, q='', inAbout='0',
              categories=[],countries="Россия",
              languages="Руссикй",channelType = "",
              isVerified=0,
              participantsCountFrom="",
              participantsCountTo="",
              avgReachFrom = "",
              avgReachTo = "",
              avgReach24From = "",
              avgReach24To = "",
              ciFrom = "",
              ciTo = "",
              age = "0",
              err = "0",
              noRedLabel = "1",
              noScam = "1",
              noDead = "1",
              ):
    categories = get_categories(categories)
    countries = get_countries(countries)
    languages = get_languages(languages)
    date_pars = change_data(q,inAbout,categories,countries,languages,
                   channelType,
                   isVerified,
                   participantsCountFrom,
                   participantsCountTo,
                   avgReachFrom,
                   avgReachTo,
                   avgReach24From,
                   avgReach24To,
                   ciFrom,
                   ciTo,
                   age,
                   err,
                   noRedLabel,
                   noScam,
                   noDead,)
    responce = requests.post(url=url,
                            headers=data.headers,
                            data=date_pars)
    if (responce.status_code !=200):
        print("[ERROR] STATUS CODE ERROR", responce.status_code)
        exit(0)
    responce.encoding = 'utf-8'
    page = json.loads(str(responce.text))['html']
    soup = BeautifulSoup(page, 'lxml')
    links = soup.find_all('a', {'target':'_blank'})
    names = get_name(page)
    photos = get_photo(page)
    for name, link, photo in zip(names, links, photos):
        link = "https://t.me/joinchat/"+link.get("href").split('/')[4]
        responce=requests.get(url = photo)
        with(open(f"photo/{name}.jpg", "wb+")) as file:
            file.write(responce.content)
        time.sleep(1)
        print(name, link, photo)

'''
получение фото
'''
def get_photo(text_page):
    soup = BeautifulSoup(text_page, 'lxml')
    soup = soup.find_all("img", class_="rounded-circle")
    photo = []
    for i in soup:
        photo.append("https:"+i.get("src"))
    return photo

'''
получение имени
'''
def get_name(text_page):
    soup = BeautifulSoup(text_page, 'lxml')
    soup = soup.find_all("div", class_="text-truncate")
    names = []
    for index, name in enumerate(soup):
        if (index % 6 == 0):
            names.append(name.text)
    return names

'''
получение категорий
'''
def get_categories(categories):
    categories = categories.split(',')
    return_array = []
    for i in categories:
        return_array.append(data.category.get(i))
    return return_array

'''
получение стран
'''
def get_countries(countries):
    countries = countries.split(',')
    return_array = []
    for i in countries:
        return_array.append(data.countries.get(i))
    return return_array

'''
получение языков
'''
def get_languages(languages):
    languages = languages.split(',')
    return_array = []
    for i in languages:
        return_array.append(data.languages.get(i))
    return return_array

'''
создание словаря
'''
def change_data(q,inAbout,categories,countries,languages,
                   channelType,
                   isVerified,
                   participantsCountFrom,
                   participantsCountTo,
                   avgReachFrom,
                   avgReachTo,
                   avgReach24From,
                   avgReach24To,
                   ciFrom,
                   ciTo,
                   age,
                   err,
                   noRedLabel,
                   noScam,
                   noDead,):
    data_dict = data.data
    data_dict['q'] = q
    data_dict['inAbout'] = inAbout
    data_dict['categories'] = categories
    data_dict['countries'] = countries
    data_dict['languages'] = languages
    data_dict['channelType'] = channelType
    data_dict['isVerified'] = isVerified
    data_dict['participantsCountFrom'] = participantsCountFrom
    data_dict['participantsCountTo'] = participantsCountTo
    data_dict['avgReachFrom'] = avgReachFrom
    data_dict['avgReachFrom'] = avgReachFrom
    data_dict['avgReachTo'] = avgReachTo
    data_dict['avgReach24From'] = avgReach24From
    data_dict['avgReach24To'] = avgReach24To
    data_dict['ciFrom'] = ciFrom
    data_dict['ciTo'] = ciTo
    data_dict['age'] = age
    data_dict['err'] = err
    data_dict['noRedLabel'] = noRedLabel
    data_dict['noScam'] = noScam
    data_dict['noDead'] = noDead
    return data_dict