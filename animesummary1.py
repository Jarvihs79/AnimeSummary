import wikipedia
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
wel= print("Welcome")
speak.Speak("welcome")

for i in range(10000000):
    pass
pgm=print("this program will tell you the summary of any anime you want to know")
speak.Speak("this program will tell you the summary of any anime you want to know")

for i in range(10000000):
    pass
prop=print("you should write the name properly")
speak.Speak("you should write the name properly")
for i in range(10000000):
    pass
try:
    while True:
        speak.Speak("type the name of anime you want summary of")
        a=input("type the name of anime you want summary of\n")
        print("wait foe a sec")
        #speak.Speak("type the name of anime you want summary of")
        b= f"{a},'anime'"
        summ=wikipedia.summary(b,sentences=4)
        print(summ)
        speak.Speak(summ)
        check=input("press n to konw about another anime ")
        if check=='n':
            continue
        print('have a good day \n project work by:\n shivraj and chaitanya')
        break
except:
    print("you might have entered wrong name")


