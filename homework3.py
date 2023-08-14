input_string = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

length = len(input_string)
print(f"Довжина рядка: {length} символів")

words = input_string.split()
num_words = len(words)
print(f"Кількість слів: {num_words} слова")

vowels = "аеиіоуюяєї"
modified_words = []
for word in words:
    modified_word = ""
    for letter in word:
        if letter.lower() in vowels:
            modified_word += "#"
        else:
            modified_word += letter
    modified_words.append(modified_word)

print("Модифіковані слова:", modified_words)

restored_string = " ".join(modified_words)
print("Відновлений рядок:", restored_string)
