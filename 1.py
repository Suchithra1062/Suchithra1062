#length,width=20,50
#print(length*width)

#print("Hi My name is ",name ,"and I am", age, "yours old")
#number=int(input('enter the number'))

#if number %2==0:
 #   print("It's an even number")
#else:
 #   print("It's an old number")


#l=[1,2,3,-22,-33,44,99]
#print(max(l))
#print(min(l))

mystr="python"
reversed_string=mystr[::-1]
if mystr==reversed_string:
    print("It's a palindrome")
else:
    print("It is not a palindrome")

#sixth
#(P*t*r)/100

sum=0
l=[-8,8,0,2,3,4,10,12,-18,-19]
for elements in l:
    if elements>0:
        sum+=elements
#print(sum)

#swaping
a,b=10,20
a,b=b,a
#print(a,b)

a=1,"Hi","bye",2.5,2+5j
#print(a,type(a))

b,*c=[1,2,3],[4,5,6],"Hi","bye"
#print(b,type(b),c,type(c))

#a=int(input("enter your number"))
#print("it's an even") if a%2==0 else print("it's an odd")
#print("it's an even") if a%2==0 else print("it's a zero") if a==0 else print("its an odd")


"""list4=list()
for i in range(1,101):
    list4.append(i)
    print(list4)

o=list()
for divisible_by_4 in list4:
    if divisible_by_4 %4==0:
        o.append(divisible_by_4)
print(o)"""

"""list4=[data for data in range(1,101)]
o=[data for data in list4 if data%4==0]
print(l)
print(o)"""

#syntax list comprhension
#[<result> for <temp_var><opr><expr> if<condition>]

dictionary={k:k**2 for k in range(1,10)}
print(dictionary)