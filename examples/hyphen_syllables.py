from hyphen import Hyphenator
from hyphen.dictools import *
import sys
 
for lang in ['es_MX', 'es_SP']:
        if not is_installed(lang): install(lang)
h_mx = Hyphenator('es_MX')
for word in sys.argv[1:]:
    print h_mx.syllables(unicode(word.encode('utf-8')))
