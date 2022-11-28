########################################
#             MD Shekh Sadi            #
#        sadiewu12345@gmail.com        #
########################################

import random
# from random import randint  #It will save our memory



for x in range(5):
    number = int(input("Enter your number in between 1 to 10: "))

    randomNumber = random.randint(1,10)   #Here "random" is the package and "randint" is the function of "random" package. 
                                        # We can also use random function for big number e.g. random.random() * 34e89

    if(number==randomNumber):   
        print("You win\n\n")
    else:
        print("The actual number is: ",randomNumber,"and you lost\n\n")