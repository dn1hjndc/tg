from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons

# Главная клавиатура
main_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎮 Начать викторину", callback_data=buttons.setting_button)]
])

# Клавиатура для 1 уровня
qize1_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Марс", callback_data=buttons.not_right_button1)],
    [InlineKeyboardButton("Юпитер", callback_data=buttons.right_button1)],
    [InlineKeyboardButton("Сатурн", callback_data=buttons.not_right_button2)],
    [InlineKeyboardButton("Земля", callback_data=buttons.not_right_button3)]
])

# Клавиатура для 2 уровня
qize2_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("4", callback_data=buttons.not_right_button4)],
    [InlineKeyboardButton("5", callback_data=buttons.not_right_button5)],
    [InlineKeyboardButton("6", callback_data=buttons.right_button2)],
    [InlineKeyboardButton("7", callback_data=buttons.not_right_button6)]
])

# Клавиатура для 3 уровня
qize3_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Кислород", callback_data=buttons.right_button3)],
    [InlineKeyboardButton("Углекислый газ", callback_data=buttons.not_right_button7)],
    [InlineKeyboardButton("Азот", callback_data=buttons.not_right_button1)],
    [InlineKeyboardButton("Водород", callback_data=buttons.not_right_button2)]
])

# Клавиатура для 4 уровня
qize4_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Лондон", callback_data=buttons.not_right_button3)],
    [InlineKeyboardButton("Берлин", callback_data=buttons.not_right_button4)],
    [InlineKeyboardButton("Париж", callback_data=buttons.right_button4)],
    [InlineKeyboardButton("Мадрид", callback_data=buttons.not_right_button5)]
])

# Клавиатура для 5 уровня
qize5_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("5", callback_data=buttons.not_right_button6)],
    [InlineKeyboardButton("6", callback_data=buttons.not_right_button7)],
    [InlineKeyboardButton("7", callback_data=buttons.right_button5)],
    [InlineKeyboardButton("8", callback_data=buttons.not_right_button1)]
])

# Клавиатура для 6 уровня
qize6_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Слон", callback_data=buttons.not_right_button2)],
    [InlineKeyboardButton("Жираф", callback_data=buttons.right_button6)],
    [InlineKeyboardButton("Кит", callback_data=buttons.not_right_button3)],
    [InlineKeyboardButton("Страус", callback_data=buttons.not_right_button4)]
])

# Клавиатура для 7 уровня
qize7_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Золото", callback_data=buttons.not_right_button5)],
    [InlineKeyboardButton("Кислород", callback_data=buttons.right_button7)],
    [InlineKeyboardButton("Осмий", callback_data=buttons.not_right_button6)],
    [InlineKeyboardButton("Олово", callback_data=buttons.not_right_button7)]
])