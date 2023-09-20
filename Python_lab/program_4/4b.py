def roman2int(roman):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman_back=list(roman)[::-1]
    value=0
    rightval=roman_dict[roman_back[0]]
    for numeral in roman_back:
        leftval=roman_dict[numeral]
        if leftval < rightval:
            value-=leftval
        else:
            value+=leftval
        rightval=leftval
    return value


roman=input("enter a roman number:")
res=roman2int(roman)
print("Integer equivalent of entered roman number is",res)