from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_answer_keyboard(answers):
    # Создаем кнопки с вариантами ответов
    buttons = [
        KeyboardButton(text=answers[0]),
        KeyboardButton(text=answers[1]),
        KeyboardButton(text=answers[2]),
        KeyboardButton(text=answers[3]),
    ]

    # Создаем клавиатуру с двумя строками, на каждой по две кнопки
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    # Добавляем кнопки в клавиатуру
    keyboard.add(*buttons)

    return keyboard
