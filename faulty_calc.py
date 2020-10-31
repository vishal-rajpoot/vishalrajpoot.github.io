#                                          faulty calculator
#Design a calculator which will correctly solve all the problems except

# THESE ARE THE EXCEPTIONAL CASES IN THIS FAULTY CALC 56+9 = 77 , 45*3 = 555, 56/6 = 4
 
print("\t\t\t\twelcome to calculator: this is devloped by vishal rajput") # it is print on the screen
def calculator():
    operation=input("""\nplease type the operator which you wish to complete 

+ for addition
- for multiplication
* for multiplication
/ for division
** for power
% _for modulus

enter your operator : """) # it will take input as  an operator

    num1=int(input("enter first no: ")) # here enter the value of variable 1
    num2=int(input("enter second no: "))# here enter the value of variable 2
    if operation=='+':  # there are calculator oprations 
        if num1==56 and num2==9: # it will give a wrong output because it is a exceptional case
            print("77")
        else:
            print(num1+num2)# here addition of 2 no's will be performed
    elif operation=='-':
        print(num1-num2)# here subtraction of 2 no's will be performed
    elif operation =='*':
        if num1==45 and num2==3:  # it will give a wrong output because it is a exceptional case
            print("555")
        else:
            print(num1*num2)# here multiplication of 2 no's will be performed
    elif operation =='/':
        if num==56 and num2==6:  # it will give a wrong output because it is a exceptional case
            print("4")
        else:
            print(num1/num2)# here division of 2 no's will be performed
    elif operation =='**':
        print(num1**num2)# here power of 2 no's will be performed
    elif operation =='%':
        print(num1%num2)# here modulus of 2 no's will be performed
    else:
        print("you press an invalid operator")

    call=input("""\tDo you want to calculate again: 
    please type y for yes and n for no:  """) # this variable is used to calculate again
    if call == 'y':
        calculator()
    elif call =='n':
        print("see you later")
    else:
        print("you entered an invalid input")
calculator()

   
