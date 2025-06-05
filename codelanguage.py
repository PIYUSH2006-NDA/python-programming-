
word = input("Enter the word:\n")

if len(word) > 3:
    word_list = list(word)                # Convert to list
    first_char = word_list.pop(0)         # Remove first character
    word_list.append(first_char)          # Append first character to the end
    word_list.insert(-1, "abc")
    word_list.insert(0, "kbc")
    new_word = ''.join(word_list)
    print("Modified word:", new_word)

else:
    reversed_word = reversed(word)
    print("Reversed word:", reversed_word)
