import asyncio

from aiogram import types
from config import dp, bot, question1, answer1, question2, answer2, question3, answer3, \
    question4, answer4, question5, answer5, question6, answer6, question7, answer7, question8, \
    answer8, question9, answer9, question10, answer10, first_message
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.answers import get_answer_keyboard
from aiogram.dispatcher import FSMContext


class Questions(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()
    Q11 = State()


# Обработка команд /start и /help
@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer(first_message)


# Отлавливание ответа "да"
@dp.message_handler(lambda message: message.text.lower() == 'да', state=None)
async def process_yes(message: types.Message):
    # Переводим пользователя в состояние Q1 (первый вопрос)
    await Questions.Q1.set()
    # Отправляем первый вопрос
    await message.answer(question1, reply_markup=get_answer_keyboard(answer1))


# Первый вопрос
@dp.message_handler(state=Questions.Q1)
async def process_q1(message: types.Message, state: FSMContext):
    if message.text == 'Футуризм':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'Н'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q2.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question2, reply_markup=get_answer_keyboard(answer2))


# Второй вопрос
@dp.message_handler(state=Questions.Q2)
async def process_q2(message: types.Message):
    if message.text == 'Salvador Dali':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'А'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q3.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    image_path = "img/1.jpg"
    photo = types.InputFile(image_path)
    await message.answer_photo(photo, caption=question3, reply_markup=get_answer_keyboard(answer3))


# Третий вопрос
@dp.message_handler(state=Questions.Q3)
async def process_q3(message: types.Message):
    if message.text == 'Обретение гармонии':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'Р'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q4.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question4, reply_markup=get_answer_keyboard(answer4))


# Четвертый вопрос
@dp.message_handler(state=Questions.Q4)
async def process_q4(message: types.Message):
    if message.text == 'Убийство Джоффри Баратеона':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'В'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q5.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question5, reply_markup=get_answer_keyboard(answer5))


# Пятый вопрос
@dp.message_handler(state=Questions.Q5)
async def process_q5(message: types.Message):
    if message.text == 'В переулке на Тверской улице':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'С'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q6.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question6, reply_markup=get_answer_keyboard(answer6))


# Шестой вопрос
@dp.message_handler(state=Questions.Q6)
async def process_q6(message: types.Message):
    if message.text == 'c XIV по XVII век':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'К'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q7.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question7, reply_markup=get_answer_keyboard(answer7))


# Седьмой вопрос
@dp.message_handler(state=Questions.Q7)
async def process_q7(message: types.Message):
    if message.text == 'Уровень B':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'А'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q8.set()
    await asyncio.sleep(2)
    await message.answer("Переходим к следующему вопросу")
    await asyncio.sleep(2)
    await message.answer(question8)


# Восьмой вопрос
@dp.message_handler(state=Questions.Q8)
async def process_q8(message: types.Message):
    if message.text != '':
        await asyncio.sleep(2)
        await message.answer("Правильно! Ты получаешь букву 'Я'")
    else:
        await asyncio.sleep(2)
        await message.answer("К сожалению, ответ неправильный")
    await Questions.Q9.set()
    await asyncio.sleep(2)
    await message.answer('Теперь у тебя есть все необходимое, чтобы переместиться на первую '
                         'контрольную точку!\n\n'
                         'Составь из букв слово и отправь его ответным сообщением \n\nПодсказка '
                         'на случай, если ты собрала не все буквы и/или тупишь. Это место - '
                         'станция метро, очень связано с одной таинственной рекой под названием '
                         'Нарва')


# Отлавливаем кодовое слово
@dp.message_handler(state=Questions.Q9)
async def process_q9(message: types.Message):
    if message.text.lower() == 'нарвская':
        await asyncio.sleep(2)
        await message.answer("Все верно! Отправляйся туда и жди дальнейших указаний")
    else:
        await asyncio.sleep(2)
        await message.answer('Что-то пошло не так... Отправляйся на станцию Нарвская и жди '
                             'дальнейших указаний')
    await Questions.Q10.set()
    await asyncio.sleep(15 * 60)
    await message.answer("Вижу, что ты почти на месте. Осталось совсем немного, всего два вопроса, "
                         "постарайся! Продолжаем!")
    await asyncio.sleep(2)
    await message.answer(question9, reply_markup=get_answer_keyboard(answer9))


@dp.message_handler(state=Questions.Q10)
async def process_q10(message: types.Message):
    if message.text != '':
        await asyncio.sleep(2)
        await message.answer("Отлично! Держи следующую подсказку")
        image_path = "img/2.png"
        photo = types.InputFile(image_path)
        await message.answer_photo(photo, caption='Тебе сюда, через некоторое время я свяжусь с '
                                                  'тобой')
    await Questions.Q11.set()
    await asyncio.sleep(13 * 60)
    await message.answer("Настал черёд последнего вопроса, важно ответить правильно, не торопись ")
    await asyncio.sleep(2)
    await message.answer(question10)


@dp.message_handler(state=Questions.Q11)
async def process_q11(message: types.Message, state: FSMContext):
    if message.text != '':
        await asyncio.sleep(2)
        await message.answer("Ура! Все получилось, Герман ждет тебя тут")
        image_path = "img/3.png"
        photo = types.InputFile(image_path)
        await message.answer_photo(photo, caption='Где-то в этой области')
    await asyncio.sleep(60 * 5)
    await state.finish()
