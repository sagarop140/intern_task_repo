from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    try:
        img = Image.open(input_image_path)
        img = Image.eval(img, lambda x: (x + key) % 256)
        img.save(output_image_path)
        print(f"Image encrypted and saved to {output_image_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_image_path, output_image_path, key):
    try:
        img = Image.open(input_image_path)
        img = Image.eval(img, lambda x: (x - key) % 256)
        img.save(output_image_path)
        print(f"Image decrypted and saved to {output_image_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Get user input
    action = input("Do you want to 'encrypt' or 'decrypt' the image? ").strip().lower()
    input_image_path = input("Enter the path to the input image: ").strip().strip('"')
    output_image_path = input("Enter the path to save the output image: ").strip().strip('"')
    key = int(input("Enter the key value for encryption/decryption (a number): ").strip())

    if action not in ['encrypt', 'decrypt']:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        return
    
    if action == 'encrypt':
        encrypt_image(input_image_path, output_image_path, key)
    elif action == 'decrypt':
        decrypt_image(input_image_path, output_image_path, key)

if __name__ == "__main__":
    main()
