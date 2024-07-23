import time
import random
import shutil
import requests
import tkinter as tk
import pyautogui
from PIL import Image
import os
import info

def information():
    info.number_images = int(input('Введите количество обоев --> '))
    info.text = input('Введите тему обоев --> ')
    info.folder_name = f"Папка - {info.text}"

def your_screen_resolution():
    root = tk.Tk()
    info.screen_width = root.winfo_screenwidth()
    info.screen_height = root.winfo_screenheight()
    root.destroy()

def flipping_through():
    pyautogui.press('right')

def download_wallpapers_for_your_desktop():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, info.folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    def save_image(url, folder_name, filename):
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            file_path = os.path.join(folder_name, filename)
            time.sleep(random.uniform(3, 5))

            with open(file_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)

            response.close()

        else:
            print(f"Не удалось скачать изображение. Статус-код: {response.status_code}")

    for i, yandex_image_url in enumerate(info.solution_images_link_ya):
        save_image(f'https:{yandex_image_url}', folder_path, f"yandex_image_{i}.jpg")

    time.sleep(random.uniform(3, 5))

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            file_path = os.path.join(folder_path, filename)

            try:
                image = Image.open(file_path)
                width, height = image.size
                time.sleep(random.uniform(3, 5))

                if info.screen_width > width or info.screen_height > height:
                    os.remove(file_path)

                image.close()

            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}")

