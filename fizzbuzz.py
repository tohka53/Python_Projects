count = 0
for count in range (0,100):  
    count= count+1
    print(count)
    if count%15==0:
        print('FizzBuzz')
    elif count % 3 ==0:
        print('Fizz')
    elif count %5 ==0:
        print('Buzz')
    else:
        print(count)
   
    

    