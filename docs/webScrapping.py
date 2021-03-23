import requests
from bs4 import BeautifulSoup

#entrada do usuário
moeda = input('digite em qual moeda deseja converter: ')
valor = float(input('insira o valor: '))

#motor de pesquisa
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

#pesquisando o valor da moeda no google
pesquisaGoogle = 'valor atual do '+ moeda
urlPesquisaGoogle = requests.get(f'https://www.google.com/search?q={pesquisaGoogle}&oq={pesquisaGoogle}&aqs=chrome.0.69i59j0i433j46i433j46j46i433j0i433l2j46i131i433j0l2.1316j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

#pegando o html da pagina e filtrando para obter apenas o valor da moeda
soup = BeautifulSoup(urlPesquisaGoogle.content, 'html.parser')
answerGoogle = soup.find_all('span', class_='DFlfde SwHCTb')[0]
valorMoeda = float(answerGoogle['data-value'])

#convertendo o valor inserido pelo cliente e convertendo para a moeda desejada

convertido = valor*valorMoeda

#printando o resultado da conversão
print(f'A moeda {moeda} vale R${valorMoeda:.2f} {moeda} e {valor:.2f} em {moeda} vale R${convertido:.2f}!')