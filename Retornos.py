import pandas as pd
import numpy as np
import math, os

ndf = pd.read_csv('NewDataFrame.csv')
print(ndf)

ativos = ['PETR4', 'BOVA11', 'ITUB4', 'VALE3', 'BBAS3']

retornos = pd.DataFrame()
retornos['Data'] = ndf['Data']

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


print(retornos)

retornos.to_csv('Retornos.csv', index = False)

