# Справочник бухгалтера
## __Telegram Bot by AuF__

---
+ #### RU
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
+ #### ENG
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
