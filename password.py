import string
import secrets
import pyperclip

def pass_gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

   return ''.join(secrets.choice(chars) for x in range(size))

result = pass_gen(10)

pyperclip .copy(result)
 
