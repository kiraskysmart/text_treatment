text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

char_frequency = {}
longest_word = words[0]
shortest_word = words[0]

for word in words:
    # Поиск самого длинного и самого короткого слова
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word

# Подсчет частоты использования символов
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Количество разных слов:", len(set(words)))
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)

print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")