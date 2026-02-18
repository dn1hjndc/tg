from pyrogram import Client, filters
from pyrogram.types import Message
import keyboards
import config
import buttons
from custom_filters import button_filter
# from costom_filters import button_filter
bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="блслб"
)

@bot.on_message(filters=filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}')


@bot.on_message(filters=filters.command("input"))
async def start(client: Client, message: Message):
    quiz = show_all()
    await message.reply(f"статистика - {quiz}")


from pyrogram import Client, filters
from pyrogram.types import Message
import keyboards
import config
import buttons
from custom_filters import button_filter

# Создаем экземпляр бота
app = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="@danpaulquiz_bot"
)

QUIZ_DATA = [

    {
        'level': 1,
        'question': "❓ Вопрос 1: Какая планета самая большая в Солнечной системе?",
        'keyboard': keyboards.qize1_keyboard,
        'right_button': buttons.right_button1,
        'wrong_buttons': [
            buttons.not_right_button1,
            buttons.not_right_button2,
            buttons.not_right_button3
        ]
    },

    {
        'level': 2,
        'question': "❓ Вопрос 2: Сколько материков на Земле?",
        'keyboard': keyboards.qize2_keyboard,
        'right_button': buttons.right_button2,
        'wrong_buttons': [
            buttons.not_right_button4,
            buttons.not_right_button5
        ]
    },

    {
        'level': 3,
        'question': "❓ Вопрос 3: Какой газ мы вдыхаем?",
        'keyboard': keyboards.qize3_keyboard,
        'right_button': buttons.right_button3,
        'wrong_buttons': [
            buttons.not_right_button6,
            buttons.not_right_button7
        ]
    },

    {
        'level': 4,
        'question': "❓ Вопрос 4: Столица Франции?",
        'keyboard': keyboards.qize4_keyboard,
        'right_button': buttons.right_button4,
        'wrong_buttons': []
    },

    {
        'level': 5,
        'question': "❓ Вопрос 5: Сколько цветов в радуге?",
        'keyboard': keyboards.qize5_keyboard,
        'right_button': buttons.right_button5,
        'wrong_buttons': []
    },

    {
        'level': 6,
        'question': "❓ Вопрос 6: Самое высокое животное на Земле?",
        'keyboard': keyboards.qize6_keyboard,
        'right_button': buttons.right_button6,
        'wrong_buttons': []
    },

    {
        'level': 7,
        'question': "❓ Вопрос 7: Какой химический элемент обозначается как 'O'?",
        'keyboard': keyboards.qize7_keyboard,
        'right_button': buttons.right_button7,
        'wrong_buttons': []
    }
]

RIGHT_BUTTONS = {
    item['right_button']: item
    for item in QUIZ_DATA
}

ALL_WRONG_BUTTONS = []
for item in QUIZ_DATA:
    ALL_WRONG_BUTTONS.extend(item['wrong_buttons'])


@app.on_message(filters=filters.command("quiz") | button_filter(buttons.setting_button))
async def start_quiz(client: Client, message: Message):
    first_level = QUIZ_DATA[0]

    await message.reply(
        text=first_level['question'],
        reply_markup=first_level['keyboard']
    )


@app.on_message(filters=button_filter(list(RIGHT_BUTTONS.keys())))
async def handle_right_answer(client: Client, message: Message):
    for button, level_data in RIGHT_BUTTONS.items():
        if button_filter(button).__call__(None, message):
            current_level = level_data['level']

            if current_level < len(QUIZ_DATA):
                next_level = QUIZ_DATA[current_level]

                await message.reply(
                    text=f"✅ ПРАВИЛЬНО!\n\n{next_level['question']}",
                    reply_markup=next_level['keyboard']
                )
            else:
                await message.reply(
                    text="🏆 ПОБЕДА! 🏆\n\n"
                         "Ты успешно прошёл все 7 уровней викторины!\n"
                         "Ты настоящий знаток!\n\n"
                         "Хочешь попробовать ещё раз? Напиши /quiz",
                    reply_markup=keyboards.main_keyboard
                )
            break


@app.on_message(filters=button_filter(ALL_WRONG_BUTTONS))
async def handle_wrong_answer(client: Client, message: Message):
    await message.reply(
        text="❌ НЕПРАВИЛЬНО!\n\n"
             "К сожалению, ты ошибся. Викторина начинается заново.\n"
             "Попробуй ещё раз! Нажми /quiz",
        reply_markup=keyboards.main_keyboard
    )

@app.on_message(filters=filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply(
        text=f"👋 Привет, {message.from_user.first_name}!\n\n"
             f"🎮 Я бот-викторина с 7 уровнями сложности.\n"
             f"На каждом уровне тебе нужно выбрать правильный ответ.\n\n"
             f"📋 Правила:\n"
             f"• Правильный ответ - переходишь на следующий уровень\n"
             f"• Неправильный ответ - начинаешь сначала\n\n"
             f"🚀 Нажми /quiz чтобы начать викторину!",
        reply_markup=keyboards.main_keyboard
    )

    if __name__ == '__main__':
        print("=" * 50)
        print("🤖 БОТ-ВИКТОРИНА ЗАПУЩЕН")
        print("📊 Уровней: 7")
        print("=" * 50)
        app.run()



