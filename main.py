import requests
import json
import os
import time
import urllib.parse
import pathlib
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg
import vk_api
import time
import threading
import multiprocessing
# 6ea1ba87fc429e807182d512dae6c502b89a85c43b455215883a1076c07e9b825dfb37d0966b98a0e3489
# 24aa810149f9fcee0755dccb54abedf13541e1265bd107d71a2c5f3ab76bfbae79411804708ce1cccae8c
import vk_api
import time
import requests
import bs4
import random
import urllib.parse
import re
import time
from random import randrange
import os

from selenium.webdriver.firefox.options import Options


sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#303030',
                                        'TEXT': '#ffffff',
                                        'INPUT': '#444444',
                                        'TEXT_INPUT': '#aaaaaa',
                                        'SCROLL': '#000000',
                                        'BUTTON': ('#f0f0f0', '#555555'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, }

sg.theme('MyCreatedTheme')




def engine(login, psw, str_zapros, page):
	options = Options()
	# options.headless = True
	# browser = webdriver.Firefox(executable_path="/home/ilnur/geckodriver")
	browser = webdriver.Firefox( options=options, executable_path="/home/ilnur/geckodriver")
	data_str='filter=&orderColumn=RELEVANCE_DESC&page=0&pageSize=1000'
	data_en=urllib.parse.quote(data_str)
	payload={}
	url_all_e='https://trudvsem.ru/iblocks/_catalog/flat_filter_prr_search_cv/data'




	str_cookie='geolocation=7800000000000; geolocation-name=%D0%B3.%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; region-choose-first-visit=true; iblocksapi=3b40daf89f6547d056f37e4d9d03ca91; ID=Fj16gNSt69qLauAmzI_oEmP-ZHVZOENDV-5LrTgWuA_awtOm6abyPrEwy1LP-EUB; iblocksapimanager=f134614a104dedcf411f9f8e46f50815; prr:site:agreement=true; JSESSIONID=MDhlNDcxNzAtNzcyNC00OTQ1LTk2NDktMjUzODc0YzlmZTU4; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJwcnIiOnsiaWQiOiJiOGFiMzQ2MC00NGM0LTExZWQtOTllYS1hN2Y3NjdjM2NmYjMifSwibmJmIjoxNjY0OTkzNjI2LCJqd3QiOiJmNWFhY2ExZC1iMTk0LTRlYTktODliMS0yZDA5ZmVkMDVkYjIiLCJpc3MiOiJiZnQtand0LXNlcnZpY2UiLCJleHAiOjE2NjQ5OTQyMjYsImlhdCI6MTY2NDk5MzYyNiwiZXNpYUlkIjoiMTA2ODk2MTY5NCJ9.nDWhpqpQwFhK6pxIXq_qjf4j1WCPgeEbZl7wLZBuZj00i_eZQhV6KQ4_onul8gOc; refreshToken=036f2988-7729-4205-af50-c7a8bfc1d766'
	browser.get("https://trudvsem.ru/auth/login#employer")
	browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div/form/button").click()
	time.sleep(20)
	browser.find_element(By.XPATH, '//*[@id="login"]').send_keys(login)
	browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(psw)
	browser.find_element(By.XPATH, '/html/body/esia-root/div/esia-login/div/div[1]/form/div[4]/button').click()
	time.sleep(2)
	browser.find_element(By.XPATH, '/html/body/div/div/div[2]/button[2]/div[2]').click()
	time.sleep(5)
	# browser.get(url_all_e)
	# cookies=browser.get_cookies()
	print("\n\n\n\n\n")





	headers = {
			# 'Cookie': str_cookie,
			# 'Referer':'https://trudvsem.ru/cv/search?_title=%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80&_regionIds=7700000000000&page=0&professionalSphere=Marketing'

			}


	params={

	
		"filter":'{"title":["электрик"],"regionCode":["1100000000000"]}',
		"orderColumn":"RELEVANCE_DESC",
		"age":["18,65"],
		"page":str(page),
		"pageSize":'1000',	

	}







	response = requests.get(url_all_e, headers=headers, params=params)
	data=response.json()
	print(len(data["result"]["data"]))
	i=0
	os.chdir("CVs")
	try:
		os.chdir(str_zapros)
		pass
	except FileNotFoundError as e:
		os.mkdir(str_zapros)
		os.chdir(str_zapros)
		print(e)

	for x in data["result"]["data"]:
		i=i+1
		if 0==0:
			# url='https://trudvsem.ru/cv/card/print?candidateId='+str(x[1])+'&cvId='+str(x[0])+''
			url='https://trudvsem.ru/cv/card/print?candidateId='+str(x[1])+'&cvId='+str(x[0])+''
			browser.get(url)
			time.sleep(3)
			info=browser.find_elements(By.CLASS_NAME,'col')
			filename=str(i)+" "+browser.title
			filename=filename.replace('/', '_')
			filename=filename.replace('.', '_')
			filename=filename.replace('-', '_')
			filename=filename.replace('\\', '_')
			filename=filename.replace(',', '_')
			if len(filename)>59:
				filename=filename[0:59]
				pass
			f=open(filename+".txt","w")
			for x in info:
				print(x.text)
				with open(filename+".txt", "a") as ff:
					ff.write(x.text+"\n")
				pass
			time.sleep(3)
	pass





























tab4_layout = [[sg.Text("HEAD RECRUITER by PEACE (dev1ce).", text_color="red")],

[sg.Text("ГОСУСЛУГИ: ")],
[sg.Text("Логин ",text_color="#cccccc"), sg.Input("radian-kch@yandex.ru",size=(15,1),  key="login_gsg") ],
[sg.Text("Пароль ",text_color="#cccccc"), sg.Input("Radian-72", size=(15,1), key="psw_gsg") ],
[sg.Text("")],
[sg.Text("Запрос ",text_color="#dddddd"), sg.Input("ELECTRICIANS",size=(22,1),  key="zapros")],

[sg.Text("")],
[sg.Button("Запустить выгрузку.")],
[sg.Text("")],
[sg.Text("Статус.", key="status")  ],
[sg.Text("")],

]


layout = [[sg.TabGroup([[sg.Tab('Head finder', tab4_layout,),
                         ]])]]

window = sg.Window('AD killer', layout, margins=(1,1) , default_element_size=(75, 120))


while True:
	event, values = window.read()
	if event == "Запустить выгрузку.":
		zapros=values["zapros"]
		login_gsg=values["login_gsg"]
		psw_gsg=values["psw_gsg"]

		engine(login_gsg, psw_gsg, zapros,0)
		pass
	if event == sg.WIN_CLOSED:
		try:
			sys.exit()
			pass
		except Exception as e:
			print(e)
		break