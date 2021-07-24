# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 06:37:06 2020

@author: Matheus
"""
import os
from googletrans import Translator
translator = Translator()
try:
 with open('script.rpy', 'r',encoding= "utf-8") as input_file, open('tempscript.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '    # e ' in line:
      output_file.write(line)
      translations = translator.translate(line.strip( '# e' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line) 
          
 with open('tempscript.rpy', 'r',encoding= "utf-8") as input_file, open('scripttl.rpy', 'w',encoding= "utf-8") as output_file:              
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
             output_file.write(line)

except IOError:
 next
try:     
 with open('common.rpy', 'r',encoding= "utf-8") as input_file, open('commontl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)

except IOError:
 next
 
try:           
 with open('gui.rpy', 'r',encoding= "utf-8") as input_file, open('guitl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)   
except IOError:
 next

try:        
 with open('style.rpy', 'r',encoding= "utf-8") as input_file, open('styletl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:        
 with open('screens.rpy', 'r',encoding= "utf-8") as input_file, open('screenstl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:           
 with open('options.rpy', 'r',encoding= "utf-8") as input_file, open('optionstl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:            
 with open('launcher.rpy', 'r',encoding= "utf-8") as input_file, open('launchertl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:            
 with open('obsolete.rpy', 'r',encoding= "utf-8") as input_file, open('obsoletetl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:
 with open('error.rpy', 'r',encoding= "utf-8") as input_file, open('errortl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

try:            
 with open('developer.rpy', 'r',encoding= "utf-8") as input_file, open('developertl.rpy', 'w',encoding= "utf-8") as output_file:
    for line in input_file:
     if '# e' in line:
      output_file.write(line) 
      translations = translator.translate(line.strip( ' # e ' ),dest='pt')
      next(input_file)
      output_file.write('    e ' + translations.text + "\n")
     else:
          output_file.write(line)   
     for line in input_file:
        if 'old' in line:
         output_file.write(line) 
         translations = translator.translate(line.strip( ' old' ),dest='pt')
         
         next(input_file)
         output_file.write('    new ' + translations.text + "\n")      
        else:
            output_file.write(line)
except IOError:
 next

 os.remove('tempscript.rpy')
 
