#Danial Ganijee
#11/9/2024
#Personal Project 001
#Building a calculator

#How can I make this better?
#--Allow user to input calculation in one line of code
    #How would I convert parts of string to different floats/operators
#--Make code less redundant (there has to be a more efficient way)
#--Make the calculation follow the rules of PEMDAS
#--Goal for next project 
    #Learn more about python to make my code more efficient and capable
#-----------------------------------------------------------------
#Operator variables
import operator
add = operator.add
sub = operator.sub
mul = operator.mul
div = operator.truediv
frmt=f'{"":^19}' #formatting shortcut

#Title formatting
print(f'{"Ganijee Calculator":^40}') 
print("_"*40) 
print()
print(f'{"Instructions:":^40}') 
print(f'{"Input numbers and operators seperately.":^40}')
print(f'{"Operators: (/, *, +, -)":^40}')
print(f'{"Press enter when done inputting.":^40}')
print("_"*40)

#Empty tuple (mutable)
terms=[] #note: terms[0] and terms[1] are updated per new calculation


print()
term1=(input(frmt))
terms.append(term1)
operation=(input(frmt))
term2=(input(frmt))
terms.append(term2) #put term1 & term2 in list
while term2 and operation!="":
    #Assigning input to operations
    if operation[0]=="/":
        operation=div
    elif operation[0]=="*":
        operation=mul
    elif operation[0]=="+":
        operation=add
    elif operation[0]=="-":
        operation=sub
    if term1 and term2 ==0:
        term1=int(term1) #convert num 0 to int, otherwise error
        term2=int(term2)
    else:
        term1=float(term1)
        term2=float(term2)
    if operation==div and term2==0: #allows division by 0
        term1=0
    else:
        term1=operation(term1,term2) 
    terms[0]=term1 #updates term1 to calculated number
    operation=(input(frmt))
    if operation=="": #blank input triggers end
        print("-"*40)
        print(f'{"Total:":<13}{term1:10.3f}')
        print(f'\n{"Thanks for using my calculator!":^40}')
        exit()
    term2=(input(frmt)) #continues with calculation
    terms.append(term2)