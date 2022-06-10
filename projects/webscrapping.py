
import requests
from bs4 import BeautifulSoup as bs

#input("Enter your name :")
user_name = "Carolynembugua"
#input("Enter site url :")
url = "https://github.com/"+user_name
results = requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})['src']
print(profile_pic)