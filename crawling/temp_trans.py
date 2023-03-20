#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def trans(txt, lang):
    translator = Translator()
    translator.raise_Exception = True
    fulltrans = ''
    trans_t=''
    a=[]
    split_txt = txt
    tmp = 0
    while True:
        tleng = len(txt)
        if tleng > 5000:
            tmp = 0
            while tmp <tleng:
                cur = txt.find('.',tmp,tmp+5000)
                a.append(txt[tmp:cur])
                if tmp+5000 > tleng:
                    cur= tleng+1
                    a.append(txt[tmp:cur])
                    break
                else:
                    tmp = cur+1
            #a = [t[i:i + 5000] for i in range(0, tleng, 5000)]
            for j in a:
                trans_t += translator.translate(j, src=lang, dest='ko').text
        else:
            trans_t += translator.translate(txt, src=lang, dest='ko').text
            break

        fulltrans+=trans_t
    return fulltrans