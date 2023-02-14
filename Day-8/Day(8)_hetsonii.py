student = {
    'first_name': 'Het',
    'last_name': 'Soni',
    'gender': 'male',
    'age': '18',
    'marital_status': 'Unmarried',
    'skills': ['Python', 'C++', 'Bash'],
    'country': 'India',
    'city': 'Nadiad',
    'address': "Charusat University, Changa"
}

print("Length of the Student Dictionary: ",len(student))
print("\nSkills: {} \nDatatype of Skills: {}".format(student.get("skills"), type(student.get("skills"))))

student['skills'].append('Vagrant')
student['skills'].append('PowerShell')
print("Updated Skills: ", student.get("skills"))

print("\nDictionary values as a list: \n",list(student.values()))
print("\ndictionary as a list of tuples: \n", student.items())