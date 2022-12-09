# Справочник бухгалтера
## __Telegram Bot by AuF__

---
+ ## RU
Данного бота я сделал для получения большого опыта впрограммирование.
Создавая данный проект я столкнулся с новыми старыми проблемами, но которые я смог 
в полной мере решить. Тем кто понимает данный частично кодинг, надеюсь вы оцените мои
старания и соблюдения стандартам ``PEP8``.

В дальнейшем я буду дальше развивать этот проект добавляя больше возможностей и улучшая 
уже имеющиеся споособности бота.

Можете посмотреть как я писал примерно такого же бота раннее после 2-х месяцев обучения
``Python3``
Находится в папке ``old_bot``. И сравнить с тем как я пишу сейчас.

___
##### Небольшая рекомендация
___
>Data/config/config.py
```doctest
import os
from dotenv import load_dotenv

load_dotenv()

admins_id = [os.getenv('Your_list_of_admins')]
API_KEY = os.getenv('Your_API')
```

В этой части советую создать файл переменной окружения ``.env`` и сохранить свои данные
внутри неё для вашей безопасности, но можете передать и напрямую

Создавать же данный файл нужно в следующем путе: ``Data/config/.env``

---
- ### __Начало__

---
![Bot Commands](image/Commands.jpg)
Первое что вы видите при запуске данного бота

---
- ### __User Panel__

---
![User panel](image/userPanel.jpg)
Таким образом выглядит панель кнопок у обычного пользователя
---
- ### __Admin Panel__

---
![Admin panel](image/adminPanel.jpg)
Данным образом выглядит панель у админов бота

Панель кнопок подготавливается в следующем файле
>keyboards/default/start_kb.py
```doctest
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Полный список кнопок
keyboard = [
    [
        KeyboardButton(text='🎓Проверка знаний')
    ],
    [
        KeyboardButton(text='ℹ️Информация')
    ],
    [
        KeyboardButton(text='Реклама 🎥'),
        KeyboardButton(text='Статистика 📊')
    ]
]

# Список кнопок для обычных пользователей
start_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=keyboard[:-1],
                               resize_keyboard=True
                               )
# Список кнопок для админов
admin_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=keyboard,
                               resize_keyboard=True
                               )
```
Обрез списка ``keyboard[:-1]`` мы получаем из массива все элементы кроме последнего.
В целом объекты ``start_kb`` и ``admin_kb`` называть списком неправильно. Они являются
экземплярами класса ``ReplyKeyboardMurkup``, который в свою очередь возвращает словарь.
И внутри этого словаря в ключе ``keyboard`` лежит наш список с кнопочками.
- ### Рассылка
>handlers/admins/admin.py
```doctest
@dp.message_handler(state=State_Advertising.photo, content_types=types.ContentType.PHOTO)
async def photo_(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    # Обновляем данные фото в памяти
    await state.update_data(photo=photo_id)
    data = await state.get_data()
    # Получаем данные из 
    text = data.get('text')
    photo = data.get('photo')
    text = data.get('text')
    
    id_list = await db.len_user_id()
    i = 0
    # Запускается цикл перебора всех user_id в DB
    for user_id in id_list:
        # Отправляется сообщения пользователям
        await dp.bot.send_photo(chat_id=user_id[0], photo=photo, caption=text)
        i += 1

    await message.answer(text=f'Сообщение доставлено:\n{i=}')
    # Выход из Машино состояния
    await state.finish()
```
Настоятельно вам рекомендую просмотреть Python File находящийся в ``handlers/admins/admin.py``
Так называемая __Машино Состояние.__ 

---
+ ## ENG
I made this bot to get a lot of experience in programming.
Creating this project, I ran into new old problems, but which I was able to
fully resolve. For those who understand this partial coding, I hope you appreciate my
diligence and adherence to __PEP8__ standards

In the future, I will further develop this project by adding more features and improving
existing bot abilities.

You can see how I wrote about the same bot earlier after 2 months of training
``Python3``
Located in the ``old_bot`` folder. And compare with how I write now.

___
##### Small recommendation
___
>Data/config/config.py
```doctest
import os
from dotenv import load_dotenv

load_dotenv()

admins_id = [os.getenv('Your_list_of_admins')]
API_KEY = os.getenv('Your_API')
```

In this part, I advise you to create an environment variable file ``.env`` and save your data
inside it for your safety, but you can also pass it directly

You need to create this file in the next path: ``Data/config/.env``

---
- ### __The Start__

---
![Bot Commands](image/Commands.jpg)
The first thing you see when you start this bot

---
- ### __User Panel__

---
![User panel](image/userPanel.jpg)
This is how the button bar looks like for a regular user
---
- ### __Admin Panel__

---
![Admin panel](image/adminPanel.jpg)
This is how the panel for bot admins looks like

The button bar is prepared in the following file
>keyboards/default/start_kb.py
```doctest
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Full list of buttons
keyboard = [
    [
        KeyboardButton(text='🎓Проверка знаний')
    ],
    [
        KeyboardButton(text='ℹ️Информация')
    ],
    [
        KeyboardButton(text='Реклама 🎥'),
        KeyboardButton(text='Статистика 📊')
    ]
]

# List of buttons for regular users
start_kb = ReplyKeyboardMarkup(row_width=2,
                                keyboard=keyboard[:-1],
                                resize_keyboard=True
                                )
# List of buttons for admins
admin_kb = ReplyKeyboardMarkup(row_width=2,
                                keyboard=keyboard,
                                resize_keyboard=True
                                )
```
Trimming the list ``keyboard[:-1]`` we get all the elements from the array except the last one.
In general, the objects ``start_kb`` and ``admin_kb`` are wrong to call a list. They are
instances of the ``ReplyKeyboardMurkup`` class, which in turn returns a dictionary.
And inside this dictionary in the ``keyboard`` key is our list of buttons.
- ### Newsletter
>handlers/admins/admin.py
```doctest
@dp.message_handler(state=State_Advertising.photo, content_types=types.ContentType.PHOTO)
async def photo_(message: types.Message, state: FSMContext):
     photo_id = message.photo[-1].file_id
     # Update photo data in memory
     await state.update_data(photo=photo_id)
     data = await state.get_data()
     # Get data from
     text = data.get('text')
     photo = data.get('photo')
     text = data.get('text')
    
     id_list = await db.len_user_id()
     i = 0
     # Run a loop through all user_ids in the DB
     for user_id in id_list:
         # Send messages to users
         await dp.bot.send_photo(chat_id=user_id[0], photo=photo, caption=text)
         i += 1

     await message.answer(text=f'Сообщение доставлено:\n{i=}')
     # Exit Machine State
     await state.finish()
```
I strongly recommend that you look at the Python File located in ``handlers/admins/admin.py``
The so-called __Machine Condition.__
