import pygame
import requests
from bs4 import BeautifulSoup

pygame.init()
X = 480
Y = 320
# because this has no frame to quit, you will have to quit using CTRL+C in PowerShell
display_surface = pygame.display.set_mode((X, Y), pygame.NOFRAME) 

# colors
white = (255, 255, 255) 
red = (255, 0, 0)
green = (0 , 255, 0)
black = (0, 0, 0)
grey = (220, 220, 220)

def tickers():
	i = 1
	while True:
		# ticker1
		url = 'https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		price = float(soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
		open_ = float(soup.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
		change_ = float((price / open_) - 1)
		o_ch = ("{:.2f}".format(price - open_))
		percent_change = ("{:.2f}".format((change_ * 100)) + '%')
		font = pygame.font.Font('Bebas-Regular.otf', 40, bold = True)
		if change_ == 0:
			ourColor = white
		elif change_ > 0:
			ourColor = green
		else:
			ourColor = red
		# ticker2
		url2 = 'https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC'
		response2 = requests.get(url2)
		soup2 = BeautifulSoup(response2.text, 'lxml')
		price2 = float(soup2.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
		open_2 = float(soup2.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
		change_2 = float((price2 / open_2) - 1)
		o_ch2 = ("{:.2f}".format(price2 - open_2))
		percent_change2 = ("{:.2f}".format((change_2 * 100)) + '%')
		if change_2 == 0:
			ourColor2 = white
		elif change_2 > 0:
			ourColor2 = green
		else:
			ourColor2 = red
		# ticker 3
		url3 = 'https://finance.yahoo.com/quote/%5EIXIC/'
		response3 = requests.get(url3)
		soup3 = BeautifulSoup(response3.text, 'lxml')
		price3 = float(soup3.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
		open_3 = float(soup3.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
		change_3 = float((price3 / open_3) - 1)
		o_ch3 = ("{:.2f}".format(price3 - open_3))
		percent_change3 = ("{:.2f}".format((change_3 * 100)) + '%')
		if change_3 == 0:
			ourColor3 = white
		elif change_3 > 0:
			ourColor3 = green
		else:
			ourColor3 = red
		#adds the plus sign before a positive number
		if price-open_ > 0:
			plus = '+'
		else:
			plus = ''
		if price2-open_2 > 0:
			plus2 = '+'
		else:
			plus2 = ''
		if price3-open_3 > 0:
			plus3 = '+'
		else:
			plus3 = ''
		# what to display
		stockname = font.render('DJIA' + '    ' + ("{:.2f}".format(price)), True, white)
		stocknameRect = stockname.get_rect()
		stocknameRect.center = (X // 2, 40)
		text = font.render('('+plus+str(o_ch) + '  ,  ' +plus+percent_change+')', True, ourColor)
		textRect = text.get_rect()
		textRect.center = (X // 2, 80)
		
		stockname2 = font.render('S&P' + '    ' + ("{:.2f}".format(price2)), True, white)
		stocknameRect2 = stockname2.get_rect()
		stocknameRect2.center = (X // 2, 140)
		text2 = font.render('('+plus2+str(o_ch2) + '  ,  ' +plus2+percent_change2+')', True, ourColor2)
		textRect2 = text2.get_rect()
		textRect2.center = (X // 2, 180)
		
		stockname3 = font.render('NASDAQ' + '    ' + ("{:.2f}".format(price3)), True, white)
		stocknameRect3 = stockname3.get_rect()
		stocknameRect3.center = (X // 2, 240)
		text3 = font.render('('+plus3+str(o_ch3) + '  ,  ' +plus3+percent_change3+')', True, ourColor3)
		textRect3 = text3.get_rect()
		textRect3.center = (X // 2, 280)
		
		#data loop to display
		if i > 0:
			display_surface.fill(black)
			display_surface.blit(stockname, stocknameRect)
			display_surface.blit(text, textRect)
			display_surface.blit(stockname2, stocknameRect2)
			display_surface.blit(text2, textRect2)
			display_surface.blit(stockname3, stocknameRect3)
			display_surface.blit(text3, textRect3)
			for event in pygame.event.get() : 
			    if event.type == pygame.QUIT :
			    	pygame.quit() 
			    	quit()  
			pygame.display.update()
			i += 1
tickers()
