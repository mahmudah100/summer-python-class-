# Vigenère Cipher (Encryption & Decryption)

This project demonstrates how to use the **Vigenère Cipher**, a method of encrypting and decrypting text using a repeating key.

---

## 🔑 How the Code Works

### 1. Inputs
- `text`: The message to encrypt or decrypt.
- `custom_key`: The secret key used for shifting letters.

Example:
```python
text = "mrttaqrhknsw ih puggrur"
custom_key = "happycoding"
```

---

### 2. Vigenère Cipher Function

```python
def vigenere(message, key, direction=1):
```
- `message`: The text to encrypt or decrypt.
- `key`: The secret word used for shifting.
- `direction`: 
  - `1` → **Encrypt**
  - `-1` → **Decrypt**

#### Steps inside the function:
1. Loop through each character in the message.
2. If it’s **not a letter** (like spaces or punctuation), keep it unchanged.
3. If it’s a letter:
   - Match it with a character in the key (repeating as needed).
   - Find the **shift amount** from the key character.
   - Shift the message character forward (encryption) or backward (decryption).
   - Add the new character to the result.

---

### 3. Encrypt Function
```python
def encrypt(message, key):
    return vigenere(message, key)
```
Encrypts the message using the Vigenère cipher.

### 4. Decrypt Function
```python
def decrypt(message, key):
    return vigenere(message, key, -1)
```
Decrypts the message by reversing the shift.

---

## 🛠️ Usage Example

```python
text = "mrttaqrhknsw ih puggrur"
key = "happycoding"

print("Encrypted text:", text)
print("Key:", key)

# Decrypting
decrypted = decrypt(text, key)
print("Decrypted text:", decrypted)

# Encrypting
new_message = "secret message"
encrypted = encrypt(new_message, key)
print("Encrypted again:", encrypted)
```
---

## ✅ Output Example

```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding
Decrypted text: programming is awesome
Encrypted again: zocjsb epqbdjb
```

---

## 📌 Notes
- Works only with **lowercase letters** (a–z).
- Non-alphabet characters (spaces, punctuation) are preserved.
- Key must be **letters only**.

