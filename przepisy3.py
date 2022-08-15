#http://przepisy.swiatkobiety.pl/ciasta-desery/news-lekkie-ciasto-z-bakaliami,nId,2285376

import requests
from bs4 import BeautifulSoup


while True:

    class __init__():

        def reqest(site):

            def strr(abc):

                abc = list(abc)
                n = abc.count("\n")
                t = abc.count("\t")
                o = abc.count ("więcej")
                for i in range(n):
                    abc.remove("\n")
                for j in range(t):
                    abc.remove("\t")
        
                abc = "".join(abc)
                return abc


            req = requests.get(site)

            soup = BeautifulSoup(req.text, "lxml")
            body = soup.body

            title = body.find("h1")
            title = title.text
#subtitle = body.find("h3")
#subtitle = subtitle.text

#list_all_p=soup.find_all("p")
#print(f'znalazłem {len(list_all_p)} linków')
#list_all_p[10].get_text()

            div =body.select("div p", {"class": "boxBody"})

            print("\n")
            print("\n")
            print(title)
            print("\n")
#print(subtitle)
            print("\n")

            for x in div:
                xc = x.text
                xc = strr(xc)
                print(xc)

            print("\n")


        
        
        lis = []
        list_all_p = []
        
        site =(input("Poddaj linka do przepisu: "))

        start = reqest(site)
        




