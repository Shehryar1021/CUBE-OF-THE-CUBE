def cube(number):

 return number*number*number
#define a number will execute cube function if the user entered the number
is divisible by 3
def by_three(number):
 if number %3 ==0:
  return cube(number)
 else: 
  return FALSE
 #display result
print(by_three(9))
print(by_three(4))