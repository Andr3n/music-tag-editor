# V.0.2
import eyed3
import os

CURRENT_PATH = os.getcwd()
os.chdir(os.path.join(CURRENT_PATH, 'Music'))
files = os.listdir()

print('Ищу папку Music и проставляю теги в соответствии с их именем...', end='\n\n')

for f in files:
    file_name = f.replace('.mp3', '')
    index_dash = file_name.find('-')
    
    try:
        audiofile = eyed3.load(f)
        
    except FileNotFoundError:
        print('Путь к файлам не найден')
        print('Проверьте, находится ли скрипт рядом с папкой Music')
        input('Нажмите любую клавишу, для завершения...')
        
    if not audiofile.tag:
        audiofile.initTag()
            
    audiofile.tag.artist = file_name[:index_dash]
    audiofile.tag.title = file_name[index_dash+1:]
    audiofile.tag.save()      
        
print('Теги успешно проставлены!', end='\n\n')

input('Нажмите любую клавишу, для завершения...')
