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

    if commands.split()[0][:8] == '/imagine':
        command = commands.split()[0]

        fromname = msg['from']['username']
        fromid = msg['from']['id']
        prompt = ' '.join(commands.split()[1:])
        
        seed = None
        if len(command) > 8:
            seed = int(command[8:])

        print(f'Got command: {command}, prompt: {prompt}, seed: {seed}')

        image, seed = diff.inference(pipe, device, seed=seed, prompt=prompt)
        image.save(f'tmp/test_{fromid}.png')

        bot.sendPhoto(chat_id, photo=open(f"tmp/test_{fromid}.png", 'rb'),
                      caption=f'@{fromname}\n\n*PROMPT*: `{prompt}`\n\n*SEED*={seed}',
                      parse_mode="Markdown")

if __name__ == '__main__':
    print('lol')
    api = sys.argv[1]
    bot = telepot.Bot(api)
    print('Ready to take photos')
    bot.message_loop(handle)

    while 1:
        time.sleep(10)
