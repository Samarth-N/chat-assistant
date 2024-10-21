import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia




listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()
def input_instruction():
    global instruction
    
    try:
       with aa.Microphone() as origin:
           print("listening")
           speech = listener.listen(origin)
           instruction = listener.recognize_google(speech)
           instruction = instruction.lower()
           if "Jarvis" in instruction:
               instruction = instruction.replace('jarvis', '')
               print(instruction)
           
    
    
    except:
        pass
    return instruction
   

def play_Jarvis():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p' )
        talk('current time'+ time)
        
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date" + date)
        
    elif 'how are you' in instruction:
        talk('I am fine, how are you')
        
    elif 'What is your name' in instruction:
        talk('I am Jarvis, What can I do For you?')
  
    elif 'introduce my father and mother' in instruction:
        talk('my father name is natesh and my mother name is roopa')
    elif 'who is the goat of cricket' in instruction:
        talk('The king Kohli')
    elif 'who invented you' in instruction:
        talk('I was invented by samarth')
    elif 'who is' in instruction:
        human = instruction.replace('who is'," ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    elif 'why is' in instruction:
        human = instruction.replace('why is'," ")
        info = wikipedia.summary(human, 2)
        print(info)
        talk(info)
        
    else:
        talk('Please repeat')
        
play_Jarvis()
