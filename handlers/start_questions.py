import logging
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.kbs import get_start_kb
from keyboards.kbs import get_again_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f'Добро пожаловать, {message.from_user.first_name}, в "Реклама оффлайн"\n'
        f"Я бот, составляющий заявку на обслуживание\n"
        f"/cancel - для отмены введённых данных\n"
        f"/start - начать заново",
        parse_mode=None,
        reply_markup=get_start_kb()
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Отмена",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(F.text.lower() == "завершить")
async def end_chat(message: types.Message):
    await message.answer(
        "До свидания!",
        parse_mode=None,
        reply_markup=get_again_kb()
    )


@router.message(F.text.lower() == "начать заново")
async def complete(message: types.Message):
    await message.answer(
        "Нажми /start",
        parse_mode=None,
        reply_markup=ReplyKeyboardRemove()
    )
