print("ceasar cipher")



def user_input():
    code = " "
    i = 0
    code = input("enter the code to encrypt:")
    code_len = len(code)
    for i in range(code_len):
        code_new = i
        encryption(code_new)

    


user_input()


def encryption(code_new):
    
    encrypt_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i = 0
    if code_new.islower():
        pass
    else:
        lower_case_code = code_new.lower()
    
    for i in range(encrypt_list):
        if encrypt_list[i] == lower_case_code:
            print(i)
            i+=1

    



# def decryption():
    