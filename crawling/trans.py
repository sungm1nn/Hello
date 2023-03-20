#translating articles about corresponding languages

#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def trans(txt, lang):
    translator = Translator()
    fulltrans = ''

    if len(txt) < 4000:
        return str(translator.translate(txt, src=lang, dest='ko').text)
    else:
        #t = []
        tmp = 0
        while tmp < len(txt):
            cur = txt.rfind('.',tmp,tmp+4000)
            t = txt[tmp:cur+1]
            if len(t)==0:
                break
            tmp = cur+1
            fulltrans += str(translator.translate(t, src=lang, dest='ko').text)
            #print(fulltrans)
    #fulltrans+=trans_t
    return fulltrans
