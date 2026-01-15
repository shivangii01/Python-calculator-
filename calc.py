# PYTHON PROGRAM TO CREATE SIMPLE CALCULATOR
print("BASIC CALCULATOR :")
print("Please select an operation to perform:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

choice = int(input("Select a operation from 1,2,3,4,5: ")) 

n=int(input("Number of values you are going to enter?"))
values=[]
for i in range (n):
    num=eval(input("enter the value:"))
    values.append(num)
if choice==1:
    result=0
    for num in values:
        result+=num
    print("RESULT:",result)
elif choice==2:
    result=values[0]
    for num in values[1:]:
        result-=num
    print("RESULT:",result)
elif choice==3:
    result=1
    for num in values:
        result*=num
    print("RESULT:",result)
elif choice==4:
    result=values[0]
    for num in values[1:]:
        if num == 0:
            print("Error! Division by zero.")
            break
        result/=num
    else:
        print("RESULT:",result)
elif choice==5:
    result=values[0]
    for num in values:
     result+=num
     result/n
    print("RESULT:",result)
else:
    print("Invalid choice!!")






