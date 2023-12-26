import playsound
import speech_recognition as sr 
from gtts import gTTS
import random

def konus(yazi):
    tts=gTTS(text=yazi,lang="tr")
    dosya_ismi="ses"+str(random.randint(0,10000000000000))+".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)
def sesi_kaydet():
    r=sr.Recognizer()  
    
    with sr.Microphone() as kaynak:
        ses=r.listen(kaynak)
        soylenen_degisken=""
        try:
            soylenen_degisken=r.recognize_google(ses,language="Tr-tr")
            print(soylenen_degisken)
            
        
        except Exception:
            konus("soylediğin çümleyi anlamadım")
    return soylenen_degisken
while True:
    yazi=sesi_kaydet()
    if "nasılsın" in yazi:
        konus("iyim sen nasilsin")         
    