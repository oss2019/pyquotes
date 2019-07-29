from bs4 import BeautifulSoup
import requests
import random
import os

# website to get wallpapers
parent_link = 'https://pixabay.com/images/search/wallpaper/'

def get_wallpapers():
	""" returns a list of links of wallpapers """
	lst = list()
	item = requests.get(parent_link).text
	soup = BeautifulSoup(item,'lxml')
	var = soup.find_all('div',attrs = {'class':'item'})
	for images in var:
		image = images.find('img')
		interest = image.get('src')
		if 'http' in interest:
			lst.append(interest)
	return lst

if __name__=='__main__':
	lst = get_wallpapers()
	image = random.choice(lst)
	name = image[47:]
	r = requests.get(image)
	with open(name,'wb') as f:
		f.write(r.content)
	print('downloaded ',name)


# use the following to automate using cron tab every midnight
# 0 0 * * * python3 nn.py