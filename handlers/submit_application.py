from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from keyboards.kbs import get_close_kb
from keyboards.kbs import get_again_kb
from keyboards.kbs import get_check_kb

from googlesheets import db_users
import csv

import pandas as pd

import gs_gen

db_users.DbNewUser()

router = Router()


class UserData(StatesGroup):
    name = State()
    orga = State()
    location = State()
    contacts = State()
    side = State()
    finmat = State()
    period = State()


db_data = [0, 0, 0, 0, 0, 0, 0]


@router.message(F.text.lower() == "завершить")
async def no_answer(message: types.Message):
    await message.answer(
        text="До свидания!",
        parse_mode=None,
        reply_markup=get_again_kb()
    )


@router.message(F.text.lower() == "подать заявку")
async def submit_app(message: types.Message):
    await message.answer(
        text=f"Для составления заявки нужно ответить на несколько простых вопросов.\n"
             f"Вы готовы начать составление сейчас?",
        parse_mode=None,
        reply_markup=get_close_kb()
    )


@router.message(F.text.lower() == "продолжить")
async def yes_answer(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer(
        text=f"Как я могу к вам обращаться?",
        parse_mode=None,
        reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(UserData.name)
async def user_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    global name_data
    name_data = message.text
    db_data[0] = name_data
    print(db_data)
    await state.set_state(UserData.orga)
    await message.answer(
        text=f"Приятно познакомиться {message.text}.\n"
             f"Укажите название вашей организации",
        parse_mode=None
    )


@router.message(UserData.orga)
async def user_orga(message: Message, state: FSMContext):
    await state.update_data(orga=message.text)
    global orga_data
    orga_data = message.text
    db_data[1] = orga_data
    print(db_data)
    await state.set_state(UserData.location)
    await message.answer(
        text=f"Уже определились с выбором локации размещения?\n"
             f"Если да, то укажите желаемый адрес.",
        parse_mode=None
    )


@router.message(UserData.location)
async def user_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    global location_data
    location_data = message.text
    db_data[2] = location_data
    print(db_data)
    await state.set_state(UserData.side)
    await message.answer("Вам потребуется одна сторона или две?")


@router.message(UserData.side)
async def user_side(message: Message, state: FSMContext):
    await state.update_data(side=message.text)
    global side_data
    side_data = message.text
    db_data[3] = side_data
    print(db_data)
    await state.set_state(UserData.finmat)
    await message.answer("У вас есть готовый к размещению материал?")


@router.message(UserData.finmat)
async def user_finmat(message: Message, state: FSMContext):
    await state.update_data(finmat=message.text)
    global finmat_data
    finmat_data = message.text
    db_data[4] = finmat_data
    print(db_data)
    await state.set_state(UserData.period)
    await message.answer("На какой срок планируете аренду?")


@router.message(UserData.period)
async def user_period(message: Message, state: FSMContext):
    await state.update_data(period=message.text)
    global period_data
    period_data = message.text
    db_data[5] = period_data
    print(db_data)
    await state.set_state(UserData.contacts)
    await message.answer(
        text=f"Пожалуйста, оставьте контактные данные, по которым вам удобнее всего получить обратную связь.\n"
             f"Какие способы связи предпочтительнее?",
        parse_mode=None
    )


@router.message(UserData.contacts)
async def user_contacts(message: Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    global contacts_data
    contacts_data = message.text
    db_data[6] = contacts_data
    print(db_data)
    final_data = await state.get_data()
    await message.answer(
        text=f"Уже почти закончили, давайте проверим данные:\n"
             f"Имя клиента: {final_data['name']}\n"
             f"Название организации: {final_data['orga']}\n"
             f"Адрес локации: {final_data['location']}\n"
             f"Количество сторон: {final_data['side']}\n"
             f"Готовый материал: {final_data['finmat']}\n"
             f"Срок аренды: {final_data['period']}\n"
             f"Контакты: {final_data['contacts']}\n"
             f"Всё верно?",
        parse_mode=None,
        reply_markup=get_check_kb()
    ),
    await state.clear()


@router.message(F.text.lower() == "да, верно")
async def yes_check(message: types.Message):
    await message.answer(
        text=f"Ваша заявка успешно зарегестрирована в системе.\n"
             f"В ближайшее время менеджер свяжется с вами для уточнения нектороых моментов договора.\n"
             f"Хорошего вам дня!",
        parse_mode=None,
        reply_markup=get_again_kb()
    )
    db_users.DbNewUser.cur.execute('''INSERT INTO users(Имя_клиента,
        Название_организации,
        Адрес_локации,
        Количество_сторон,
        Готовый_материал,
        Срок_аренды,
        Контакты) VALUES(?,?,?,?,?,?,?)''', db_data)
    db_users.DbNewUser.conn.commit()
    # Выполнить SQL-запрос
    query = "SELECT * FROM users"
    db_users.DbNewUser.cur.execute(query)
    data = db_users.DbNewUser.cur.fetchall()
    print('Выполнить SQL-запрос')
    # Записать данные в CSV-файл
    with open('googlesheets/base.csv', 'w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in db_users.DbNewUser.cur.description])  # Write header
        writer.writerows(data)  # Write data rows
    print('Записать данные в CSV-файл')
    # Подсоединение к Google Таблицам
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]
    # credentials = ServiceAccountCredentials.from_json_keyfile_name("googlesheets/gs_credentials.json", scope)
    # client = gspread.authorize(credentials)
    # Откройте таблицу
    sheet = gs_gen.client.open("Example2").sheet1
    # Прочитайте csv с помощью pandas
    df = pd.read_csv('googlesheets/base.csv', encoding='cp1251')
    # Экспортируйте df в таблицу
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('Экспорт в ГО')


@router.message(F.text.lower() == "нет, неверно")
async def no_check(message: types.Message):
    await message.answer(
        text="Повторим заполнение?",
        parse_mode=None,
        reply_markup=get_close_kb()
    )
