import pandas as pd
import numpy
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re

import Celular

class phoneArena:
	
	"""docstring for phoneArena"""
	
	def __init__(self, aparelho):
		super(phoneArena, self).__init__()
		self.aparelho = aparelho

	def executa(self):

		# Site que iremos procurar os smartphones
		link = 'https://www.phonearena.com/'

		# Navegadores abertos para pesquisa do elementos
		driver = webdriver.Chrome('/home/kaio/Desktop/UFV/POC/Repositório/analise-usuarios/Crawlers/Kimovil/Coleta Dados/chromedriver')
		driver.get(link)
		
		celular = Celular.celular()

		def escolhe(aparelho, driver, celular, link):

			try:
				if (driver.find_element_by_xpath('//*[@id="phones"]/div/p').text): # Caso em que o nome procurado não é encontrado no site
					log = open('logs.txt', 'a')
					log.write('O Aparelho '+aparelho+' não foi encontrado, com esse nome, no site '+link+'.\n\n')
					log.close()
					return celular
			except Exception:

				principal_cel1 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[1]/h3/a').text
				
				if aparelho == principal_cel1:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[1]/h3/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel2 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[2]/h3/a').text
				if aparelho == principal_cel2:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[2]/h3/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel3 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[3]/h3/a').text
				if aparelho == principal_cel3:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[3]/h3/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel4 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[4]/h3/a').text
				if aparelho == principal_cel4:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[4]/h3/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel5 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[5]/h3/a').text
				if aparelho == principal_cel5:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[5]/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel6 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[6]/h3/a').text
				if aparelho == principal_cel6:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[6]/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel7 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[7]/h3/a').text
				if aparelho == principal_cel7:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[7]/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					principal_cel8 = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[8]/h3/a').text
				if aparelho == principal_cel8:
					smartphone = driver.find_element_by_xpath('//*[@id="phones"]/div[1]/div[8]/a').click()
					getValuePhoneArena(aparelho, driver, celular)
					return celular
				else:
					log = open('logs.txt', 'a')
					log.write('Aparelho '+aparelho+" não encontrado, com esse nome, nos sites.\n\n")
					log.close()
			else:
				return celular

		def getValuePhoneArena(aparelho, driver, celular):
			try:
				Capacidade_Bateria = driver.find_element_by_xpath('//*[@id="battery_cPoint"]/ul/li[1]/ul/li').text

				celular.setBateria(Capacidade_Bateria.split(" ")[0])
			except Exception:
				celular.setBateria('')
			
			try:
				Memoria_Ram = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[4]/ul/li/ul/li').text
				Memoria_Ram = Memoria_Ram.split(' ')[0]
				
				if (float(Memoria_Ram) > 100): #Comparando como float
					nova_Memoria_Ram = ('0' + '.' + Memoria_Ram) # Adicionando o "0." para transformar de MB para GB
				else:
					nova_Memoria_Ram = Memoria_Ram
				
				celular.setRam(nova_Memoria_Ram)
			except Exception:
				celular.setRam('')
			
			try:
				Memoria_Armazenamento = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[5]/ul/li').text
				Memoria_Armazenamento = Memoria_Armazenamento.split(' ')[0]
				
				if (Memoria_Armazenamento[0] == '['):
					new_Memoria_Armazenamento = Memoria_Armazenamento.split('\n')[1]
					new_Memoria_Armazenamento = new_Memoria_Armazenamento.split(' ')[0]
				else:
					new_Memoria_Armazenamento = Memoria_Armazenamento
				
				celular.setArmazenamento(new_Memoria_Armazenamento)
			except Exception:
				celular.setArmazenamento('')
			
			try:
				Bluetooth = driver.find_element_by_xpath('//*[@id="connectivity_cPoint"]/ul/li[1]/ul/li/ul/li').text

				celular.setBluetooth(Bluetooth[0]+Bluetooth[1]+Bluetooth[2])
			except Exception:
				celular.setBluetooth('')
			
			try:
				try:
					NFC = driver.find_element_by_xpath('//*[@id="connectivity_cPoint"]/ul/li[6]/ul/li').text
				except Exception:
					NFC = driver.find_element_by_xpath('//*[@id="connectivity_cPoint"]/ul/li[5]/ul/li').text

				if (NFC.find('NFC') > -1) | (NFC.find('nfc') > -1):
					celular.setNfc('SIM')
				else:
					celular.setNfc('NAO')
			except Exception:
				celular.setNfc('')
			
			## Não está bem implementado
			try:
				try:
					Dual_chip = driver.find_element_by_xpath('//*[@id="cellular_cPoint"]/ul/li[6]/strong').text
				except Exception:
					celular.setDualChip('NAO')
				#'//*[@id="phone"]/div[4]'

				if (Dual_chip.find('Dual') > -1):
					celular.setDualChip('SIM')
				else:
					Dual_chip = driver.find_element_by_xpath('//*[@id="cellular_cPoint"]/ul/li[7]/strong').text
					if (Dual_chip.find('Dual') > -1):
						celular.setDualChip('SIM')
					else:
						celular.setDualChip('NAO')
				#tem_Dual = str.find(Dual_chip, "2 slots")
				#if tem_Dual > -1:
			except Exception:
				celular.setDualChip('')
			
			try:
				#Lte = driver.find_element_by_xpath('//*[@id="cellular_cPoint"]').text
				Lte = driver.find_element_by_xpath('//*[@id="cellular_cPoint"]/ul').text
				Lte1 = driver.find_element_by_xpath('//*[@id="cellular_cPoint"]/ul/li[4]').text

				if (Lte.find('LTE')) > -1 | (Lte.find('lte')) > -1:
					celular.setLte('SIM')
				else:
					celular.setLte('NAO')
				
				#tem_lte = str.find(Lte, "LTE")
				
			except Exception:
				celular.setLte('')
			
			try:
				Resoluçao_camera = driver.find_element_by_xpath('//*[@id="camera_cPoint"]/ul/li[1]/ul/li[1]/ul').text
				
				celular.setResolucaoCam(Resoluçao_camera.split(" ")[0])
			except Exception:
				celular.setResolucaoCam('')
			
			try:
				Peso = driver.find_element_by_xpath('//*[@id="design_cPoint"]/ul/li[2]/ul/li').text
				Peso = Peso.split(' ')[2]

				celular.setPeso(Peso[1:])
			except Exception:
				celular.setPeso('')
			
			try:
				Dimensao = driver.find_element_by_xpath('//*[@id="design_cPoint"]/ul/li[1]/ul/li').text
				teste = Dimensao.split('(')
				numero = teste[1].split(" ")
				
				celular.setDimensoes(numero[0],numero[2],numero[4])
			except Exception:
				celular.setDimensoes('')
			
			try:
				Tamanho_tela = driver.find_element_by_xpath('//*[@id="display_cPoint"]/ul/li[1]/ul/li').text

				celular.setTela(Tamanho_tela.split(' ')[0])
			except Exception:
				celular.setTela('')
			
			try:
				#SO = driver.find_element_by_xpath('//*[@id="design_cPoint"]/ul/li[2]/ul/li').text
				try:
					SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[8]/ul/li').text
					if (SO.find('Android') > -1) | (SO.find('iOS') > -1):
						celular.setSo(SO.split(' ')[0])
				except Exception:
					try:
						SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[7]/ul/li').text
						if (SO.find('Android') > -1) | (SO.find('iOS') > -1):
							celular.setSo(SO.split(' ')[0])
					except Exception:
						SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[6]/ul/li').text
						if (SO.find('Android') > -1) | (SO.find('iOS') > -1):
							celular.setSo(SO.split(' ')[0])
						else:
							celular.setSo('')
							
			except Exception:
				worksheet.write(linha + 1, 15, '')
			
			try:
				flag = 0
				conc = '' # Variáveis auxiliares para compor a liste de sistemas operacionais
				try:
					Versao_SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[8]/ul/li').text
					if (Versao_SO.find('Android') > -1):
						vetorVersaoSO = re.findall(r'(\d+.\d+)',Versao_SO)
					else:
						if (SO.find('iOS') > -1):
							vetorVersaoSO = re.findall(r'(\d+)',Versao_SO)
					
					for item in vetorVersaoSO:
						if (flag != 0) & (flag < len(vetorVersaoSO)):
							conc = conc + ', '
						conc = conc + item
						celular.setVersaoSo(conc)
						flag = flag + 1
					
				except Exception:
					try: 
						Versao_SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[7]/ul/li').text
						if (Versao_SO.find('Android') > -1):
							vetorVersaoSO = re.findall(r'(\d+.\d+)',Versao_SO)
						else:
							if (SO.find('iOS') > -1):
								vetorVersaoSO = re.findall(r'(\d+)',Versao_SO)
						
						for item in vetorVersaoSO:
							if (flag != 0) & (flag < len(vetorVersaoSO)):
								conc = conc + ', '
							conc = conc + item
							celular.setVersaoSo(conc)
							flag = flag + 1
						
					except Exception:
						Versao_SO = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[6]/ul/li').text
						if (Versao_SO.find('Android') > -1):
							vetorVersaoSO = re.findall(r'(\d+.\d+)',Versao_SO)
						else:
							if (SO.find('iOS') > -1):
								vetorVersaoSO = re.findall(r'(\d+)',Versao_SO)

						for item in vetorVersaoSO:
							if (flag != 0) & (flag < len(vetorVersaoSO)):
								conc = conc + ', '
							conc = conc + item
							celular.setVersaoSo(conc)
							flag = flag + 1

			except Exception:
				celular.setVersaoSo('')
			
			try:
				Processamento = driver.find_element_by_xpath('//*[@id="hardware_cPoint"]/ul/li[2]/ul/li').text
				Processamento = Processamento.split(',')[1]
				
				celular.setProcessamento(Processamento.split(' ')[1])
			except Exception:
				celular.setProcessamento('')
			
			try:
				Ano_lançamento = driver.find_element_by_xpath('//*[@id="phone_specificatons"]/div/div[11]/ul/li[1]/ul/li[1]/ul/li').text

				celular.setDataLancamento(Ano_lançamento)
			except Exception:
				celular.setDataLancamento('')

			return celular

		pesquisa = driver.find_element_by_xpath('//*[@id="term"]')
		pesquisa.send_keys(self.aparelho)
		pesquisa.send_keys(Keys.ENTER)

		escolhe(self.aparelho, driver, celular, link)

		driver.close()

		return celular