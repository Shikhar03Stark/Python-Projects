#we know from the fact that every prime number is of form 6m +- 1 after 2 and 3
#also number of prime factors run out after reaching sqrt(number)
#prime_set contains all values of 6m +- 1
import time
#Limiting value of this program is 9Billion numbers within the range(50,000)
while True:
    print('Enter values greater than 10,000 or else use normal PrimeGenerator.py \n')
    lower = int(input('Enter lower limit: '))
    upper = int(input('Enter upper limit: '))
    t1 = time.time()
    for i in range(lower, upper+1):
        if(i % 6 == 1 or i % 6 == 5):
            for iter in range(2,int(i**0.5)):
                if(i%iter == 0):
                    break
            else:
                print(i,end='\n')
    t2 = time.time()
    print('Time Elapsed in Execution: '+str(t2 - t1)+' s')
