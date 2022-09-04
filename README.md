# Telegram bot for stable diffusion inference

# Installation

1. To install bot clone this repo:
    `git clone https://github.com/rw404/sd_telegram_bot.git`

2. Create telegram bot with BotFather, get your bot's token
3. Install python requirement packages:
    `pip[pip3] install -r requirements.txt`
4. To infer SD model, you have to agree the [huggingface rules](https://huggingface.co/CompVis/stable-diffusion-v1-4), get your id accept token and enter it after running[it can return errors and suggestions to fix it]:
    `hugginface-cli login`
5. Try model with following command:
    `python[python3] diff.py` -- It returns smth like **CUDA inference started** or **CPU inference started**, then downloads the model, then runs 50 iterations to generate the image.

# Running Bot

1. [OPTIONAL - IF BOT IN CHAT, NOT IN CHANNEL] Disable bot's privacy via BotFather:
    1. `/setprivacy`
    2. `@YOUR_BOT_NAME`
    3. `Disable`
2. [OPTIONAL - IF BOT IN CHAT, NOT IN CHANNEL] Add bot to chat with admin preferences 
3. Run python script with a bot's token as argument:
    `python[python3] bot.py YOUR_TOKEN`
4. [OPTIONAL - IF BOT IN CHAT, NOT IN CHANNEL] If you got an error, fix it:
    1. In my case, adding `'update_id'` to message keys in \_\_init.py\_\_ file with str from errors solved the problem.
5. Wait for message:
    > Ready to take photos
6. Enjoy!
