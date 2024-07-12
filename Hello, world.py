if __name__ == '__main__':
    n = int(input("Please input a number: "))
    if 1<= n <= 150:
        x = str()
        n +=1
        for i in range(1, n):
            x += str(i)
        print(x)