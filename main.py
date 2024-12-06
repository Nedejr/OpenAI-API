from openai import OpenAI
from dotenv import load_dotenv
import os

# gpt-4o-mini
def criando_chat():
    response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        {'role':'system', 'content': 'Vocè é um asistente virtual debochado, irônico e engraçado'},
        {'role':'user', 'content': 'Me fale sobre a rede social TikTok?'},
   ],
    #    max_tokens = 150,
    #    temperature = 0.2,
    )
    print(response.choices[0].message.content)

# dall-e-3
def criando_imagem():
    response = client.images.generate(
        model='dall-e-3',
        prompt='Um gato nadando no mar em um dia de sol',
        size='1024x1024',
        quality='standard',
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)

# tts-1
def texto_em_audio():
    response = client.audio.speech.create(
        model='tts-1',
        voice='onyx',
        input= '''A API da OpenAI é uma ferramenta poderosa que permite criar soluções 
        inovadoras em diversas áreas. Se você está interessado em aprender mais sobre 
        a API da OpenAI e outras tecnologias de inteligência artificial, recomendamos 
        explorar a documentação oficial e os tutoriais disponíveis. '''
    )
    response.write_to_file('audio.mp3')

#whisper-1
def audio_em_texto():
    audio_file = open('audio.mp3', 'rb')
    if audio_file:
        transcription = client.audio.transcriptions.create(
            model = 'whisper-1',
            file = audio_file
        )
        print(transcription.text)
    else:
        print('Arquivo não encontrado.')

if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    client = OpenAI(api_key=API_KEY)
    audio_em_texto()
