# Импорт aiogram
from aiogram import types, Bot, executor, Dispatcher
from aiogram.types import InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup

# Импорт модулей из FightCore
from FightCore.Scripts.json import *

# Загрузка конфига
config = load_from('config.json')

# Создание диспатчера и бота
bot = Bot(token=config['token'])
dp = Dispatcher(bot)

# Стартовая команда
@dp.message_handler(commands=['start', 'start_game'])
async def game(message: types.Message):
    print(f'Пользователь {message.from_user.id} написал /start')

    markup = Markup(row_width=1)

    yes = Button('Да ✅', callback_data='fb_f_start')

    markup.insert(yes)

    await bot.send_message(message.chat.id,
                           'Вы уверены что хотите начать игру?',
                           reply_markup=markup)

@dp.callback_query_handler(text = 'fb_f_start')
async def start(callback: types.CallbackQuery):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)