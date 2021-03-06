import pandas as pd
import numpy as np
import math, os


#Acessando os dados históricos na pasta DataBase e criando a lista dos ativos // Acessing the DataBase directory and creating the stock list
lista = os.listdir('/home/jorge/Documentos/Advisor_Backtest/DataBase')
ativos = []

for l in lista:
	if l.endswith('.csv') == True:
		codigo = os.path.splitext(l)[0]
		ativos.append(codigo)

print(ativos)

#Processando os dados obtidos para cada ativo e os organizando em um novo dataframe // Processing the data of each stock and organizing them in a new dataframe
ndf = pd.DataFrame()
for Ativo in ativos:
	
	historico = pd.read_csv(str('/home/jorge/Documentos/Advisor_Backtest/DataBase/' + Ativo + '.csv'))


	log = []
	log.append(0)

	data = historico['Data']
	fechamentos = historico['Último']


	for i in range(1, len(fechamentos)):

		ln = math.log(fechamentos[i] / fechamentos[i-1])
		log.append(ln)

	log = np.array(log)

	ndf['Data'] = data
	ndf[str(Ativo + '- Fechamento')] = fechamentos
	ndf[str(Ativo + '- Log') ] = log
	ndf[str(Ativo + '- MM20')] = ndf[str(Ativo + '- Log')].rolling(window = 20).mean()
	ndf[str(Ativo + '- Desvpad')] = ndf[str(Ativo + '- Log')].rolling(window = 20).std()

	ndf[str(Ativo + '- Superior')] = ndf[str(Ativo + '- MM20')] + (ndf[str(Ativo + '- Desvpad')]) * 2
	ndf[str(Ativo + '- Inferior')] = ndf[str(Ativo + '- MM20')] - (ndf[str(Ativo + '- Desvpad')]) * 2

ndf = ndf[20:len(historico)]

#Salvando os dados processados para fins de análises futuras // Saving the processed data for future analysis
ndf.to_csv('/home/jorge/Documentos/Advisor_Backtest/DadosProcessados.csv', index = False)
ndf = pd.read_csv('DadosProcessados.csv')


#Criando um dataframe diferente para avaliar os ganhos históricos acumulados para cada ativo // Creating a different DataFrame to evaluate the historical gains for each stock
retornos = pd.DataFrame()
retornos['Data'] = ndf['Data']

prev = []

for Ativo in ativos:

	state = []
	acumulado = []
	benchmark = []
	state.append(0)
	acumulado.append(float(1000.00))
	benchmark.append(float(1000.00))



	for i in range(1, len(ndf)):

		if ndf[str(Ativo + '- Log')][i-1] >= ndf[str(Ativo + '- Superior')][i-1]:
			state.append(-1)

		elif ndf[str(Ativo + '- Log')][i-1] <= ndf[str(Ativo + '- Inferior')][i-1]:
			state.append(1)

		else:
			state.append(0)

	for a in range (1, len(ndf)):
		acumulado.append(acumulado[a-1] * (1 + (state[a] * ndf[str(Ativo + '- Log')][a])))

		benchmark.append(benchmark[a-1] * (1 + (ndf[str(Ativo + '- Log')][a])))


	retornos[str(Ativo + '- Acumulado')] = acumulado
	retornos[str(Ativo + '- Benchmark')] = benchmark

	RetornoAbs = math.log(acumulado[-1] / acumulado[0])
	BenchmarkAbs = math.log(benchmark[-1] / benchmark[0])

	last = str(state[-1])
	absoluto = round(RetornoAbs * 100)
	absoluto = str(absoluto) + '%'
	
	bench = round(BenchmarkAbs * 100)
	bench = str(bench) + '%'

	prev.append(str(Ativo + '( ' 'Acumulado: ' + absoluto + ',' + ' B&H: ' + bench + ')' + ': ' + last))	
print(retornos)

retornos.to_csv('Retornos.csv', index = False)

#Apresentando as previsões de compra e venda dentro da estratégia para o último período apresentado na base de dados // Presenting the buying and selling forecasts of the strategy for the last period on the database
#Se nenhuma operação for detectada para o período apresentará a mensagem: "Nenhuma operação detectada" // If no operations were detected will print the messege: "No operations detected"
print('=============================== Previstos =============================== ')

ops = 0
for p in prev:
	
	if p[-1] != '0':
		print(p, '\n')
		ops += 1
	else:
		continue

if ops == 0:
	print('Nenhuma operação detectada. // No operations detected') 

print('========================================================================= ')
