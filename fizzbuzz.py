RANGE = 100
for i in range(1,RANGE+1):
   a = ""
   if i%3==0:
       a += "Fizz"
   if i%5==0:
       a += "Buzz"
   print a or i
