import pandas as pd
import numpy as np
import math, os

ndf = pd.DataFrame()
ativos = ['PETR4', 'BOVA11', 'ITUB4', 'VALE3', 'BBAS3']

for Ativo in ativos:
	
	historico = pd.read_csv(str(Ativo + '.csv'))
	print(historico)

	log = []
	log.append(0)

	data = historico['Data']
	fechamentos = historico['Último']
	var = historico['Var%']

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
	ndf[str(Ativo + '- Var%')] = var


ndf = ndf[20:900]
print(ndf)

ndf.to_csv('NewDataFrame.csv', index = False)