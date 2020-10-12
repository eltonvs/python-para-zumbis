#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Seja o statement sobre diversidade:
“The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are,
and whatever your background, we welcome you.”.
Gere uma lista de palavras deste texto com split(),
a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”.
Imprima a lista resultante.
Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''

from re import sub

text = '''
The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are,
and whatever your background, we welcome you.
'''
text = sub('[!@#$,.]', '', text)
words = text.split()
letters = 'python'
l = list(x for x in words if x[0].lower() in letters or x[-1].lower() in letters)

print(l)
