import sys
import time
import datetime
import telepot
import diff
import io

pipe, device = diff.load_model()

def handle(msg):
    print(msg)
    chat_id = msg['chat']['id']
    commands = msg['text']
    
    command = commands.split()[0]

    fromid = commands.split()[1]
    prompt = ' '.join(commands.split()[2:])

    print(f'Got command: {command}, prompt: {prompt}')


    if command == '/imagine':
        image = diff.inference(pipe, device, prompt)
        image.save('tmp/test.png')

        bot.sendPhoto(chat_id, photo=open("tmp/test.png", 'rb'), caption=fromid)

if __name__ == '__main__':
    print('lol')
    api = sys.argv[1]
    bot = telepot.Bot(api)
    print('Ready to take photos')
    bot.message_loop(handle)

    while 1:
        time.sleep(10)
