"""1. Скопировать в файл F2 только четные строки из F1.
Подсчитать размер файлов F1 и F2 (в байтах)."""
import os

file_txt1 = "F1.txt"
file_txt2 = "F2.txt"

try:
    file1 = open(file_txt1, "r")
    file2 = open(file_txt2, "w")

    lines_of_first_file = file1.readlines()  # чтение всех строк

    file2.writelines(lines_of_first_file[::2])  # запись во второй файл строк,
    # которые удовл. условию среза item[START:STOP:STEP], где START и STOP начало и конец всей строки через 2 строки

    print(os.path.getsize(file_txt1))
    print(os.path.getsize(file_txt2))

    file1.close()
    file2.close()

except FileNotFoundError:
    print("Исходный файл не найден")
except IOError:
    print("Происхошла ошибка чтения\"\"записи файла")
