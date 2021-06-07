import requests
from bs4 import BeautifulSoup

def take_the_list(x=3):
    url = "http://www.allscrabblewords.com/"+str(x)+"-letter-words/"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    get= soup.find_all("ul", {"class": "list-inline"})

    get[0] = get[0].text
    all_words = get[0].split("   ")
    all_words = [i.strip() for i in all_words]

    return all_words

letters = list()

def eliminate(liste,letters):
    return_list = list()
    if_add = False
    for word in liste:
        if_add = True
        for letter in word:
            if letter not in letters or list(word).count(letter) > letters.count(letter):
                if_add = False
        if if_add:
            return_list.append(word)
    return return_list

while True:
    letters = input("Lütfen harfleri bitişik girin: ")

    for word_length in range (3,7):
        print(" **************\n" +
        str(word_length) + " HARFLİ KELİMELER\n" +
        " *************** ")
        for each in eliminate(take_the_list(word_length), [*letters]):
            print(each)
    break

