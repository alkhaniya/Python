s = "aditya.alkhaniya@gmail.com"

def getDomain(email):
    return email.split('@')[1]

print(getDomain(s)) 
