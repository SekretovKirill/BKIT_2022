



if __name__ == "__main__":
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


    #без использования лямбда функции
    result=sorted(data,key=abs,reverse=True)
    print(result)


    #с использованием лямбда функции
    result=sorted(data,key = lambda x: abs(x),reverse=True)
    print(result)