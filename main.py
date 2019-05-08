# Get input from user 
num = int(input('input for prime or not prime :'))
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print('prime')
