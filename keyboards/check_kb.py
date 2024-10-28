from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_check_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да, верно")
    kb.button(text="Нет, неверно")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
