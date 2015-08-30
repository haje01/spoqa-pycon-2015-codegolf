from __future__ import print_function

D = ''' T( S+ R, Q. Q.%$ Q-", Q: R: C)): A++7 >.,6 >.+5 89%(#+ 4G 1I /M .O -Q ,R +T +U *.$0$4 *+$%#*#%#2 *+")"'#)"1 +)"*"'"*#0 +)"+"&"+"0 +)"+"&"+"0 )+"+"&"+"2 (,"*"'"+"4 '.")"(#(#5 &1',(7 %` %` %` %` &^ '\ ([ )Y *V -Q 1H '''


def draw_pupu():
    i = 0
    e = ord('!')
    while i < len(D):
        if D[i] == ' ':
            print('')
            i += 1
        else:
            o, l = ord(D[i]) - e, ord(D[i+1]) - e
            print('{}{}'.format(' ' * o, '*' * l), end='')
            i += 2

if __name__ == '__main__':
    draw_pupu()
