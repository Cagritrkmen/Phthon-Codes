
import random

def sender():
    message = random.randint(1,100)
    return message

def is_prime(number):
    factor = 0
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                factor += 1
        if factor == 0:
            return True
        else:
            return False

def generate_prime():
    p = random.randint(100, 150)
    q = random.randint(100, 150)
    if is_prime(p) and is_prime(q) and p != q:
        return p, q
     
    else:
        while True:
            p = random.randint(100, 150)
            q = random.randint(100, 150)
            if is_prime(p) and is_prime(q) and p!=q:
                return p, q
def gcd(num1, num2):
    if num2 == 0:
        return num1
    elif num2 == 1:
        return 1
    else:
        return gcd(num2, num1 % num2)
    
p_and_q = generate_prime()
n = p_and_q[0] * p_and_q[1]
fi = (p_and_q[0] - 1) * (p_and_q[1] - 1)

e=0
def generate_public_key(e):
    if gcd(e, fi) != 1:
        while True:
            e = random.randint(1, fi)
            if gcd(e, fi) == 1:
                return e
    else:
        return e
#defining e 

e = generate_public_key(e)

def generate_private_key():
    for d in range(1, fi):
        if (d * e %fi ) == 1 % fi:
            return d
d=generate_private_key()

print("public key(n,e):", (n, e))
print("private key:(n,d):", (n, d))

def mc( a,b,n):
    _a=a%n
    _b=b%n
    if b==0:
        return 1
    while _b>1:
        _a = _a*a
        _a = _a%n
        _b=_b-1
    
    return _a
    

my_message=sender()    


def encrypting_message_func():
    return mc(my_message,e,n) 


def decrypting_message_func():
    return mc(encrypting_message_func
(),d,n)

print("our message:",my_message)
print("encrypting message:",encrypting_message_func())
print("solving message:",decrypting_message_func())





