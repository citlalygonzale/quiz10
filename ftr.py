def find_threes(l):
    sum = 0
    for c in l:
        if(c % 3 == 0):
            sum = sum + c
    return sum

s = []

print ("Enter 0 to stop the program")
n= input("Enter a number: ")
while (n!= "0"):
    s+= [int(n)]
    n=input("Write another number: ")

print("The numbers you have wrotten are: ",s)

print("The sum of the numers are: ",find_threes(s))
