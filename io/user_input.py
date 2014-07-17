import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('введите текст: ')

# регулярки в питоне непривычные
something = re.sub(r'[\s\?\.,!-]', '', something)

if is_palindrome(something.lower()):
    print('это палиндром')
else:
    print('нет, не палиндром')