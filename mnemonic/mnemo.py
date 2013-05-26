#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
mayor.py
Codifica una palabra a su equivalente numérico siguiendo una adaptación al español del sistema mnemotécnico "mayor"
http://en.wikipedia.org/wiki/Mnemonic_major_system
Escrito por René Romero Benavides - @icodeiexist - GNU Public Licence

Reglas fonéticas:
1. t,d
2. n,ñ
3. m
4. q,k,ca,co,cu,c[consonante]
5. l,ll
6. s,z,ce,ci
7. j,f,ge,gi
8. ch,ga,go,gu,sh
9. v,p,b
0. r

Uso:
python mayor.py word1 word2 wordN

Ejemplos:
python mayor.py "arrollo" "escarlatina" "canalla" "electricidad"
05
640512
425
5410611

Code references:
http://docs.python.org/2/howto/sorting.html
http://docs.python.org/2/howto/regex.html
http://docs.python.org/2/library/re.html#match-objects
http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
http://www.tutorialspoint.com/python/string_replace.htm
http://stackoverflow.com/questions/419163/what-does-if-name-main-do
http://stackoverflow.com/questions/4574509/python-remove-duplicate-chars-using-regex
"""
import re,sys

class major:
   codes = [('r'),('t','d'),('n','ñ'),('m',),('c[bcdfgjklmnpqrstvwxyz]','ca','co','cu','k','q'),('l','y'),('s','z','ce','ci'),('j','f','ge','gi'),('ch','ga','go','gu','sh'),('p','v','b')]
   def encode(self,word):
      word = re.sub(r'([a-z])\1+', r'\1', word) #remove dupplicate continous letters
      matches = []
      for idx,code in enumerate(self.codes):
         for pattern in code:
            itera = re.finditer(pattern,word)
            if itera:
               for match in itera:
                   matches.append((match.start(),idx))
      matches_sorted = sorted(matches, key=lambda pos: pos[0])
      num_string = ""
      for start,idx in matches_sorted:
          num_string += str(idx)
      return num_string # ll and rr should account for l and r respectively

if __name__ == "__main__":
   m = major()
   for word in sys.argv[1:]:
      print m.encode(word)
