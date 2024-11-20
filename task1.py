def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Handle uppercase letters
            start = ord('A') if char.isupper() else ord('a')
            offset = ord(char) - start
            if mode == 'encrypt':
                new_char = chr((offset + shift) % 26 + start)
            elif mode == 'decrypt':
                new_char = chr((offset - shift) % 26 + start)
            result.append(new_char)
        else:
            # Non-letter characters remain unchanged
            result.append(char)
    
    return ''.join(result)

def main():
    print("Caesar Cipher Encryption/Decryption")
    
    # Ask the user to input a message
    text = input("Enter the text: ")
    
    # Ask the user to input the shift value (an integer)
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Please enter a valid integer for the shift value.")
        return
    
    # Ask the user whether they want to encrypt or decrypt
    mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    
    # Ensure mode is valid
    if mode not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return
    
    # Determine the mode ('encrypt' or 'decrypt')
    mode = 'encrypt' if mode == 'e' else 'decrypt'
    
    # Perform the encryption or decryption
    result = caesar_cipher(text, shift, mode)
    
    # Display the result using the format method
    if mode == 'encrypt':
        print("Encrypted message: {}".format(result))
    else:
        print("Decrypted message: {}".format(result))

# Run the program
if __name__ == "__main__":
    main()
