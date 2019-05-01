import requests
from bs4 import BeautifulSoup

url = "https://ia800301.us.archive.org/cdrview.php?cdr=/11/items/GifsGalore_Aug92/GifsGalore_Aug92.cdr"
output = open("links.txt", "a", encoding="UTF-8")
requ=requests.get(url=url)
soup = BeautifulSoup(requ.content, "html.parser")
image_urls = soup.find('table', attrs={"class": "archext"}).find_all('a')
for i in range(len(image_urls)):
    image = image_urls[i].attrs['href']
    if ".GIF" in image:
        link = "https:" + image + "\n"
        output.write(link)
        output.flush()
