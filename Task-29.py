def reversed(variable):
    result=''
    for i in range(len(variable)-1,-1,-1):
        result+=variable[i]
    return result

string = reversed(input())
print(string)
