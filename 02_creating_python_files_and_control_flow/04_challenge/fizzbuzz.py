# ここにコードを書いてください
for x in range(1,101):
    if (x % 3 ==0 and x % 5 == 0):#3と5の公倍数の場合は `FizzBuzz`
        print("FizzBuzz")
    
    elif (x % 5 == 0):#5の倍数の場合は `Buzz`
        print("Buzz")
        
    elif (x % 3 ==0):#3の倍数の場合は数字の代わりに `Fizz`
        print("Fizz")
    
    else:
        print(x)
    
     