def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabetic characters are not encrypted
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)  # Decryption is just encryption with the negative shift

def main():
    print("Caesar Cipher Program")
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_message = caesar_cipher_encrypt(message, shift)
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
