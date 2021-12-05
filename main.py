import string
from random import sample

letters = string.ascii_letters
digits = string.digits
punctutaion = string.punctuation
total = letters + digits + punctutaion

length = int(input("Length:"))
password = "".join(sample(total, length))

print("Password:",password)