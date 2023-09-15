# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))
print()

# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
vowels = 'аеёиоуыэюя'
count_vowels = 0
for i in word:
    if i in vowels:
        count_vowels +=1
print(count_vowels)
print()

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
print(len(list_sentence))
print()

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for word in list_sentence:
    print(word[0])
print()

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
avg_word = 0
for word in list_sentence:
    avg_word += len(word)
print(avg_word/len(list_sentence))