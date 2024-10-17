# открываем файл text.txt в режиме чтения
with open("text.txt", "r", encoding = "utf-8") as file:
    # читаем содержание файла
    text = file.read()
#разделяем текст на слова, используя пробел и перевод строки в качестве разделителей
words = text.split()
# подсчитываем количество слов
word_count = len(words)
# выводим количество слов в файле
print(f"Количество слов в файле: {word_count}") 