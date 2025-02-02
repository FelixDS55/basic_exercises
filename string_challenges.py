# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for element in word:
    if element.lower() == 'a':
        count += 1
print(count)

# Вывести количество гласных букв в слове
word = 'Архангельск'
vse_gls = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
count = 0
for el in word:
    if el.lower() in vse_gls:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*[i[0] for i in sentence.split()], sep='\n')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(sum([len(word) for word in words]) // len(words))