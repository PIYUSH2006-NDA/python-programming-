def wordwrite():
    word = input("Enter the word:\n")

    if len(word) > 3:
        word_list = list(word)
        first_char = word_list.pop(0)
        word_list.append(first_char)
        word_list.insert(-1, 'abc')
        word_list.insert(0, 'kbc')
        new_word = ''.join(word_list)
        print("Code word is:", new_word)
        return new_word
    else:
        reversed_word = word[::-1]
        print("Reversed word:", reversed_word)
        return reversed_word


def wordread(word):
    # Step 1: Remove 'kbc' from beginning (3 chars)
    if word.startswith('kbc'):
        word = word[3:]
    else:
        print("Invalid encoded word (missing 'kbc').")
        return

    # Step 2: Remove 'abc' which was inserted before the last character
    if 'abc' in word:
        idx = word.rfind('abc')
        word = word[:idx] + word[idx+3:]
    else:
        print("Invalid encoded word (missing 'abc').")
        return

    # Step 3: Move last character to the beginning
    word = word[-1] + word[:-1]

    print("Decoded word is:", word)


print("Enter your choice:\nPress 1 to write the message\nPress 2 to read the message")
m = int(input())

match m:
    case 1:
        encoded = wordwrite()
    case 2:
        encoded = input("Enter the encoded word:\n")
        wordread(encoded)
