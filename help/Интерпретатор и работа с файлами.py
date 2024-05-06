для того что бы в Виндовс открыть файл в интерпретаторе нужно зайти в папку с файлом в адресной строке
ввести cmd  появится окно cmd далее ввести python имя_файла.py и программа запуститься

                                          # УРОКИ ЕГОРОВА:
                    # Работа с файлами:
 # -Чтение с файла
a=open('name_file.txt') # - функция open , первый аргумент - это имя файла
print(a.read())
open('name_file.txt', encoding='utf-8') # - второй аргумент - это кодировка для нормального распознавания русских букв,
# если в файле буквы только английские, то кодировку указывать не нужно

# Если файл лежит в другом месте, то нужно указать путь к нему
file=open(r'C:\Users\Zver\PycharmProjects\Test\111.txt') # - r перед строкой служит для нормального восприятия программой символов  типа '\\'
print(file.read(23)) #- выводим первые 23 символа из файла file,
print(file.read(3)) #- питон запоминает место где он остановился, поэтому при повторном выводе он будет выводить следующие 3 символа,
# а не начинать сначала.

file.seek(0) #- метод, который позволяет указать позицию активной клетки,.seek(0) - т.е мы переместимся в начало, в нулевую клетку

print(file.readline()) #- выводит первую строчку
print(file.readline()) #- выводит вторую строчку

for row in file:        #- выводит все строки из файла
    print(row)

for row in file:        - выводит все буквы из строк из файла
    for letter in row:
        print(letter)

s=file.readlines() - метод который позволяет создать список элементами которого будут строки файла(каждая строка заканчивается '\n')
print(s)

-Запись в файлам
file=open('name_file.txt', 'r') - если не указывать 'r' или 'w' по умалочанию режим 'r'
file=open('name_file.txt', 'w')
file.write('hello')
file.write('hello') - слова записываются друг за другом, без пробелов и переноса строк
file.write('hello\n') - слова записываются с новой строки
file=open('name_file.txt', 'a') - режим 'a' позволяет записывать новые данные, после уже имеющихся, не стирая старых данных

нужно учитывать - не все режимы поддерживают одновременное чтение и запись файла, допустим 'w' и 'a' не поддерживают чтение
для этого нужно закрывать файл и открывать его в другом режиме, либо использовать режимы поддерживающие чтение, допустим 'a+'

file.close() - закрывает файл для очистки используемой памяти


                         УРОКИ ИЗ КУРСА ПРОГРАММИРОВАНИЕ НА ПИТОНЕ:

Чтение в файл
a=open('name_file.txt', 'r')  - подключаем файл с именем name_file.txt (можно указывать полный путь вместо имени)
к программе , с помощью функции open(имя файла, r - указывает на то что открываем файл на прочтение)
s1=a.readline() - содержание превой строки из файла
s2=a.readline() - содержание второй строки из файла
a.close() - когда мы прочитали файл нужно закрыть файл

Этот Способ рекомендуется(более удобный)
with open('name_file.txt')  as a: - открывает файл name_file.txt, позволяет читать файл и сама закрывает файл
    s1=a.readline() - содержание первой строки из файла
    s2=a.readline() - содержание второй строки из файла
файл уже закрыт

Для чтение всех строк:
with open ('input.txt') as inf:
    for line in inf:
        line=line.strip()
        print(line)


s=a.readline().strip() - убирает служебные символы при чтении строки(\n,пробелы, табуляции)

os.path.join('.', 'dirname', 'filename.txt') - функция склеивает в один путь к файлу -'./dirname/filename.txt'
для этой функции нужно import os

Запись в файл
a=open('name_file.txt', 'w') - подключаем файл с именем name_file.txt (можно указывать полный путь вместо имени)
к программе , с помощью функции open(имя файла, w - указывает на то что открываем файл для записи)
a.write('Some text\n')  - для того что бы записать какую то строку - 'Some text\n', \n - нужно укзаывать что бы
строка была переведена на следующую
a.write(str(25)) - для того что бы вывести число нужно обязательно преобразовать в строку
a.close()

with open('name_file.txt', 'w')  as a: - открывает файл name_file.txt, позволяет записывать в файл и сама закрывает файл
    a.write('Some text\n')
    a.write(str(25)) - содержание второй строки из файла
файл уже закрыт

Обход файлов:

import os

path= 'C:\\Movies' - если слэш то двойной

def obxodFile(path,level=1)  - функция обхода элементов, в каждой папке, на каждом уровне
    print('Level=', level, 'Content:', os.listdir(path)) - выводит уровень папки, функция os.listdir() показывает содержимое указанного пути
    for i in os.listdir(path): - обходим все содержимое папки
        if os.path.isdir(path+'\\'+i): - если элемент папка
            print('Спускаемся', path+'\\'+i)
            #print(i, type(i),path+'\\'+i, os.path.isdir(path+'\\'+i)) - все названия файлов будут выводиться с типом "строка"; path+'\\'+i - это вывод пути файла вместе с самим файлом;
            #                                                           - os.path.isdir(path+'\\'+i)) -проверяет является ли элемент папкой по указанному пути - (path+'\\'+i) и выводит
            #                                                            True или False
            #                                                            - os.path.isfile(path+'\\'+i))  - аналогично проверяет является ли элемент файлом по указанному пути - (path+'\\'+i)
            #                                                            и выводит True или False
            obxodFile(path+'\\'+i,level+1)
            print('Возвращемся в', path)
obxodFile(path)

r   # Только для чтения.
w	# Только для записи. Создаст новый файл, если не найдет с указанным именем.
rb	# Только для чтения (бинарный).
wb	# Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
r+	# Для чтения и записи.
rb+	# Для чтения и записи (бинарный).
w+	# Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
wb+	# Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
a	# Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
a+	# Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
ab	# Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
ab+	# Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем.

https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod # полезная статья по работе с файлами