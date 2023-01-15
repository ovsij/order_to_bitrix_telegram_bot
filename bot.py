from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

import logging
import os
from dotenv import load_dotenv

import keyboards as kb
from database import Database

load_dotenv()

TOKEN = os.getenv("TOKEN")

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    username = State()


# запуск бота
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    text, reply_markup = kb.inline_kb_menu()
    await bot.send_message(message.from_user.id,
				text=text,
				reply_markup=reply_markup,
				parse_mode=ParseMode.MARKDOWN)

# назад в главное меню 
@dp.callback_query_handler(lambda c: c.data == 'btn_backmenu')
async def btn_backmenu(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_menu()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# условия оплаты
@dp.callback_query_handler(lambda c: c.data == 'btn_terms')
async def btn_terms(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_terms()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# сроки поставки
@dp.callback_query_handler(lambda c: c.data == 'btn_deliverytime')
async def btn_deliverytime(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_deliverytime()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# связаться с менеджером
@dp.callback_query_handler(lambda c: c.data == 'btn_manager')
async def btn_manager(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_manager()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# личный кабинет
@dp.callback_query_handler(lambda c: c.data == 'btn_lk')
async def btn_lk(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_lk()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# удалить товар
@dp.callback_query_handler(lambda c: c.data == 'btn_deleteitem')
async def btn_deleteitem(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_deleteitem()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# оформить заказ
@dp.callback_query_handler(lambda c: c.data == 'btn_order')
async def btn_order(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_order()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )

# каталог
@dp.callback_query_handler(lambda c: c.data == 'btn_catalog')
async def btn_catalog(callback_query: types.CallbackQuery):
    text, reply_markup = kb.inline_kb_catalog()
    await callback_query.message.edit_text(
        text=text, 
        reply_markup=reply_markup, 
        parse_mode=ParseMode.MARKDOWN
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
