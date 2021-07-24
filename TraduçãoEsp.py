# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:56:28 2020

@author: Matheus
"""
import os

from googletrans import Translator
translator = Translator()

nomearq= input("entre o nome do arquivo a ser traduzido(com sua extensão ex:script.rpy):")

try:
 with open(nomearq, 'r',encoding= "utf-8") as input_file, open('temp'+nomearq, 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '    #' in line:
      output_file.write(line)
      translations = translator.translate(line.strip( '    #' ),dest='pt')
      next(input_file)
      output_file.write('    ' + translations.text + "\n")
     else:
          output_file.write(line) 
          
 with open('temp'+nomearq, 'r',encoding= "utf-8") as input_file, open('tl'+nomearq, 'w',encoding= "utf-8") as output_file:              
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( '    old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
             output_file.write(line)

except IOError:
 next

os.remove('temp'+nomearq)



 
 


 





