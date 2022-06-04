# genetic-neural-network


_**УКРАЇНСЬКИЙ КАТОЛИЦЬКИЙ УНІВЕРСИТЕТ**_

_**ФАКУЛЬТЕТ ПРИКЛАДНИХ НАУК**_

_**Комп’ютерні науки**_



**Дослідження й симуляція штучного життя за допомогою теорії автоматів та машини Тюрінга.**

![image](https://user-images.githubusercontent.com/91616531/172024410-9e5ca404-12e2-4993-8a32-e11e518cf6ca.png = 250x250)


*Автори:*

Іван Шевченко

Казимир Арсеній

Ярослав Клим

Польова Анна

Олексюк Любомир


4 червня 2022


**Короткий опис проекту**


На полі є два види об’єктів: квіточки і організми. Організми можуть їсти квіточки і одне одного, розмножуватись, мутувати і рухатися в межах поля.

Коли організм стикається з квіточкою, він отримує її енергію, яка залежна від розміру квіточки (розмір вибирається випадково при створенні)
Коли організм стикається з іншим організмом, більший поїдає меншого і отримує енергію, яка знову ж таки залежна від його розміру.

Енергія потрібна організмам для того, щоб розмножуватись і рухатись. Рух забирає енергію (її кількість залежить від розміру і швидкості організму),  і якщо вона закінчується, організм помирає. При розмноженні енергія організму зменшується вдвічі.

Коли організм розмножується, він мутує. З певним шансом змінюється його розмір і змінюється нейронна мережа, яка відповідає за прийняття рішення, куди організм має рухатись. Себто при мутації може змінитися кут зору організму і аналіз даних, які організм отримує з нього.

В кожного організму є зір, який складається з 24 ліній (очей), які бачать на відстань 1 і на певний кут. Нейронна мережа аналізує дані, отримані від зору (про стіни та інші організми), та власні параметри (розмір та енергію), і базуючись на цьому організм робить рух з певною швидкістю і напрямом.

Базуючись на запусках програми, модуль scene створює відео, яке показує, як рухались і розмножувались організми впродовж програми
