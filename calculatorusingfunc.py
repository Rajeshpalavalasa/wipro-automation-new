#Calculator

def calculator(a,b,op):

    for event in range(1,3):
        if op=="division" or op=="/":
            if b!=0:
                return a/b
            else:
                return 'Error cant be divide by 0'
        elif op=="multiplication" or op=="*":
            return a*b
        elif op=="Addition" or op=="+":
            return a+b
        elif op=="sub" or op=="-":
            return a-b
        else:
            return "inavlid operation"




#Calculate Speed
def speed(d,t):
    return d/t
