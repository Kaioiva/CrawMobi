import pandas as pd
import numpy
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re

import Zoom
import Celular

class kimovil:

	"""docstring for kimovil"""

	def __init__(self, aparelho):
		super(kimovil, self).__init__()
		self.aparelho = aparelho

	def executa(self):

		# Site que iremos procurar os smartphones
		link = 'https://www.kimovil.com/pt/'

		# Navegadores abertos para pesquisa do elementos
		driver = webdriver.Chrome('/home/kaio/Desktop/UFV/POC/Repositório/analise-usuarios/Crawlers/Kimovil/Coleta Dados/chromedriver')
		driver.get(link)

		celular = Celular.celular()

		# Funções utilizadas na execução

		''' Função para procurar o aparelho correto, dentro dos disponíveis após pesquisa, no site Kimovil.
		Depois da pesquisa são dados vários cards contendo celulares com nomes parecidos. Todo trabalho abaixo consiste em 
		verificar nos 15 primeiros cards se possuem o nome idêntico ao pesquisado no site kimovil. Caso não ocorra a 
		incidência, o aparelho é dado como não encontrado '''
		def escolhe(aparelho, driver, celular, link):

			if (driver.find_element_by_xpath('//*[@id="results"]/div[3]/h3').text): # Caso em que o nome procurado não é encontrado no site
				log = open('logs.txt', 'a')
				log.write('O Aparelho '+aparelho+' não foi encontrado, com esse nome, no site '+link+'.\n\n')
				log.close()
				return celular

			principal_cel1 = driver.find_element_by_xpath('//*[@id="results-list"]/li[1]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel1.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[1]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel2 = driver.find_element_by_xpath('//*[@id="results-list"]/li[2]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel2.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[2]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				principal_cel3 = driver.find_element_by_xpath('//*[@id="results-list"]/li[3]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel3.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[3]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				principal_cel4 = driver.find_element_by_xpath('//*[@id="results-list"]/li[4]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel4.upper():        
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[4]/div[2]/a[2]/div[2]/div[1]/span[1]').click()        
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				principal_cel5 = driver.find_element_by_xpath('//*[@id="results-list"]/li[5]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel5.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[5]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel6 = driver.find_element_by_xpath('//*[@id="results-list"]/li[6]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel6.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[6]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel7 = driver.find_element_by_xpath('//*[@id="results-list"]/li[7]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel7.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[7]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel8 = driver.find_element_by_xpath('//*[@id="results-list"]/li[8]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel8.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[8]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel9 = driver.find_element_by_xpath('//*[@id="results-list"]/li[9]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel9.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[9]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel10 = driver.find_element_by_xpath('//*[@id="results-list"]/li[10]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel10.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[10]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel11 = driver.find_element_by_xpath('//*[@id="results-list"]/li[11]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel11.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[11]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel12 = driver.find_element_by_xpath('//*[@id="results-list"]/li[12]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel12.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[12]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel13 = driver.find_element_by_xpath('//*[@id="results-list"]/li[13]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel13.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[13]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel14 = driver.find_element_by_xpath('//*[@id="results-list"]/li[14]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel14.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[14]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel15 = driver.find_element_by_xpath('//*[@id="results-list"]/li[15]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel15.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[15]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular

		# Função para atribuição dos valores ao objeto celular
		def getValueKimovil(aparelho, driver, celular):
			try:
				Marca = driver.find_element_by_xpath('//*[@id="about"]/div/div[1]/div[2]/dl/dd[1]').text #Kimovil
				temp_marca = Marca.split("\n")

				celular.setMarca(temp_marca[0])
			except Exception:
				celular.setMarca('')

			try:
				Modelo = driver.find_element_by_xpath('//*[@id="basics"]/div/div[2]/h1').text #Kimovil
				temp_modelo = Modelo.split("\n")

				celular.setModelo(temp_modelo[1])
			except Exception:
				celular.setModelo('')

			try:
				Capacidade_Bateria = driver.find_element_by_xpath('//*[@id="battery"]/div/div[1]/div[2]/dl/dd[1]').text #Kimovil

				celular.setBateria(Capacidade_Bateria.split(" ")[0])
			except Exception:
				celular.setBateria('')

			try:
				Memoria_Ram = driver.find_element_by_xpath('//*[@id="hardware"]/div/div[3]/div[2]/dl/dd').text #Kimovil
				Memoria_Ram = Memoria_Ram.split(" ")[0]
				if (float(Memoria_Ram) > 100): #Comparando como float
					nova_Memoria_Ram = ('0' + '.' + Memoria_Ram) # Adicionando o "0." para transformar de MB para GB
				else:
					nova_Memoria_Ram = Memoria_Ram

				celular.setRam(nova_Memoria_Ram)
			except Exception:
				celular.setRam('')

			try:
				Memoria_Armazenamento = driver.find_element_by_xpath('//*[@id="hardware"]/div/div[5]/div[2]/dl/dd[1]').text #Kimovil
				temp_Armazenamento = re.findall(r'\d+', Memoria_Armazenamento)

				celular.setArmazenamento(temp_Armazenamento[0])
			except Exception:                            
				celular.setArmazenamento('')

			try:                            
				Bluetooth = driver.find_element_by_xpath('//*[@id="connectivity"]/div/div[5]/div[2]/dl/dd[1]').text #Kimovil
				temp_Bluetooth = re.findall(r'(\d+\.\d+)', Bluetooth)

				celular.setBluetooth(temp_Bluetooth[0])
			except Exception:
				celular.setBluetooth('')

			try:
				# função para encontrar nfc
				NFC = driver.find_element_by_xpath('//*[@id="connectivity"]/div/div[9]/div[2]/dl/dt[4]').text #Kimovil        

				if (NFC == 'NFC'):
					celular.setNfc('SIM')
				else:
					celular.setNfc('NAO')
			except Exception:
				celular.setNfc('')

			try:
				Dual_chip = driver.find_element_by_xpath('//*[@id="connectivity"]/div/div[3]/div[2]/dl/dd').text #Kimovil

				if (Dual_chip.split(' ')[0] == 'Single'):
					celular.setDualChip('NAO')
				else:
					celular.setDualChip('SIM')
			except Exception:
				celular.setDualChip('')

			try:
				Lte = driver.find_element_by_xpath('//*[@id="connectivity"]/div/div[2]/div[2]/dl/dt[1]/a').text #Kimovil        

				if (Lte.split(' ')[0] == '4G'):
					celular.setLte('SIM')
				else:
					celular.setLte('NAO')

			except Exception:
				celular.setLte('')

			try:
				Resoluçao_camera = driver.find_element_by_xpath('//*[@id="camera"]/div/div[1]/div[2]/dl/dd[1]').text #Kimovil

				celular.setResolucaoCam(Resoluçao_camera.split(" ")[0])
			except Exception:
				celular.setResolucaoCam('')

			try:
				Peso = driver.find_element_by_xpath('//*[@id="design"]/div/div[1]/div[2]/dl/dd[3]').text #Kimovil

				celular.setPeso(Peso.split(' ')[0])
			except Exception:
				celular.setPeso('')

			try:
				Dimensao = driver.find_element_by_xpath('//*[@id="design"]/div/div[1]/div[2]/dl/dd[1]').text #Kimovil
				numero = re.findall(r'\d+.\d+', Dimensao)

				celular.setDimensoes('{0}x{1}x{2}'.format(numero[0],numero[1],numero[2]))
			except Exception:
				celular.setDimensoes('')

			try:
				Tamanho_tela = driver.find_element_by_xpath('//*[@id="design"]/div/div[2]/div[2]/dl/dd[1]').text #Kimovil

				celular.setTela(Tamanho_tela.split('"')[0])
			except Exception:
				celular.setTela('')

			try:
				SO = driver.find_element_by_xpath('//*[@id="software"]/div/div[1]/div[2]/dl/dd').text #Kimovil

				celular.setSo(SO.split(' ')[0])
			except Exception:
				celular.setSo('')

			try:
				#Versao_SO = driver.find_element_by_xpath('//*[@id="software"]/div/div[1]/div[2]/dl/dd/p/small').text #Kimovil
				Versao_SO = driver.find_element_by_xpath('//*[@id="software"]/div/div[1]/div[2]/dl/dd').text #Kimovil
					
				celular.setVersaoSo(Versao_SO.split(' ')[1])
			except Exception:
				celular.setVersaoSo('')

			try:
				Processamento = driver.find_element_by_xpath('//*[@id="hardware"]/div/div[1]/div[2]/dl/dd[4]').text #Kimovil

				celular.setProcessamento(Processamento.split(" ")[0])
			except Exception:
				celular.setProcessamento('')

			try:
				celular.setFonte(link) #Geral
			except Exception:
				celular.setFonte('')

			try:
				Data_atualizacao = time.strftime('%m/%Y') #Geral

				celular.setData(Data_atualizacao)
			except Exception:
				celular.setData('')

			try:
				Ano_lancamento = driver.find_element_by_xpath('//*[@id="about"]/div/div[2]/div[2]/dl/dd[1]').text #Kimovil
						
				celular.setDataLancamento(padraoData(Ano_lancamento.split(',')[0]))
			except Exception:
				celular.setDataLancamento('')

			try:
				Avaliacao_site = driver.find_element_by_xpath('//*[@id="basics"]/div/div[2]/div[6]/div[1]/div/div[1]/div/div[2]/span').text #Kimovil

				if (Avaliacao_site == 'Não preço,\nnão Ki'):
					celular.setAvaliacaoSite('')

				celular.setAvaliacaoSite(Avaliacao_site)
			except Exception:
				celular.setAvaliacaoSite('')

			try:        
				Avaliacao_Usuario = driver.find_element_by_xpath('//*[@id="basics"]/div/div[2]/div[6]/div[1]/a/div[1]/div/div[2]/span').text #Kimovil

				celular.setAvaliacaoUsu(Avaliacao_Usuario)
			except Exception:
				celular.setAvaliacaoUsu('')

			return celular

		def padraoData(data):
			mes = data.split(' ')
			if (mes[0] == 'Janeiro'):
				data = '01' + '/' + mes[1]
				return data
			if (mes[0] == 'Fevereiro'):
				data = '02' + '/' + mes[1]
				return data
			if (mes[0] == 'Março'):
				data = '03' + '/' + mes[1]
				return data
			if (mes[0] == 'Abril'):
				data = '04' + '/' + mes[1]
				return data
			if (mes[0] == 'Maio'):
				data = '05' + '/' + mes[1]
				return data
			if (mes[0] == 'Junho'):
				data = '06' + '/' + mes[1]
				return data
			if (mes[0] == 'Julho'):
				data = '07' + '/' + mes[1]
				return data
			if (mes[0] == 'Agosto'):
				data = '08' + '/' + mes[1]
				return data
			if (mes[0] == 'Setembro'):
				data = '09' + '/' + mes[1]
				return data
			if (mes[0] == 'Outubro'):
				data = '10' + '/' + mes[1]
				return data
			if (mes[0] == 'Novembro'):
				data = '11' + '/' + mes[1]
				return data
			if (mes[0] == 'Dezembro'):
				data = '12' + '/' + mes[1]
				return data
			return data

		# Fim das funções!

		pesquisa = driver.find_element_by_xpath('//*[@id="js_global-search-input"]')
		pesquisa.send_keys(self.aparelho)
		pesquisa.send_keys(Keys.ENTER)

		escolhe(self.aparelho, driver, celular, link)

		preço = Zoom.zoom(self.aparelho)

		celular.setPreco(preço.preçoZoom())

		driver.close()

		return celular