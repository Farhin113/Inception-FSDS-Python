# """
# Exercise -1
# Find the minimun number from 3 given number
# """

# Num1 = int(input("Enter the First num: "))
# Num2 = int(input("Enter the second num: "))
# Num3 = int(input("Enter the Third num: "))

# if Num1<Num2 and Num1<Num3:
#     print("The minimum number:" ,Num1)


# elif Num2<Num1 and Num2<Num3:
#     print("The minimum number:" ,Num2)

# else:
#     print("The minimum number:" ,Num3)


"""
Exercise -2
1.pin change
2.Blance cheak
3.Whitdrow
4.Deposet
5.Exit
"""

manu =input("""
Hi there!wellcame to ATM 
please chose
1.Enter 1 for pin change
2.Enter 2 for Blance cheak
3.Enter 3 for Whitdrow
4.Enter 4 for Deposet
5.Exit                       
""")
 
if manu=="1":
   print("pin change")

elif manu=="2":
   print("Blance cheak")

elif manu=="3":
    print("Whitdrow")    

elif manu=="4":
    print("Deposet") 

else:
    print("Exit")   