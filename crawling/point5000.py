#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def trans(txt):
    translator = Translator()
    fulltrans = ''
    trans_t=''
    a = []
    for t in txt:
        tleng = len(t)
        if tleng > 5000:
            tmp = 0
            while tmp <tleng:
                a.append(t[tmp:t.rfind('.',tmp,tmp+5000)])
                if tmp+5000 > tleng:
                    tmp= tleng
                    a.append(t[tmp:t.rfind('.',tmp,tmp+5000)])
                    break
                else:
                    tmp = t.rfind('.',tmp,tmp+5000)+1
            #a = [t[i:i + 5000] for i in range(0, tleng, 5000)]
            for j in a:
                trans_t += translator.translate(j, src='ru', dest='ko').text
        else:
            #trans_t += translator.translate(t,src='ru', dest='ko').text
            trans_t += translator.translate(t, dest='ko', src='ru').text
        
        #transtext.append(trans_t)
        #print(trans_t)
        fulltrans+=trans_t
    return fulltrans
