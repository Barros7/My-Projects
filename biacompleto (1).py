# -*- coding: utf-8 -*-
"""biaCompleto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TnfvTfObII5qaJ2scIQ3cmIzxw34NWkf
"""

#Desenvolvido por BIA, 30/05/2021
!pip3 install biopython #instalação da biblioteca Biopython no colab

from Bio.Blast import NCBIWWW #Importando o modolo NCBIWWW, este modulo serve para
from Bio.Blast import NCBIXML #Importando o modolo NCBIXML, este modulo serve para analise de ficheiros XML
from Bio import SeqIO #Importando o modolo SeqIO da biblioteca Bio
#Modolo SeqIO é um modolo utilizado para leitura e gravação de ficheiro em diversos formatos

ficheiro = SeqIO.read("exemplo.fasta", format="fasta")

print("Iniciando a busca no NCBIWWW..." )

resultado = NCBIWWW.qblast("blastn", "nt", \
ficheiro.seq, format_type="XML")

print("Busca concluida. Salvando resultados..." )

saida = open("blast_resultado.xml", "w")
saida.write(resultado.read())
saida.close() 

# Ler ficheiro XML
ficheiro_xml = open("blast_resultado.xml","r")
dados = NCBIXML.parse(ficheiro_xml)
item = next(dados)

i = 1

for a in item.alignments:
	for hsp in a.hsps:
		print('Alinhamento',i)
		print('Sequencia: '+a.title)
		print('Tamanho: ',a.length)
		print('Score: ',hsp.score)
		print('Gaps: ',hsp.gaps)
		print(hsp.query )
		print(hsp.match)
		print(hsp.sbjct)
		print("\n")
		i+=1

print("Executado com sucesso." )