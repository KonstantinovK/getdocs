import os
import requests
import xml.etree.ElementTree as ET
import time  # Импортируем модуль time для добавления паузы
from urllib.parse import urlparse

# Указываем полный путь к папке, куда будут сохраняться страницы
save_dir = '/Users/macbook/Desktop/MWS/Анализ MWS/Фичевый анализ/selectel_data'

# Создаем папку, если она не существует
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# URL карты сайта
sitemap_url = 'https://docs.selectel.ru/sitemap.xml'  # Обновленный URL

# Запрос к sitemap.xml
response = requests.get(sitemap_url)

# Парсинг XML и скачивание страниц
if response.status_code == 200:
    root = ET.fromstring(response.content)
    
    # Перебираем все URL
    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        page_url = url.text
        try:
            page_response = requests.get(page_url)
            if page_response.status_code == 200:
                # Генерируем имя файла для страницы
                parsed_url = urlparse(page_url)
                # Заменяем слэши на подчеркивания, чтобы избежать проблем с именами файлов
                page_name = parsed_url.path.replace("/", "_") + ".html"  
                
                # Формируем полный путь к файлу
                file_path = os.path.join(save_dir, page_name)
                
                # Если файл уже существует, добавляем уникальный суффикс
                if os.path.exists(file_path):
                    base, ext = os.path.splitext(file_path)
                    i = 1
                    while os.path.exists(file_path):
                        file_path = f"{base}_{i}{ext}"
                        i += 1
                
                # Сохраняем страницу в указанную папку
                with open(file_path, 'wb') as f:
                    f.write(page_response.content)
                print(f"Скачана страница: {page_url} -> сохранена как: {file_path}")
            else:
                print(f"Не удалось скачать страницу: {page_url} (статус: {page_response.status_code})")
        except Exception as e:
            print(f"Ошибка при скачивании {page_url}: {e}")
        
        # Добавляем паузу в 1 секунду
        time.sleep(1)
else:
    print(f"Ошибка загрузки карты сайта: {response.status_code}")
