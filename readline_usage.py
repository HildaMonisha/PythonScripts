var=open('testtxt')
#print(var.read())
#print(var.readline())
#var.close()


#var1=var.readline()
#while var1 != "":
#    print(var1)
#    var1=var.readline()

print("*****")
for var2 in var.readlines():
    print(var2)
var.close()