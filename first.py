from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '6600080191:AAFUBCn1GvknB7pcTQ6uViBFTU3mBxWsvzU'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_stic(message):
    await message.reply_sticker(message.sticker.file_id)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"f
async def rep_audio(message:Message):
    await message.reply_audio(message.audio.file_id)
    await message.answer("It's fine audio")
async def send_voice(message:Message):
    await message.reply_voice(message.voice.file_id)
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(send_voice, F.voice)
dp.message.register(send_stic, F.sticker)
dp.message.register(rep_audio, F.audio)
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)





























"""

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'

BOT_TOKEN = '6600080191:AAFUBCn1GvknB7pcTQ6uViBFTU3mBxWsvzU'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

timeout = 0
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True: 
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            chat_mes = result['message']['text']
            if chat_mes == "/help":
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Пришли мне любое предложение?')
            elif chat_mes == "/start":
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Я готов начать работу')
            else:requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={chat_mes}')
            print(chat_mes)
            timeout = 50
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

"""


"""Code to reply photos
while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            chat_mes = result['message']['text']
            cat_response = requests.get(API_CATS_URL)
            dog_response = requests.get(API_DOGS_URL)
            if dog_response.status_code == 200:
                dog_link = dog_response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=okay?')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=wtf?')

            
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                if chat_mes == '1':
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Гандон, ты как цифру угадал?')
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Не угадал, держи фотки котов теперь:')
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Бля хз че не так поидее')

    time.sleep(1)
    counter += 1"""
