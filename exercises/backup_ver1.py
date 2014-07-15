import os
import time

# файлы и каталоги, которые бекапим
source_dir = '/home/fin/js/'
source = ['a-byte-of-python']

# чтобы не париться, архив кладем туда же, где исходники
target_dir = source_dir

target = target_dir + os.sep + time.strftime('%Y.%m.%d_%H-%M-%S') + '.zip'

#
zip_command = "cd {0} && zip -qr {1} {2}".format(source_dir, target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('бекап сделан в', target)
else:
    print('бекап сделать не удалось')