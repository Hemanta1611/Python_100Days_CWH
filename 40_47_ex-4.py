import getpass

line = getpass.getpass("Write some thing as a line: ")
new_line = line.split()
encrypted_line = ""

for word in new_line:
    if(len(word) > 3):
        word = word[1:] + word[0]
        encrypted_line = encrypted_line + " " + word
    else:
        word = word[::-1]
        encrypted_line = encrypted_line + " " + word


print("Encrypted Code:", encrypted_line)

decrypted_line = ""
for words in encrypted_line.split():
    if(len(words) > 3):
        words = words[len(words) - 1:] + words[:len(words) - 1]
        decrypted_line = decrypted_line + " " + words
    else:
        words = words[::-1]
        decrypted_line = decrypted_line + " " + words

print("Decrypted Code:", decrypted_line)