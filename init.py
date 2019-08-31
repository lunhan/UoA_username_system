import random
def main():
    systitle = title()
    print(systitle)
    print()
    full_name = input_name()
    generate_num = num_sys()
    username = generate_username(full_name, generate_num)
    print("Your username is:", username)
    print("Your e-mail address is:", username + "@aucklanduni.ac.nz")
    print("Your username and e-mail could be using for login Canvas, Student Service Online(SSO) and open disktop in University")

def title():
    word = "Welcom to University of Auckland Username System"
    return word

def input_name():
    print("While when you enter your name, please using one space to devide your surename and forename.")
    name = input("Please Enter Your Name: ")
    name = name.lower()
    return name

def num_sys():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    num3 = random.randrange(1, 10)
    full_num = str(num1) + str(num2) + str(num3)
    return full_num

def generate_username(name, num):
    space = name.find(" ")
    first_part = name[0]
    second_part = name[space+1 : space+4]
    name_part = first_part + second_part
    username = name_part + num
    return username

main()
