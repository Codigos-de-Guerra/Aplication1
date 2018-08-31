#!/usr/bin/env python3

#import pandas as pd
#data_eleicao = pd.read_csv("eleicao.csv", sep=';')
#pd.DataFrame(data_eleicao.head())
#print('\n')
#pd.DataFrame(data_eleicao.tail())

#data_eleicao['Partido/Coligação']

total_cadeiras = 29
QE = 12684

Votos_per_Coligacao = dict()
with open("eleicao.csv", encoding="utf-8") as f:
	f.readline()
	for line in f:
		#print(line)
		data = line.split(';')
		partido = data[2]
		if partido in Votos_per_Coligacao:
			Votos_per_Coligacao[partido] += int(data[3])
		else:
			Votos_per_Coligacao[partido] = int(data[3])

print(Votos_per_Coligacao, '\n')
QE = sum(Votos_per_Coligacao.values())//total_cadeiras

Vagas_per_Coligacao = dict()
for key in Votos_per_Coligacao.keys():
	QP = Votos_per_Coligacao[key]//QE
	if QP > 0:
		Vagas_per_Coligacao[key] = QP


print(Vagas_per_Coligacao)

vagas_residuais = total_cadeiras - sum(Vagas_per_Coligacao.values()) 
Medias_Residuais = dict()
while(vagas_residuais > 0):
	for key in Vagas_per_Coligacao.keys():
		Media_Partido_Atual = Votos_per_Coligacao[key]/(Vagas_per_Coligacao[key]+1)

		Medias_Residuais[key] = Media_Partido_Atual

	Maior_Media = max(Medias_Residuais, key=Medias_Residuais.get)
	Vagas_per_Coligacao[Maior_Media] += 1


