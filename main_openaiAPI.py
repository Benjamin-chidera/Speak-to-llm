import speech_recognition as sr
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

from dotenv import load_dotenv

load_dotenv()


def listen_for_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Start speaking...")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)  # type: ignore
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"⚠️ Could not request results; {e}")
            return ""


def chat_with_bot(text):
    # llm = ChatOllama(model="llama3.1")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    message = [
        ("system", "You are a conversational AI who chats with users and answers questions."),
        ("human", "{text}")
    ]
    
    chat = ChatPromptTemplate.from_messages(message)
    chain = chat | llm | StrOutputParser()
    
    res = chain.invoke({"text": text})
    print("Bot:", res)
    return res


def speak(text):
    if not text.strip():
        return
    
    # Generate TTS audio into memory
    tts = gTTS(text=text, lang='en', slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # rewind
    
    # Load and play audio directly from memory
    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    play(audio)


if __name__ == "__main__":
    while True:
        text = listen_for_speech()
        if text.lower() in ["exit", "quit", "stop"]:
            break
        response = chat_with_bot(text)
        speak(response)
