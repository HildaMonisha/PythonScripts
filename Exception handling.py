cart=0
if cart !=2: #raise Exception("cart doesnt match")
    pass

assert(cart!=2)

#try and except
try:
    with open('testttt','r') as var:
        print(var.read())
except Exception as a:
    print(a)
finally:
    print("end of test")
