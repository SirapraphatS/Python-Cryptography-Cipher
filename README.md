# Cryptography Cipher Tool

This is a simple, Python tool for encrypting and decrypting messages using the **Caesar Cipher**.

---

## Key Features

* **Handles All Letters:** Works correctly with both uppercase (A-Z) and lowercase (a-z) letters.
* **Keeps Punctuation:** It does not change spaces, punctuation (`!`, `?`), or numbers.
* **Command-Line Tool:** Uses `argparse` so you can run it easily from your terminal.
* **Clear Code:** Written in a simple way that is easy to read and understand.

---

## Prerequisites

1.  **Python 3.x**
    *(No special libraries are needed. `string` and `argparse` are included with Python.)*

## How to Use It (Usage Examples)

You can run this script directly from your terminal. You must provide a **key** (a number) and choose a **mode** (encrypt `-e` or decrypt `-d`).

### 1. To Encrypt a Message

Use the `-k` (key) and `-e` (encrypt) flags.

```bash
python caesar_cipher.py -k 3 -e "Hello World!"
```

Output:

```bash
Message:   Hello World!
Key:       3
Encrypted: Khoor Zruog!
```

### 2. To Decrypt a Message

Use the same -k (key) you used to encrypt and the -d (decrypt) flag.

```Bash
python caesar_cipher.py -k 3 -d "Khoor Zruog!"
```
Output:

```Bash
Encrypted: Khoor Zruog!
Key:       3
Decrypted: Hello World!
```

---

## Credits

The foundational concept and initial code structure for this Caesar Cipher was inspired by the excellent cybersecurity tutorials provided by W J Pearce. This project expanded that code with new features like case-preserving translation and a full command-line interface.

---

## License

This project uses the MIT License. (See the LICENSE file for full details.)

