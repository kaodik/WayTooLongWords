
arr = []
words = int(input())
count = 0
def printWTLW(n):
    global count
    while(count <n):
        inp = input()
        length = int(len(inp)-2)
        if(10 < int(len(inp))):
            arr.insert(count, inp[0]+str(length)+inp[-1])
        else:
            arr.insert(count, inp)

        count+=1
    for x in arr:
        print(x)

if __name__ == '__main__':
    printWTLW(words)
