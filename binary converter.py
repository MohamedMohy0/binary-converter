order=int(input("convert from binary(1) or convert to binary(2)"))
if order==2:
    x=str(input("enter the characters:"))
    binary =' '.join(format(ord(y), 'b') for y in x)
    print(binary)
elif order==1:

    Ascii=str(input("enter the binary num:"))
    string="".join([chr(int(binary, 2)) for binary in Ascii.split(" ")])
    print(string)