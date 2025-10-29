import string
import argparse
import sys

def build_translation_table(key: int) -> dict:
    """
    Creates a translation table (a dictionary) for both upper and lowercase letters.
    The key determines how many steps to shift the alphabet.
    """
    
    # --- 1. Create lowercase table ---
    
    # Make sure the key is always between 0-25
    shift = key % 26
    
    # Original lowercase alphabet
    original_lower = string.ascii_lowercase
    # Shifted lowercase alphabet (e.g., 'defg...abc' if key=3)
    shifted_lower = original_lower[shift:] + original_lower[:shift]
    
    # Create the mapping: {'a': 'd', 'b': 'e', ...}
    lower_table = str.maketrans(original_lower, shifted_lower)
    
    # --- 2. Create uppercase table ---
    
    # Original uppercase alphabet
    original_upper = string.ascii_uppercase
    # Shifted uppercase alphabet (e.g., 'DEFG...ABC' if key=3)
    shifted_upper = original_upper[shift:] + original_upper[:shift]
    
    # Create the mapping: {'A': 'D', 'B': 'E', ...}
    upper_table = str.maketrans(original_upper, shifted_upper)
    
    # --- 3. Combine tables ---
    
    # Join the two tables together. 
    # Non-alphabetic characters (spaces, punctuation) will be ignored by translate().
    return {**lower_table, **upper_table}

def caesar_encrypt(message: str, key: int) -> str:
    """
    Encrypts a message using the Caesar cipher.
    It keeps the case (upper/lower) and any special characters.
    """
    
    # Get the correct mapping table for encryption
    cipher_table = build_translation_table(key)
    
    # Translate the message using the table. 
    # Characters not in the table (like ' ') are kept as they are.
    encrypted_message = message.translate(cipher_table)
    
    return encrypted_message

def caesar_decrypt(encrypted_message: str, key: int) -> str:
    """
    Decrypts a message from the Caesar cipher.
    The key must be the same one used to encrypt.
    """
    
    # To decrypt, we just shift in the opposite direction.
    # If we encrypted with key 3, we decrypt with key (26 - 3) = 23.
    decrypt_key = 26 - (key % 26)
    
    # Get the mapping table for decryption
    decrypt_table = build_translation_table(decrypt_key)
    
    # Translate the message back to its original form
    message = encrypted_message.translate(decrypt_table)
    
    return message

def main():
    """Sets up the command-line tool to run the cipher."""
    
    parser = argparse.ArgumentParser(
        description="Encrypt or Decrypt text using the Caesar Cipher.",
        epilog="Example: python caesar_cipher.py -k 3 -e \"Hello World\""
    )
    
    # Argument for the Key (required, must be a number)
    parser.add_argument(
        "-k", "--key", 
        type=int, 
        required=True, 
        help="The shift key (a number, e.g., 3)"
    )
    
    # --- Create a group for Encrypt OR Decrypt ---
    # This makes sure the user can only choose one option at a time.
    mode_group = parser.add_mutually_exclusive_group(required=True)
    
    mode_group.add_argument(
        "-e", "--encrypt", 
        dest="message", # Store the input text in 'message' variable
        help="The message to ENCRYPT."
    )
    
    mode_group.add_argument(
        "-d", "--decrypt", 
        dest="encrypted_message", # Store the input text in 'encrypted_message'
        help="The message to DECRYPT."
    )
    
    args = parser.parse_args()
    
    # --- Run the correct function based on user's choice ---
    if args.message:
        # User chose to encrypt
        result = caesar_encrypt(args.message, args.key)
        print(f"\nMessage:   {args.message}")
        print(f"Key:       {args.key}")
        print(f"Encrypted: {result}")
        
    elif args.encrypted_message:
        # User chose to decrypt
        result = caesar_decrypt(args.encrypted_message, args.key)
        print(f"\nEncrypted: {args.encrypted_message}")
        print(f"Key:       {args.key}")
        print(f"Decrypted: {result}")

if __name__ == "__main__":
    main()