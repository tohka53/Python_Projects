#PASSWORD GENERATOR


import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="0123456789"
symbols =".#$%&/!@"


use_for = lower_case+ upper_case + number + symbols 
password_text = 8

password = "".join(random.sample(use_for,password_text) )

print(password)
