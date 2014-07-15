import os
import time

# файлы и каталоги, которые бекапим
source_dir = '/home/fin/js/'
source = ['a-byte-of-python']

# чтобы не париться, архив кладем туда же, где исходники
target_dir = source_dir

today = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(target_dir + today)  # создание папки, если ее нет
print('папка создана')

target = today + os.sep + time.strftime('%H%M%S') + '.zip'

# команда архивирования
zip_command = "cd {0} && zip -qr {1} {2}".format(source_dir, target, ' '.join(source))

if os.system(zip_command) == 0:
    print('бекап сделан в', target)
else:
    print('бекап сделать не удалось')