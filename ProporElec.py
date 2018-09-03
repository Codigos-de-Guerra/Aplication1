#!/usr/bin/env python3

total_cadeiras = 29
QE = 12684

dataFrame_Candidates = []
Votos_per_Coligacao = dict()

# Next 2 lines represents the file with candidates
# and file with results, respectively.
inputFile = "data/eleicao.csv"
outputFile = "data/my_result.tsv"

with open(inputFile, encoding="utf-8") as f:
	f.readline()
	for idx,line in enumerate(f):
		dataFrame_Candidates.append(line.split(';'))
		partido = dataFrame_Candidates[idx][2]
		if partido.find('-') != -1:
			partido = partido[(partido.find('-')+2):]
		if partido in Votos_per_Coligacao:
			Votos_per_Coligacao[partido] += int(dataFrame_Candidates[idx][3])
		else:
			Votos_per_Coligacao[partido] = int(dataFrame_Candidates[idx][3])
print(">>> Votos para cada Coligacao:")
print(Votos_per_Coligacao, '\n')

# Uncomment next line to dynamicly work with any file.
#QE = sum(Votos_per_Coligacao.values())//total_cadeiras

Vagas_per_Coligacao = dict()
for key in Votos_per_Coligacao.keys():
	QP = Votos_per_Coligacao[key]//QE
	if QP > 0:
		Vagas_per_Coligacao[key] = QP

# My failed attempt to do past function on 1 line.
# Vagas_per_Coligacao[key] = QP if QP > 0 QP = Votos_per_Coligacao[key]//QE for key in Votos_per_Coligacao.keys()

vagas_residuais = total_cadeiras - sum(Vagas_per_Coligacao.values()) 
Medias_Residuais = dict()

while(vagas_residuais > 0):
	for key in Vagas_per_Coligacao.keys():
		Media_Partido_Atual = Votos_per_Coligacao[key]/(Vagas_per_Coligacao[key]+1)

		Medias_Residuais[key] = Media_Partido_Atual

	Maior_Media = max(Medias_Residuais, key=Medias_Residuais.get)
	Vagas_per_Coligacao[Maior_Media] += 1
	vagas_residuais -= 1

print(">>> Vagas para cada Coligacao:")
print(Vagas_per_Coligacao)

# Sorting dataFrame in function of number of votes for candidate.
dataFrame_Candidates = sorted(dataFrame_Candidates, key = lambda x: int(x[3]), reverse=True)

for idx, party in enumerate(dataFrame_Candidates):
	if party[2].find('-') != -1:
		partido = party[2][(party[2].find('-')+2):]
	else:
		partido = party[2]
	if partido in Vagas_per_Coligacao and Vagas_per_Coligacao[partido] >= 1:
		Vagas_per_Coligacao[partido] += -1
	else:
		dataFrame_Candidates[idx] = -100
dataFrame_Candidates = [x for x in dataFrame_Candidates if x != -100]

# Also failed attempt ;-;.
#dataFrame_Candidates = [party if Vagas_per_Coligacao[party[2]] > 0 for party in sorted(dataFrame_Candidates, key=lambda x: int(x[3]), reverse=True)]

out_file = open(outputFile, "w")
for i in range(0,total_cadeiras):
	out_file.write('\t'.join(dataFrame_Candidates[i]))

# :)
