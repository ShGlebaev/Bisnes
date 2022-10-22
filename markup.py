from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_Tema = KeyboardButton('Тематический Бизнес')
btn_2 = KeyboardButton('Про гранты')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_Tema, btn_2)

button_1 = KeyboardButton('1⃣')
button_2 = KeyboardButton('2⃣')
button_3 = KeyboardButton('3⃣')
button_4 = KeyboardButton('4⃣')
button_5 = KeyboardButton('5⃣')
button_6 = KeyboardButton('6⃣')
button_7 = KeyboardButton('7⃣')
button_8 = KeyboardButton('8⃣')
button_9 = KeyboardButton('9⃣')
button_10 = KeyboardButton('🔟')
button_back = KeyboardButton('Назад ➡')

tematicMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2, button_3, button_4, button_5, button_6,
                                                            button_7, button_8, button_9, button_10, button_back)

button1 = KeyboardButton('Прокат автомобилей')
button2 = KeyboardButton('Автостоянка')
button3 = KeyboardButton('Автосалон')
button4 = KeyboardButton('Шиномонтаж')
button_back = KeyboardButton('Назад ➡')
AvtoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3, button4, button_back)

btn1 = KeyboardButton('Детский магазин')
btn2 = KeyboardButton('Детская игровая комната')
btn3 = KeyboardButton('Детский магазин одежды')
btn4 = KeyboardButton('Детский развивающий центр')
button_back = KeyboardButton('Назад ➡')
ChildrenMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2, btn3, btn4, button_back)

bu1 = KeyboardButton('Мини-типография')
bu2 = KeyboardButton('Газеты')
bu3 = KeyboardButton('Журналы')
bu4 = KeyboardButton('Типография')
button_back = KeyboardButton('Назад ➡')
PublishingMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bu1, bu2, bu3, bu4, button_back)

bu_1 = KeyboardButton('Комп. клуба')
bu_2 = KeyboardButton('Интернет магазина')
bu_3 = KeyboardButton('Интернет сайт')
bu_4 = KeyboardButton('Интернет-проект')
button_back = KeyboardButton('Назад ➡')
ITMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bu_1, bu_2, bu_3, bu_4, button_back)

bn_1 = KeyboardButton('Интернет магазина')
bn_2 = KeyboardButton('Магазина бижутерии')
bn_3 = KeyboardButton('Канцелярского магазина')
bn_4 = KeyboardButton('Магазина чая и кофе')
button_back = KeyboardButton('Назад ➡')
magazineMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bn_1, bn_2, bn_3, bn_4, button_back)

bt_1 = KeyboardButton('Строительный магазин') #
bt_2 = KeyboardButton('Макетная мастерская')
bt_3 = KeyboardButton('Склад') #
bt_4 = KeyboardButton('Бизнес центр') #
button_back = KeyboardButton('Назад ➡')
constructionMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bt_1, bt_2, bt_3, bt_4, button_back)

b1 = KeyboardButton('Репетиторский центр') #
b2 = KeyboardButton('Иностранные языки') #
b3 = KeyboardButton('Автошкола')
b4 = KeyboardButton('Кинологический центр')
button_back = KeyboardButton('Назад ➡')
educationMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b1, b2, b3, b4, button_back)

b_1 = KeyboardButton('Кафе-кондитерская')
b_2 = KeyboardButton('Пивной бар')
b_3 = KeyboardButton('Блинная')
b_4 = KeyboardButton('Бар')
button_back = KeyboardButton('Назад ➡')
cateringMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b_1, b_2, b_3, b_4, button_back)

bo1 = KeyboardButton('Игровой клуб')
bo2 = KeyboardButton('Баня')
bo3 = KeyboardButton('Сауна')
bo4 = KeyboardButton('Кальянная')
button_back = KeyboardButton('Назад ➡')
rapeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bo1, bo2, bo3, bo4, button_back)

bo_1 = KeyboardButton('Спорт магазин')
bo_2 = KeyboardButton('Прокат велосипедов')
bo_3 = KeyboardButton('Скейт-парк')
bo_4 = KeyboardButton('Ледовый каток')
button_back = KeyboardButton('Назад ➡')
sportMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bo_1, bo_2, bo_3, bo_4, button_back)