import pandas as pd
import numpy as np
import math, os

ndf = pd.read_csv('NewDataFrame.csv')
#print(ndf)

ativos = ['PETR4', 'BOVA11', 'ITUB4', 'VALE3', 'BBAS3']

retornos = pd.DataFrame()
retornos['Data'] = ndf['Data']

prev = []

for Ativo in ativos:

	state = []
	state.append(0)

	var = ndf[str(Ativo + '- Var%')]

	for i in range(1, len(ndf)):

		if ndf[str(Ativo + '- Log')][i-1] >= ndf[str(Ativo + '- Superior')][i-1]:
			state.append(-1)

		elif ndf[str(Ativo + '- Log')][i-1] <= ndf[str(Ativo + '- Inferior')][i-1]:
			state.append(1)

		else:
			state.append(0)


	state = np.array(state)
	retornos[str(Ativo + '- State')] = state
	retornos[str(Ativo + '- Var%')] = var
	last = str(state[-1])

	prev.append(str(Ativo + ': ' + last))


print(retornos.tail)

retornos.to_csv('Retornos.csv', index = False)


print('=============================== Previstos =============================== ')

ops = 0
for p in prev:
	
	if p[-1] != '0':
		print(p)
		ops += 1
	else:
		continue

if ops == 0:
	print('Nenhuma operação detectada.') 