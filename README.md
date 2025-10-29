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

    Python 3.x
    (No special libraries are needed. `string` and `argparse` are included with Python.)

---

This project uses only built-in Python libraries, so no installation is needed.

Just clone the repository, go into the folder, and run the script. You can copy and paste all the commands below at once:

### 1. Clone the repository 

```bash
git clone https://github.com/YourUsername/Your-Repo-Name.git
```

### 2. Go into the newly created folder

```bash
cd Your-Repo-Name
```

### 3. That's it! You are ready.


### Run the line below to see how to use the tool.

```bash
echo "Setup complete! Run the --help command to see options:"
python caesar_cipher.py --help
```
## Examples

### 1. To Encrypt a Message

Use the `-k` (key) and `-e` (encrypt) flags.

Input :

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

Input :

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

