from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://snowe.sookmyung.ac.kr/bbs5/boards/cafeteria/rss")
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
body_div = soup.find('tbody')
trs = body_div.findAll('tr')

p_div = trs[1].findAll('td')

mon = p_div[1].text
tue = p_div[2].text

print(tue)
