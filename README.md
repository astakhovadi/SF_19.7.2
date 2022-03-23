# SF_19.7.2
В api.py описаны api, взятые с сайта https://petfriends1.herokuapp.com/apidocs/#/

В settings.py заложены правильные и ошибочные пароль и логин

В папке tests->imagine картинки, использующиеся в тестировании сайта, с разными форматами файлов

В папке tests->test_pet_friends.py описаны позитивное и негативное тестирование сайта https://petfriends1.herokuapp.com/.

Позитивные тесты:
1) Получение ключа существующего пользователя с использованием валидных логина и пароля. Тестирование get/api/key (тест пройден)
2) Получение id питомца. Тестирование get/api/pets (тест пройден)
3) Добавление питомца без фото. Тестирование post/api/create_pet_simple (тест пройден)
4) Удаление питомца. Тестирование delete/api/pets (тест пройден)
5) Удаление рандомного питомца. Тестирование delete/api/pets (тест пройден)
6-8) Обновление полной/частичной информации о питомце. Тестирование put/api/pets (тест пройден)
9-10) Добавление питомца c фото формата jpg и png. Тестирование post/api/pets (jpg - тест пройден, png - тест не пройден, хотя данный формат должен поддерживаться)

*Также проводилось тестирование на заполнение имени/типа животного состоящего из двух слов (напр, "Немецкая овчарка"). 
Тестирование post/api/create_pet_simple (тест пройден). Тестирование post/api/pets (тест пройден). Для подверждения теста достаночно изменить 
параметры в тестах 3 и 9.


Негативные тесты:
11-13) Ввод неверных/пустых строк при логине на сайте. Тестирование get/api/key (Ошибка со стороны пользователя 403)
14)Проверяем возможность обновления информации о питомце. Подаем на вход возраста данные в формате int, а не str, как ожидает функция
    Тестирование post/api/create_pet_simple (тест пройден, информация добавлена).
15-17)Добавление нового питомца с частичной информацией (возрастом/именем/типом)
    Тестирование post/api/create_pet_simple (тест пройден, информация добавлена, однако логично, что это баг сайта т.к на сайте публикуется, например, 
                                                                                                                   только значение возраста).
 18-19) Добавление питомца c фото формата txt и gif. Тестирование post/api/pets (Тест пройден. Выдается ошибка)
 20) Сортируем питомцев по неверному фильтру. Тестирование get/api/pets (Тест пройден. Выдается ошибка)

*Были обнаружены баги при добавлении/изменении информации питомцев: напр, можно ввести "слово" в параметры возраста, можно ввести "число" в имя питомца.
 Тестирование post/api/create_pet_simple. Тестирование put/api/pets. Тестирование post/api/pets
