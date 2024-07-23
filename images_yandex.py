import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import info
import desktop_wallpaper_parser

def random_user_agent():
    global driver

    ua = UserAgent()
    user_agent = ua.random

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)

def image_parser_yandex():
    choice = 1

    random_user_agent()
    driver.get(f'{info.url}{info.text} обои {info.screen_width}X{info.screen_height}')
    time.sleep(5)

    html_code = driver.page_source
    soup = BeautifulSoup(html_code, 'html.parser')
    info.url_images_ya = soup.find(class_='Link ContentImage-Cover').get('href')
    info.yandex_point.append(choice)

    driver.quit()

def image_parser_yandex_2():
    try:
        random_user_agent()
        driver.get(f'https://yandex.ru{info.url_images_ya}')
        time.sleep(2)
        viewing_images()

    except Exception as e:
        print(f'Ошибка : {e}')


def viewing_images():
    try:
        while True:
            html_code_images = driver.page_source
            soup_ = BeautifulSoup(html_code_images, 'html.parser')
            button = soup_.find('button', class_='Button2 Button2_pin_brick-circle Button2_size_l Button2_view_default OpenImageButton-SizesButton MMViewerButtons-ImageSizes MMViewerButtons-Button')

            if button:
                time.sleep(random.uniform(2, 4))
                permission_images = button.find('span', class_='Button2-Text').text
                permission_device = f'{info.screen_width}×{info.screen_height}'

                if permission_device == permission_images or permission_device > permission_images:
                    link_images = soup_.find('img', class_='MMImage-Origin')
                    time.sleep(random.uniform(2, 4))

                    if link_images:
                        link_images_src = link_images.get('src')
                        info.solution_images_link_ya.append(link_images_src)
                        break

                    else:
                        print('Изображение не найдено')
                else:
                    time.sleep(5)
                    desktop_wallpaper_parser.flipping_through()
            else:
                print('Разрешение изображение не найдено')
                driver.quit()
                time.sleep(5)
                image_parser_yandex_2()

    except Exception as e:
        print(f'Ошибка : {e}')
        driver.quit()
        time.sleep(5)
        image_parser_yandex_2()

    choice = 1
    info.yandex_point.append(choice)

    driver.quit()