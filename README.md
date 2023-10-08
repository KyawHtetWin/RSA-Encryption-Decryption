# RSA Encryption and Decryption Program

## Overview
This repository contains Python programs, `encryption.py` and `decryption.py`, demonstrating RSA (Rivest–Shamir–Adleman) encryption and decryption algorithms. RSA is a widely used asymmetric encryption algorithm providing secure data transmission by utilizing public and private keys.

## Encryption Program (encryption.py)

### Features
- **User Input:** Takes a string message from the user for encryption.
- **Customizable Keys:** Allows users to set values for p, q, n, and e.
- **Output:** Generates a string of encrypted integers.

#### Usage
1. Run `encryption.py`.
2. Input a message.
3. The program encrypts the message and displays the encrypted integers.

#### Example
**Input (Message):** `"HELLO"`
**Output (Encrypted Integers):** `3119269210213100020132321831902190321323220190132512825`

## Decryption Program (decryption.py)

### Features
- **User Input:** Takes a string of integers to decrypt.
- **Inverse Modulo Function:** Finds the inverse modulo as required in RSA.
- **Output:** Generates the decrypted message.

#### Usage
1. Run `decryption.py`.
2. Input a string of encrypted integers.
3. The program decrypts the integers and displays the original message.

#### Example
**Input (Encrypted Integers):** `3119269210213100020132321831902190321323220190132512825`
**Output (Decrypted Message):** `"HELLO"`

## Dependencies
- Standard Python libraries, no external dependencies required.

