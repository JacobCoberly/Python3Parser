def myFunc(var1, var2):
    if var1 > var2:
        return var1
    else:
        return var2

def main():
    var1 = "abc"
    var2 = 4
    for i in range(0,10):
        var2 += i
        print(myFunc(var1, var2+1))

main()
