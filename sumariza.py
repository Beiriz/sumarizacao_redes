#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
GRCN is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
#
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
#
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''
#pip install netaddr

import os
import sys
from netaddr import *

__author__ = 'Beiriz'
__version__= 1.000
__datebegin__= "16/06/2020"

#-----------------------------------------------------------------------

lista_redes_origem = []
caminho_arquivo_origem = ""
arquivo_origem = None
qt_redes_origem = 0
qt_redes_destino = 0
#-----------------------------------------------------------------------

os.system('cls' if os.name == 'nt' else 'clear')
titulo = "Sumarizador de Rotas - Converte uma arquivo de rotas em blocos maiores - %s - v%s - %s" % (__author__, __version__,__datebegin__)
print("#"*100)
print(" %s" %(titulo))
print("#"*100)

#------------------------------------------------- Parâmetros informados / manual:

try:
  caminho_arquivo_origem = str(sys.argv[1])
except:
  print("\nErro! Informe os parâmetros para este script!")
  print("\n")
  print("Exemplo:")
  print("python %s <CAMINHO_ARQUIVO_TXT_COM_ROTAS_A_SUMARIZAR>" %(sys.argv[0]))
  print(" - No arquivo, informe uma rota por linha. Exemplo: 192.168.0.0/24")
  print("\n")
  exit(0)

print("\n%s"%('-'*60))
print("Lendo redes informadas no arquivo '%s':" % (caminho_arquivo_origem))
print("%s\n"%('-'*60))

try:
  arquivo_origem = open(caminho_arquivo_origem, "r")
except:
  print("\nErro! O arquivo informado não pode ser aberto para leitura.")
  exit(0)
arquivo_origem.close()

try:
  with open(caminho_arquivo_origem) as arquivo_origem:
    for rede_origem in arquivo_origem:
      rede_origem = rede_origem.strip()
      rede_origem = rede_origem.replace(" ", "")
      print(" - Lendo rede %s" % (rede_origem))
      lista_redes_origem.append(IPNetwork(rede_origem))
except:
  print("\nErro! Uma ou mais redes informadas não está na formatação correta. Confira o arquivo.\n")
  exit(0)

qt_redes_origem = len(lista_redes_origem)

lista_redes_destino = cidr_merge(lista_redes_origem)
qt_redes_destino = len(lista_redes_destino)

print("\n%s"%('-'*60))
print("As %i redes informadas foram sumarizadas em %i redes:" % (qt_redes_origem, qt_redes_destino))
print("%s\n"%('-'*60))

for rede_destino in lista_redes_destino:
  print("%s" % (rede_destino))
#fecha o arquivo_origem
arquivo_origem.close()

print("\n%s"%('-'*60))
print("FIM")
print("%s\n"%('-'*60))
