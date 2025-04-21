from Crypto.Cipher import AES
import base64

# Base64-decoded keys add your keys here
k1 = base64.b64decode("")
k2 = base64.b64decode("")
k3 = base64.b64decode("")

# Long ciphertext (base64-decoded)
b64_ciphertext = ""
ciphertext = base64.b64decode(b64_ciphertext.strip())

# AES helpers
def aes_decrypt_block(key, block):
    return AES.new(key, AES.MODE_ECB).decrypt(block)

def aes_encrypt_block(key, block):
    return AES.new(key, AES.MODE_ECB).encrypt(block)

# Split into 16-byte blocks
def process_blocks(ciphertext, k1, k2, k3):
    plaintext = b''
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        # Ensure block is 16 bytes
        if len(block) < 16:
            continue  # or pad if necessary
        step1 = aes_decrypt_block(k3, block)
        step2 = aes_encrypt_block(k2, step1)
        plain = aes_decrypt_block(k1, step2)
        plaintext += plain
    return plaintext

pt = process_blocks(ciphertext, k1, k2, k3)
print(pt)
