print("Caesar Cipher")
print("-------------")

def input_plain_text():
    code = input("enter the plaintext for encryption: ")
    key = int(input("enter key: "))
    print(code, key)
    encryption(code, key)
    


def encryption(code, key):
    encrypted_text = []
    print(code, key)
    Lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for str in code:
        if str.isupper():
            str_lower = str.lower()
            
            str = str_lower
            
            # if str_lower in Lowercase_letters:
            #     index = Lowercase_letters.index(str_lower)
            #     print(Lowercase_letters[index+key])
                
        else:
            if str in Lowercase_letters:
                index = Lowercase_letters.index(str)
                encrypted_text.append(Lowercase_letters[index+key])
    
    print("plain text:", code)
    print("encrypted text:", encrypted_text)
                
            
        
input_plain_text()