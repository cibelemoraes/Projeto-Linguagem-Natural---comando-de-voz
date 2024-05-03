print("testando...")

import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilitar o microfone do usuario
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguam coisa: ")
        
        #Armazena o que foi dito nuam variavel
        audio = microfone.listen(source)
        
    try:
        
        #passa a variavel para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
            
        elif "Execel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start Powerpoint.exe")
            return False
        
        elif "Edge" in frase:
             os.system("start msedge.exe")
            return False
        
        elif "Fechar" in frase:
             os.system("exit")
            return True
        
        #retorna a frase pronunciada
        
        print("Você disse :  " + frase)
        
    #Se não reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

while True:
    if ouvir_microfone():
        break
        
        