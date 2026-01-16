# 🔐 Simple Message Encrypter

Simple Message Encrypter is a Python-based program that encrypts and decrypts
messages using a basic substitution cipher.

It is designed to demonstrate how encryption and decryption work at a conceptual level,
not to provide real-world cryptographic security.

---

## Overview

Encryption is all about transforming readable data into something unreadable,
and decryption is about reversing that transformation.

This tool uses:
- A predefined set of characters
- A randomly shuffled key
- Character-by-character substitution

The same logic is used to encrypt and then decrypt the message.

---

## Features

- Encrypts user-provided messages
- Decrypts the encrypted output back to original text
- Uses a randomized substitution key
- Supports letters, digits, punctuation, and spaces
- Simple and beginner-friendly logic

---

## How It Works

The program creates two character lists:
- One original character set
- One shuffled version of the same set (the key)

For encryption:
- Each character in the message is replaced with its shuffled counterpart

For decryption:
- The process is reversed using the same key

This ensures that encryption and decryption are perfectly reversible.

---

## Usage

Run the program  
python message_encrypter.py  

Enter a message when prompted.
The program will display:
- The encrypted message
- The decrypted original message

---

## Important Notes

- The encryption key is generated at runtime
- Restarting the program generates a new key
- Encrypted messages cannot be decrypted across sessions
- This is not cryptographically secure encryption

---

## Learning Value

This project helps understand:
- Substitution ciphers
- Encryption vs decryption logic
- Character mapping
- Why key management matters

---

## Final Thoughts

Real encryption is complex.
This tool keeps things simple so the concept is easy to understand.
If you understand this,
you understand the foundation of how data can be transformed securely.
