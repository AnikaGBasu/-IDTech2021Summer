def reccurFibonacci(n):
  if n<=1:
    return n
  else:
    return reccurFibonacci(n-1)+reccurFibonacci(n-2)

nTerms = int(input("How long do you want the Fibonacci Sequence to go? "))

print()

if nTerms <= 0:
  print("We need a positive integer to work. Please enter again. ")
else:
  print("This is the Fibonacci Sequence: \n")
  for i in range(nTerms):
    #print("n =  " + str(i))
    print(2**reccurFibonacci(i))