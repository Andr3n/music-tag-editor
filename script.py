# v0.3
import eyed3
import os

# Получаем текущий путь
CURRENT_PATH = os.getcwd()
MUSIC_FOLDER_PATH = os.path.join(CURRENT_PATH, 'Music')
TEXT_MENU="""
1. Проставить теги (имя, исполнитель) для треков в папке Music
2. Проставить жанр для треков в папке Music
3. Очистить теги
0. Выход
"""

while(True):
    step = int(input(TEXT_MENU))
    
    # Выход
    if step == 0:
        break
    
    # Проставляем теги Исполнитель, Заголовок
    elif step == 1:

        print('Ищу папку Music и проставляю теги в соответствии с их именем...', end='\n\n')
        try:
            os.chdir(MUSIC_FOLDER_PATH)
        
        except FolderNotFoundError:
            print('Папка Music не найдена!')
            print('Проверьте, находится ли скрипт рядом с папкой Music')
            break
            
        files = os.listdir()

        for f in files:
            file_name = f.replace('.mp3', '')
            index_dash = file_name.find('-')

            try:
                audiofile = eyed3.load(f)

            except Exception as e:
                print('Путь к файлам не найден')
                print('Проверьте, существуют ли файлы в каталоге Music')
                input('Нажмите любую клавишу, для завершения...')

            if not audiofile.tag:
                audiofile.initTag()

            audiofile.tag.artist = file_name[:index_dash]
            audiofile.tag.title = file_name[index_dash+1:]
            audiofile.tag.save()      

        print('Теги успешно проставлены!', end='\n\n')
    
    # Проставляем жанр
    elif step == 2:
        genre = input('Введите жанр:\n')
        print('Ищу папку Music и проставляю жанр', end='\n\n')
        try:
            os.chdir(MUSIC_FOLDER_PATH)
        
        except NameError:
            print('Папка Music не найдена!')
            print('Проверьте, находится ли скрипт рядом с папкой Music')
            raise
            
        files = os.listdir()

        for f in files:

            try:
                audiofile = eyed3.load(f)

            except Exception:
                print('Путь к файлам не найден')
                print('Проверьте, существуют ли файлы в каталоге Music')
                input('Нажмите любую клавишу, для завершения...')

            if not audiofile.tag:
                audiofile.initTag()

            audiofile.tag.genre = genre
            audiofile.tag.save()      

        print('Тег Жанр успешно проставлен!', end='\n\n')
    
    # Очистка тегов
    elif step == 3:
        
        print('Ищу папку Music и очищаю теги', end='\n\n')
        try:
            os.chdir(MUSIC_FOLDER_PATH)
        
        except NameError:
            print('Папка Music не найдена!')
            print('Проверьте, находится ли скрипт рядом с папкой Music')
            raise
            
        files = os.listdir()

        for f in files:

            try:
                audiofile = eyed3.load(f)

            except Exception:
                print('Путь к файлам не найден')
                print('Проверьте, существуют ли файлы в каталоге Music')
                input('Нажмите любую клавишу, для завершения...')

            if not audiofile.tag:
                audiofile.initTag()

            audiofile.tag.clear()
            audiofile.tag.save()      

        print('Теги успешно очищены!', end='\n\n')
    
    # Если ввод неверный
    else:
        print('Данного пункта меню не существует!')
        print(f'Введенный пункт: {step}', end='\n\n')

input('Нажмите любую клавишу, для завершения...')
