user_word = input("Enter a word: ")
user_word = user_word.upper()

word_without_vowels = ""  # This will store only the non-vowel letters

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter  # Add the non-vowel letter to the result

print(word_without_vowels)