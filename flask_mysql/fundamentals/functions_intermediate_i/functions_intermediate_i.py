from tkinter import Y
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[0][1] = 15
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
# Change the value 20 in z to 30
z[1]["y"] = 30

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
def iterateDictionary(students) 
    for x in range(0,len(students)):
        output="?"
        for key,val in students[x].items():
            output+= f " {key} - {val}"
            print(output)


 def iterateDictionary2(key_name, list):
    for x in range(0,len(list)):
        for key,val in lists[x].items():
            if key=key_name:
            print(val)
iterateDictionary2("first_name", students)
        

name_birth = {
    'names' : ['Yasmin', 'Adrian', 'Mel'],
    'dob' : ['April', 'March', 'May']
}

print(name_birth)