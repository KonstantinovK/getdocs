import os
from bs4 import BeautifulSoup

# Указываем путь к папке с HTML файлами
html_dir = '/Users/macbook/Desktop/MWS/Анализ MWS/Фичевый анализ/selectel_data/html/'  # Замените на путь к вашей папке
txt_dir = '/Users/macbook/Desktop/MWS/Анализ MWS/Фичевый анализ/selectel_data/txt/'  # Замените на путь, где вы хотите сохранить TXT файлы

# Создаем папку для TXT файлов, если она не существует
if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

# Перебираем все HTML файлы в указанной папке
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        html_file_path = os.path.join(html_dir, filename)
        
        # Читаем содержимое HTML файла
        with open(html_file_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        
        # Используем BeautifulSoup для извлечения текста
        soup = BeautifulSoup(html_content, 'lxml')
        text_content = soup.get_text()

        # Убираем лишние пробелы и переносы строк
        cleaned_text = ' '.join(text_content.split())

        # Формируем имя для TXT файла
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_file_path = os.path.join(txt_dir, txt_filename)

        # Сохраняем текст в TXT файл
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(cleaned_text)

        print(f'Конвертирован: {html_file_path} -> {txt_file_path}')
