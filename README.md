Парсинг сайта на python с использованием фреймворка Django. На сайте выводятся карточки товара. При нажатии на товар, можно перейти к его подробному описанию. Как бд использовалась sqlite3.
При запуске программы Вас встретит вот такая страничка.
([image.png](https://github.com/Peggysturm/django-review/blob/dev/kartinki/image.png))
Чтобы этого избежать, в адресе нужно поставить / и написать номер страницы
Было: ![Alt text](image-1.png)
Стало: ![Alt text](image-2.png)

После этого начнётся парситься информация со страницы и результат выйдет на экран.

Также в левом верхнем углу сайта есть сортировка товаров по количествую отзывов о них. Можно сортировать по возрастанию или по убыванию. Чтобы сортировка заработала, нужно выбрать тип сортировки, а после нажать на кнопку применить. 
![Alt text](image-3.png)

Работу выполнил Дмитриев Вячеслав.
