from sys import stdout as s
x,i,D=ord('!'),0,''' T( S+ R, Q. Q.%$ Q-", Q: R: C)): A++7 >.,6 >.+5 89%(#+ 4G 1I /M .O -Q ,R +T +U *.$0$4 *+$%#*#%#2 *+")"'#)"1 +)"*"'"*#0 +)"+"&"+"0 +)"+"&"+"0 )+"+"&"+"2 (,"*"'"+"4 '.")"(#(#5 &1',(7 %` %` %` %` &^ '\ ([ )Y *V -Q 1H '''
while i<len(D):
 if D[i]==' ':s.write('\n');i+=1
 else:o,l=ord(D[i])-x,ord(D[i+1])-x;s.write('{}{}'.format(' '*o,'*'*l));i+=2
