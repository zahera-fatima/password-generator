import string
import random
n = int(input())
chars = string.ascii_letters + string.digits + string.punctuation
passw = "".join(random.choice(chars) for x in range(n))
print(passw)