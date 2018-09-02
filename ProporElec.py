#!/usr/bin/env python3

total_cadeiras = 29
QE = 12684

data = []
Votos_per_Coligacao = dict()
with open("eleicao.csv", encoding="utf-8") as f:
	f.readline()
	for idx,line in enumerate(f):
		data.append(line.split(';'))
		partido = data[idx][2]
		if partido in Votos_per_Coligacao:
			Votos_per_Coligacao[partido] += int(data[idx][3])
		else:
			Votos_per_Coligacao[partido] = int(data[idx][3])

print(Votos_per_Coligacao, '\n')
#QE = sum(Votos_per_Coligacao.values())//total_cadeiras

Vagas_per_Coligacao = dict()
for key in Votos_per_Coligacao.keys():
	QP = Votos_per_Coligacao[key]//QE
	if QP > 0:
		Vagas_per_Coligacao[key] = QP


vagas_residuais = total_cadeiras - sum(Vagas_per_Coligacao.values()) 
Medias_Residuais = dict()
while(vagas_residuais > 0):
	for key in Vagas_per_Coligacao.keys():
		Media_Partido_Atual = Votos_per_Coligacao[key]/(Vagas_per_Coligacao[key]+1)

		Medias_Residuais[key] = Media_Partido_Atual

	Maior_Media = max(Medias_Residuais, key=Medias_Residuais.get)
	Vagas_per_Coligacao[Maior_Media] += 1
	vagas_residuais -= 1

print(Vagas_per_Coligacao)

#print(data, '\n\n\n')
data = sorted(data, key = lambda x: int(x[3]), reverse=True)
#print(data)

for idx, party in enumerate(data):
	if party[2] in Vagas_per_Coligacao and Vagas_per_Coligacao[party[2]] > 0:
		Vagas_per_Coligacao[party[2]] -= 1
	else:
		del data[idx]
print('\n\n')

out_file = open("guerra_eleicao.txt", "w")
for i in range(0,29):
	out_file.write('\t'.join(data[i]))
#data = [party if Vagas_per_Coligacao[party[2]] > 0 for party in sorted(data, key=lambda x: int(x[3]), reverse=True)]
