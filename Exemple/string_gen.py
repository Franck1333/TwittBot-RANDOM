#Aides : https://www.pythoncentral.io/python-snippets-how-to-generate-random-string/

import string
from random import *

min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

print ("This is your password : ",password)
