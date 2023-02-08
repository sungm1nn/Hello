#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def trans(text, transtext):
    translator = Translator()
    
    for t in text:
        la = translator.detect(text).lang
        tleng = len(t)
        if tleng > 5000:
            a = [t[i:i + 5000] for i in range(0, tleng, 5000)]
            for j in a:
                trans_t += translator.translate(j, dest='ko').text
        else:
            trans_t= translator.translate(t, dest='ko').text
        
        transtext.append(trans_t)
        print(trans_t)
    print(trans_t)