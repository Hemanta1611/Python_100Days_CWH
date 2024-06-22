# import the required module from text to speech conversion 
import win32com.client as wc
  
# Calling the Dispatch method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = wc.Dispatch("SAPI.SpVoice") 
  
# while 1: 
#     print("Enter the word you want to speak it out by computer") 
#     s = input() 
#     speaker.Speak(s) 

# list = ["Hemanta", "Love", "a", "Beutiful", "Girl", "&", 'Guess', "her", "Name"]
# list = ["Hemanta", "Madhuri", "Manju", "Prabhat"]
# say = "Shout out to"
# for element in list:

#     speaker.Speak(say + element)

while 1:
    x = "My name is Saurabh Kumar prakash jha , i am a lawyer and gandu.. my hobby is masterbation and watching hantai."
    speaker.Speak(x)