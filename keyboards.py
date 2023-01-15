from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text as txt, bold
import emoji

# общие кнопки 
back_menu_btn = InlineKeyboardButton(emoji.emojize(':arrow_left: Выйти в меню :arrow_left:', language='alias'), callback_data='btn_backmenu')
back_lk_btn = InlineKeyboardButton(emoji.emojize(':arrow_left: Назад :arrow_left:', language='alias'), callback_data='btn_lk')

# меню
def inline_kb_menu():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    text_and_data = [
			['Условия оплаты', 'btn_terms'],
			['Сроки поставки', 'btn_deliverytime'],
            ['Связаться с менеджером', 'btn_manager'],
            ['Личный кабинет', 'btn_lk'],
            ['Каталог', 'btn_catalog']
			]
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    inline_kb.add(*row_btns)

    text = txt(bold('МЕНЮ'),
			'Добро пожаловать!',
            'Чтобы продолжить нажмите одну из кнопок ниже', sep='\n')
    return text, inline_kb

# условия оплаты
def inline_kb_terms():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_menu_btn)
    text = txt(bold('УСЛОВИЯ ОПЛАТЫ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# сроки поставки
def inline_kb_deliverytime():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_menu_btn)
    text = txt(bold('СРОКИ ПОСТАВКИ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# связаться с менеджером
def inline_kb_manager():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_menu_btn)
    text = txt(bold('СВЯЗАТЬСЯ С МЕНЕДЖЕРОМ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# личный кабинет
def inline_kb_lk():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    text_and_data = [
			['Удалить товар', 'btn_deleteitem'],
			['Оформить заказ', 'btn_order'],
			]
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    inline_kb.add(*row_btns)
    inline_kb.add(back_menu_btn)
    text = txt(bold('ЛИЧНЫЙ КАБИНЕТ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# удалить товар
def inline_kb_deleteitem():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_lk_btn)
    text = txt(bold('УДАЛИТЬ ТОВАР'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# оформить заказ
def inline_kb_order():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_lk_btn)
    text = txt(bold('ОФОРМИТЬ ЗАКАЗ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb

# каталог
def inline_kb_catalog():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(back_menu_btn)
    text = txt(bold('КАТАЛОГ'),
			'Данный раздел находится в разработке', sep='\n')
    return text, inline_kb