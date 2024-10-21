import pyaudio
import wave
import speech_recognition as sr

def captura_audio():
    # Parâmetros do áudio
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    OUTPUT_FILENAME = "output.wav"

    # Inicializar PyAudio
    audio = pyaudio.PyAudio()

    # Abrir stream para gravação
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)

    #print("Gravando...")

    frames = []

    # Gravar áudio
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("Gravação finalizada")

    # Parar e fechar o stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Salvar arquivo de áudio
    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    #print(f"Áudio salvo como {OUTPUT_FILENAME}")

    # Usar SpeechRecognition para transcrever o áudio
    recognizer = sr.Recognizer()

    # Abrir o arquivo de áudio
    with sr.AudioFile(OUTPUT_FILENAME) as source:
        print("Verificando Resposta...")
        audio_data = recognizer.record(source)  # Ler o conteúdo do arquivo de áudio
        try:
            # Usar reconhecimento de voz do Google
            text = recognizer.recognize_google(audio_data, language='en-US')  # Para transcrição em português
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition não conseguiu entender o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
