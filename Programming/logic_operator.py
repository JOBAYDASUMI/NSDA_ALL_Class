num1 = 20
num2 = 47
num3 = 49

if num1 > num2 and num1 > num3:
    print(num1)
    
elif num2 > num1 and num2 > num3:
    print(num2)
    
else: 
    print(num3)
    
#vowel - a,e,i,o,u use OR

ch = 'b'
if ch == 'a' or ch == 'e' or ch =='i' or ch == 'o' or ch == 'u': #Any Condition is True then Result Is True
    print("Vowel")

else:
    print("Consonant")
    
    # Result Sheet ues And
marks = 85

if marks >= 80 and marks <=100:  # Both Condition is must be True Otherwisr its result is false
    print("A+")