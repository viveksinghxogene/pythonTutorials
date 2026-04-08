#function to find the cube of the number
f=lambda n:n**3
print(f'the cube of 3 is : {f(3.1)}')
#function to check validity of vote
vote=lambda age:"YES" if age>=18 else "NO"
name=input('Enter the name of the person: ')
age=int(input(f'Enter the age of {name}: '))
print(f'Eligibility of {name} to vote is : {vote(age)}')