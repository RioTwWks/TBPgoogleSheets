from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_check_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да, верно")
    kb.button(text="Нет, неверно")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_close_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Продолжить")
    kb.button(text="Завершить")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_again_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Начать заново")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Подать заявку")
    kb.button(text="Завершить")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
