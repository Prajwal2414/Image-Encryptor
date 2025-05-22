from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and save a key for encryption/decryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key saved to secret.key")

def load_key():
    """Load the encryption key from file."""
    return open("secret.key", "rb").read()

def encrypt_image(image_path, encrypted_path):
    """Encrypt an image and save it as a new file."""
    key = load_key()
    cipher = Fernet(key)
    
    with open("D:\pinnacle\input.jpg", "rb") as file:
        image_data = file.read()
    
    encrypted_data = cipher.encrypt(image_data)
    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)
    print(f"Encrypted image saved as {encrypted_path}")

def decrypt_image(encrypted_path, decrypted_path):
    """Decrypt an image and restore it."""
    key = load_key()
    cipher = Fernet(key)
    
    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)
    print(f"Decrypted image saved as {decrypted_path}")

# Example usage
generate_key()  # Run once to generate the key
encrypt_image("D:\pinnacle\input.jpg", "encrypted.enc")
decrypt_image("encrypted.enc", "decrypted.jpg")