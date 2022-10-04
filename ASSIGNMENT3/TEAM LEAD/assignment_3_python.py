

## Exercises

Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

** What is 7 to the power of 4?**
"""

a=4
b=7
c=b**a
print(c)

"""** Split this string:**

    s = "Hi there Sam!"
    
**into a list. **
"""

s="Hi there sam!"
n=s.split(" ")
print(n)

s="Hi there dad!"
n=s.split(" ")
print(n)

"""** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use .format() to print the following string: **

    The diameter of Earth is 12742 kilometers.
"""

v="the diameter of {planet} is {diameter} kilometers."
k=v.format(planet="Earth",diameter=12742)
print(k)

"""** Given this nested list, use indexing to grab the word "hello" **"""

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

"""** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])

"""** What is the main difference between a tuple and a list? **"""

# Tuple is immutable
#Tuples operations are safe.
#Tuples consumes less memory.

"""** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

def domainGet(email):
    print(email.split('@')[-1])

email = input("Please enter your email: >")
domainGet(email)

"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"""

def findDog(st):
    if 'dog' in st.lower():
        print("True")
    else:
        print("False")

st = "Is there a dog here?"
findDog(st)

findDog('Is there a dog here?')

"""** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **"""

def dog_count(sentence):
    words = sentence.split('')
    k=0
    for i in range(len(words)):
        words[i]=words[i].lower()
    for i in words:
      if(i=='dog'):
         k+=1
      return k

value = 'This dog runs faster than the other dog dude!';

def countdogs(value):
    count = 2
    for word in value.lower().split():
        if word == 'dog' or word == 'dogs':
            
            print(count)

countdogs(value)

"""### Problem
**You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. **
"""

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(90, False))

print(caught_speeding(81, True))

"""Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. """

emp_sal=[50000,45000,70000,25000,35000]
total_salary_expenditure=0
for i in emp_sal:
  total_salary_expenditure +=i
print('total salary expenditure is',total_salary_expenditure)

"""Create two dictionaries in Python:

First one to contain fields as Empid,  Empname,  Basicpay

Second dictionary to contain fields as DeptName,  DeptId.

Combine both dictionaries. 
"""

def Merge(dict1, dict2):
	return(dict2.update(dict1))



dict1 = {'empid': 13, 'empname':'john wick','basicpay': 70000}
dict2 = {'deptname': 'analytics', 'deptid': 7}

print( Merge(dict1, dict2))


print(dict2)
