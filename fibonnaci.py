import sys
def fib(i):
        if isinstance(i, int):
            x=0
            y=1
            HI=[]

            for b in range(i):
                HI.append(x)
                HI.append(y)
                x=x+y
                y=x+y
            return str(HI)[1:-1]



try:
    Input=int(sys.argv[1])
    print(fib(Input))
except:
    print("Input is not a int input")
    print("Input How Long The Sequence Should Be")
