# L1,L2,R1,R2 isminde 4 motor var. Bunlar arka arkaya çok defa ateşlenecek.
# Ancak aynı harf arka arkaya ateşlenmemeli.
#
'''
onceki = ''

def atesle(simdiki):
    global onceki
    if((onceki.startswith('L') or onceki=='') and simdiki.startswith('R')):
        print(simdiki,"ateşlendi.")
        onceki=simdiki
    elif((onceki.startswith('R') or onceki=='') and simdiki.startswith('L')):
        print(simdiki,"ateşlendi.")
        onceki=simdiki
    else:
        print(simdiki,"ateşlenemedi !!!")


atesle('L1')
atesle('L2')
atesle('R1')
atesle('R1')
atesle('L2')
'''

lst = [['L2', 1], ['R2', 3], ['R1', 4], ['L1', 0]]

import operator
lst = sorted(lst, key=operator.itemgetter(1))
print(lst)