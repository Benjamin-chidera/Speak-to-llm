import speech_recognition as sr
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gtts import gTTS
import os
from playsound import playsound


def listen_for_speech():
    r = sr.Recognizer()
    
    # connect to microphone
    with sr.Microphone() as source:
        print("Start speaking...")
        
        audio = r.listen(source)
        
        try:
            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio) # type: ignore
            print("What you are saying: " + text)
            
            return text
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        
        except sr.RequestError as e:
            print(f"⚠️ Could not request results; {e}")
            return ""
        
# Here is my conversation: {text}
def chat_with_bot(text):
    llm = ChatOllama(model="llama3.1")
    message = [
        (
            "system", f"""You are a conversational AI who chats with users and answers questions.

                
            """
        ),
        (
            "human", "{text}"
        )
    ]
    
    chat = ChatPromptTemplate.from_messages(message)
    
    chain = chat | llm | StrOutputParser()
    
    res = chain.invoke({"text": text})
    
    print(res)
    
    return res

def speak(text):
    if text.strip() == "":
        return
    
    gtts = gTTS(text=text, lang='en', slow=False)
    
    file_name = "conversation.mp3"
    gtts.save(file_name)
    
    # play the audio file
    playsound(file_name)
    
    # remove the audio file
    os.remove(file_name)
    
    
    
    
if __name__ == "__main__":
    while True:
        text = listen_for_speech()
        if text in ["exit", "quit", "stop"]:
            break
        llm = chat_with_bot(text)
        speak(llm)