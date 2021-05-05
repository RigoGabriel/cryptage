from hashlib import sha256
enter = input("enter the name of the file to crypt: ")
exit = input("enter the name of the final file: ")
key = input("enter the key: ")
keys = sha256(key.encode('utf8')).digest()
with open(enter, "rb") as f_enter:
    with open(exit, "wb") as f_exit:
        i = 0
        while f_enter.peek():
            c = ord(f_enter.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_exit.write(b)
            i += 1
