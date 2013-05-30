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

requires the hyphen module
$ pip install pyhyphen

"""
import re,sys
from hyphen import Hyphenator
from hyphen.dictools import *

if not is_installed('es_MX'): install('es_MX')

class major:
    patterns = [('^r',),('^t','^d'),('^n','^ñ'),('^m',),('^c[^aeiouh]','^ca','^co','^cu','^k','^q'),('^l','^y'),('^s','^z','^ce','^ci'),('^j','^f','^ge','^gi'),('^ch','^ga','^go','^gu','^sh','^g[^aeiou]'),('^p','^v','^b')]
    def encode(self,word):
        num_string = ""
        h_mx = Hyphenator('es_MX')
        for syllable in h_mx.syllables(unicode(word)):
            for idx,pattern in enumerate(self.patterns):
                for regex in pattern:
                    if re.match(regex,syllable):
                        num_string += str(idx)
        return num_string 

if __name__ == "__main__":
    m = major()
    for word in sys.argv[1:]:
        print m.encode(word)
