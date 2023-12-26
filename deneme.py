import speech_recognition as sr 
from datetime import datetime
r=sr.Recognizer()

def record():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("anlayamadım")
        except sr.RequestError:
            print("sistem calismiyor")
        return voice
 
def responce(voice):
    if "nasılsın" in voice:
        print("iyi senden")
    if "saat kaç" in voice:
        print(datetime.now().strftime("%H:%M:%S"))             
    if "arama yap" in voice:
        search=record("ne aramak istiyorsunuz?")
        url="https://google.com/search?g="
        
           
print("nasil yardimci olabilirim")    
voice=record()
print(voice)                

