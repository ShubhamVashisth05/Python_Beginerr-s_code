import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gen_pass():
    pass_len = int(input("Length of password? "))

    random.shuffle(characters)
    password =[]

    for x in range(pass_len):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(password)

gen_pass()