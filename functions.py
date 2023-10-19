
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def generate_key_sequence(alphabet, key, k):
    # Remove all key characters from the alphabet
    for c in key:
        alphabet = alphabet.replace(c, "")

    # Get a substring from the alphabet starting from position k
    remaining_alphabet = alphabet[k + len(key):]

    # Connect the key and the remaining alphabet
    result = remaining_alphabet + key + alphabet[:len(alphabet) - len(remaining_alphabet)]

    return result

def change_alphabet(input_text, alphabet, new_alphabet):
    encrypted_text = []

    for c in input_text.upper():
        index = alphabet.find(c)
        if index != -1:
            encrypted_text.append(new_alphabet[index])
        else:
            # If a character is not found in the original alphabet, leave it unchanged
            encrypted_text.append(c)

    return "".join(encrypted_text)

def enchip(text, key):
    k = 5 # by default, but if it needs we can add random (0,25)
    enchipher_alphabet = generate_key_sequence(alphabet, key.upper(), k)
    encrypted_text = change_alphabet(text, alphabet, enchipher_alphabet)
    return encrypted_text

def dechip(encrypted_text, key):
    k = 5 # by default, but if it needs we can add random (0,25)
    enchipher_alphabet = generate_key_sequence(alphabet, key.upper(), k)
    decrypted_text = change_alphabet(encrypted_text, enchipher_alphabet, alphabet)
    return decrypted_text

# ==============
# Vizionaire's part

def create_vigenere_table():
    table = [''] * 26  # Assuming you're using a standard 26-letter alphabet

    for i in range(26):
        table[i] = alphabet[i:] + alphabet[:i]

    return table


#  Vizionaire funcs

def create_key_vigenere(input_message, key):
    key = key.upper()  # Ensure the key is in uppercase
    input_message = input_message.upper()
    chars = list(input_message)
    key_length = len(key)
    key = key * (len(chars) // key_length) + key[:len(chars) % key_length]

    return ''.join(key)


def vigenere(input_message, key):
    table = create_vigenere_table()
    new_key = create_key_vigenere(input_message, key)

    chars = list(input_message.upper())
    output_message = [''] * len(chars)

    for i in range(len(chars)):
        if chars[i].isalpha():
            table_row = table[alphabet.index(new_key[i])]
            output_message[i] = table_row[alphabet.index(chars[i])]
        else:
            output_message[i] = chars[i]

    return ''.join(output_message)


def de_key_vigenere(input_message, key):
    table = create_vigenere_table()
    new_key = create_key_vigenere(input_message, key)

    chars = list(input_message)
    output_message = [''] * len(chars)

    for i in range(len(chars)):
        if chars[i].isalpha():
            table_row = table[alphabet.index(new_key[i])]
            output_message[i] = alphabet[table_row.index(chars[i])]
        else:
            output_message[i] = chars[i]

    return ''.join(output_message)


input_message = "ATTACKATDawn"
key = "LEMON"
result = vigenere(input_message, key)
print(result)

decrypted_message = de_key_vigenere(result, key)
print(decrypted_message)


