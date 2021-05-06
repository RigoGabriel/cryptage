def code_vigenere(enter, exit, k, decode = False):
    key = k.upper()
    len_key = len(key)
    with open(enter, "r") as f_enter:
        with open(exit, "w") as f_exit:
            i = 0
            while 1:
                c = f_enter.read(1)
                if not c: break
                if (c.isalpha()):
                    tab_i = ord(key[i % len_key]) - 65
                    if decode: tab_i = 26 - tab_i
                    code = chr((ord(c.upper()) - 65 + tab_i) % 26 + 65)
                    f_exit.write(code)
                    i += 1
                if (c == " "):
                    f_exit.write(' ')

def decode_vigenere(enter, exit, key):
    code_vigenere(enter, exit, key, True)

usage = input("yould you want to code or decode: ")
enter = input("enter the name of the file to code: ")
exit = input("enter the name of the final file: ")
key = input("enter the key: ")
if usage == "code":
    code_vigenere(enter, exit, key)
elif usage == "decode":
    decode_vigenere(enter, exit, key)
else:
    print("Usage: for encode type code,\n       and for decode type decode.")
