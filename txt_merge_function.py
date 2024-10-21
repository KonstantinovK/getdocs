import os

# Указываем путь к папке с TXT файлами
txt_dir = '/Users/macbook/Desktop/MWS/Анализ MWS/Фичевый анализ/selectel_data/txt/'  # Путь к папке с вашими TXT файлами
output_file = '/Users/macbook/Desktop/MWS/Анализ MWS/Фичевый анализ/selectel_data/merged.txt'  # Путь к выходному файлу

# Открываем выходной файл для записи
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Перебираем все файлы в папке
    for filename in os.listdir(txt_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(txt_dir, filename)
            # Читаем содержимое каждого файла и записываем в выходной файл
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content + '\n')  # Добавляем перенос строки между файлами

print(f'Все TXT файлы были объединены в {output_file}')
