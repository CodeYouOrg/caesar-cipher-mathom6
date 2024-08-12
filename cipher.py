letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text):
    cipher_text=''
    for char in text:
        if char in letters:
            position = letters.index(char)
            new_position = (position - 5)
            cipher_text += letters[new_position]
        else:
            cipher_text += char
    print(f"Your encrypted message: {cipher_text}")

message = input("Enter a message to encrypt: ")
text = message.lower()
encryption(text)