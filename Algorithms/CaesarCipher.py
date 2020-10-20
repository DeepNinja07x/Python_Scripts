def caesar_cipher(message_to_encrypt: str, key: int, encrypt_direction: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ"
    result = ""

    for character in message_to_encrypt:
        # returns the position of the chara"cter in alphabet array
        position = alphabet.find(character)
        if position == -1:
            # character not found
            result += character
        else:
            if encrypt_direction == "backward":
                # if backward direction return 1 position in alphabet array
                new_position = position - key
            elif encrypt_direction == "forward":
                # if forward direction advance 1 position in alphabet array
                new_position = position + key
                result += alphabet[new_position: new_position+1]
    return result

if __name__ == "__main__":
    message_to_encrypt = input("insert the message you want to encrypt: ")
    key = int(input("insert the key you want to encrypt your text: "))
    mode = input("insert the direction of the cipher: (backward) or (forward) ")

    print(caesar_cipher(message_to_encrypt, key, mode))
