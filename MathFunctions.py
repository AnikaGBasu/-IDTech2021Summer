class MathFunctions:
    def menu(self):
        options = input("There are multiple different commands that you can use in this calculator. \n" +
                              "Type 's' for sum, 'd' for difference, 'p' for product, 'q' for quotient \n" +
                              "'f' for factorial, and 'quit' to quit the program.")
        print(options)
'''
        while options != "quit":
            options = input("There are multiple different commands that you can use in this calculator. \n" +
                            "Type 's' for sum, 'sum of d' for sum of digits, 'd' for difference, 'p' for product \n" +
                            "'q' for quotient, 'f' for factorial, and 'quit' to quit the program.")
            if options == "s":
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter another number: "))
                self.addition(num1, num2)
            elif options == "sum of d":
                num = int(input("Enter a number: "))
                self.sumDigits(num)
            elif options == "d":
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter another number: "))
                self.subtraction(num1, num2)
            elif options == "p":
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter another number: "))
                self.multiplication(num1, num2)
            elif options == "q":
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter another number: "))
                self.division(num1, num2)
            elif options == "f":
                num = int(input("Enter a number: "))
                self.factorial(num)
            elif options == "m":
                userList = []
                lengthList = int(input("How many numbers do you want in your list? "))
                for i in range(lengthList):
                    newNum = int(input("Enter a number to add to your list: "))
                    userList.append(newNum)
                self.minMax(userList)
                pass
            else:
                self.menu()
            #Sum, difference, product, quotient, factorial, min/max, quit

    def addition(self, num1, num2):
        sum = num1 + num2
        print(str(sum))

    def sumDigits(self, num): #when I'm calling it, it will be a string
        digitSum = 0
        for i in range(len(num)):
            digitSum = digitSum + int(num[i])
        print(str(digitSum))

    def subtraction(self, num1, num2):
        difference = num1 - num2
        print(str(difference))

    def multiplication(self, num1, num2):
        product = num1 * num2
        print(str(product))

    def division(self, num1, num2):
        quotient = num1 / num2
        print(str(quotient))

    def factorial(self, num1):
        for i in range(num1):
            factorialNum = 1
            factorialNum = factorialNum * i
        print(str(factorialNum))

    def minMax(self, userList):
        min = userList[0]
        max = userList[0]
        for i in userList:
            if i > max:
                max = i
            elif i < min:
                min = i
        print(str(min))
        print(str(max))
'''

myInstance = MathFunctions()
myInstance.menu()
