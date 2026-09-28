import random

lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%&*'"
numbers = '1234567890'

password_kit = lower_alphabets + upper_alphabets + symbols + numbers
password_generator = "".join(random.sample(password_kit, k=12))

print(password_generator)