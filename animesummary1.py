import wikipedia
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
try:
    while True:
        a=input("tell the name of anime you want summary of")
        b= f"{a},'anime'"
        summ=wikipedia.summary(b,sentences=4)
        print(summ)
        speak.Speak(summ)
        check=input("press n to konw about another anime ")
        if check=='n':
            continue
        print('have a good day')
        break
except:
    print("you might have entered wrong name")


