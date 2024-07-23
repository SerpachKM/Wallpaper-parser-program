# Парсер обоев на рабочий стол 

Описание проекта 

О проекте: Этот проект предназначен для автоматического скачивания и настройки обоев для рабочего стола на основе заданной темы. Скрипты используют Яндекс для поиска изображений, фильтруют их по разрешению экрана и сохраняют подходящие изображения в указанную папку.

Содержимое проекта

Проект состоит из четерех основных файлов:

- desktop_wallpaper_parser.py

- images_yandex.py

- main.py

- info.py

'desktop_wallpaper_parser.py'

Этот файл содержит функции для:

Получения информации о количестве обоев и теме от пользователя.
Определения разрешения экрана пользователя.
Скачивания и сохранения изображений с Яндекса, подходящих по разрешению экрана.

Основные функции:

information(): запрашивает у пользователя количество обоев и тему.

your_screen_resolution(): определяет разрешение экрана.

download_wallpapers_for_your_desktop(): скачивает изображения и сохраняет их в указанную папку.

'images_yandex.py'

Этот файл включает функции для парсинга изображений с Яндекса и их фильтрации. Также здесь реализована функция просмотра изображений.

Основные функции:

image_parser_yandex(): парсит изображения по заданной теме.

image_parser_yandex_2(): альтернативный метод парсинга изображений.

viewing_images(): функция для просмотра изображений.

main.py

Главный файл проекта, который управляет всем процессом. Здесь происходит вызов функций из других файлов и организация основного цикла программы.

Основные функции:

start_main(): запускает основной процесс, включая определение разрешения экрана и запрос информации у пользователя.

check_images_numbers(): проверяет количество скачанных изображений.

menu(): основной цикл, который управляет скачиванием и просмотром изображений.

Установка и использование

- Клонируйте репозиторий.

- Установите необходимые библиотеки: ```pip install -r requirements.txt```

- Запустите основной скрипт: ```python main.py```

Пример использования

1. Запустите скрипт main.py.
2. Введите количество обоев и тему.
3. Скрипт автоматически скачает изображения, подходящие по разрешению экрана, и сохранит их в папке с именем, соответствующим теме.
4. После завершения скачивания вы можете выбрать, создать ли новый пак обоев или завершить программу.

Зависимости
- Python 3.x
- Библиотеки: requests, tkinter, pyautogui, PIL, shutil

Автор
Этот проект был разработан для автоматизации процесса поиска и настройки обоев для рабочего стола.

Заключение
Этот проект предоставляет удобный способ автоматического скачивания обоев на основе заданной темы и разрешения экрана. Он полезен для тех, кто хочет регулярно обновлять свои обои без необходимости вручную искать и скачивать изображения. К сожелению этот проект не совсем рабочий пока что потому что Selenium плохо работает с Яндексом.

