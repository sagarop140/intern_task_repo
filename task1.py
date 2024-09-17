def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Iterate over each character in the input text
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                # Shift character and wrap around if needed
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

# Get user input for text and shift value
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Choose mode (encryption or decryption)
mode = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

# Perform Caesar Cipher operation
output = caesar_cipher(message, shift_value, mode)

print(f"\nThe {mode}ed message is: {output}")
