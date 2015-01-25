from bs4 import BeautifulSoup
import requests
HEAD={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
#x = 4605246004766
#x = 4607108750729
x = 4606180007677
raw_data = requests.get ('https://olegon.ru/barcodes/' + str(x) + '.htm', headers=HEAD)
soup = BeautifulSoup(raw_data.text.encode('ISO-8859-1'))
str = soup.find(attrs={'class': 'style1'}).text
ans = str[str.find(':\n') + 2:str.find('Trans')]
words = ans.split(' ')
new_str = ' '
for word in words:
	if new_str.lower().find(' ' + word.lower() + ' ') != -1:
		break
	new_str = new_str + word + ' '

print new_str[1:]
