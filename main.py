import time
import os
import desktop_wallpaper_parser
import images_yandex
import info

def start_main():
    desktop_wallpaper_parser.your_screen_resolution()
    desktop_wallpaper_parser.information()

    images_yandex.image_parser_yandex()

    if info.yandex_point:
        info.yandex_point.clear()
        time.sleep(2)
        images_yandex.image_parser_yandex_2()


def check_images_numbers():
    folder = f"{info.folder_name}"
    files_list = os.listdir(folder)
    info.number_of_downloaded_photos = 0

    for item in files_list:
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            info.number_of_downloaded_photos += 1

def menu():
    try:
        images_yandex.viewing_images()

        if info.yandex_point:
            desktop_wallpaper_parser.download_wallpapers_for_your_desktop()

    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    while True:
        start_main()

        while True:
            menu()
            check_images_numbers()

            if info.number_of_downloaded_photos == info.number_images:
                print(f'Пак обоев успешно создан. {info.number_images} - {info.number_of_downloaded_photos}\n')

                choice = input("Хотите создать новый пак обоев? (да/нет): ")
                if choice.lower() == 'да':
                    break  # Выходим из внутреннего цикла и начинаем новый пак

                elif choice.lower() == 'нет':
                    print('\nХорошо. Удачи.')
                    time.sleep(2)
                    exit()  # Завершаем программу

            else:
                time.sleep(3)
                desktop_wallpaper_parser.flipping_through()
                images_yandex.viewing_images()