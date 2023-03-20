import trans

fp = open('./a.txt','r')
textt = ''
for i in fp.readlines():
    #print(i)
    textt+=str(i).strip()
    if textt[-1]!= ' ':
        textt += ' '
#textt = str(fp.readlines())
s = str(textt)
print(s)
print(trans.trans(s,'en'))
fp.close()