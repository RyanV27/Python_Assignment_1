import requests as rq
from bs4 import BeautifulSoup
import html5lib

def main():
    url = input("Enter URL: ")
    
    request = rq.get(url)
    soup = BeautifulSoup(request.content, "html5lib")
    images = soup.find_all("img")

    count = 1
    for i in images: 
        try:
            if "https://" not in i['src']:
                r = rq.get("https:" + i['src']).content
            else:
                r = rq.get(i['src']).content

            with open(f"Image_{count}.jpg", 'wb') as fout:
                fout.write(r)
            
            count += 1
        except:      
            continue 
main()