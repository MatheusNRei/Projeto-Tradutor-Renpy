# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:17:04 2020

@author: Matheus
"""

nomearq= input("entre o nome do arquivo a ser traduzido(com sua extensão ex:script.rpy):")
with open(nomearq, 'r',encoding= "utf-8") as input_file, open('asp'+nomearq, 'w',encoding= "utf-8") as output_file:
    for line in input_file:
      if '"'and '"' and'"' and '"' in line:
       output_file.write(line.rstrip( '"' ))
      else:
       output_file.write(line)   
      