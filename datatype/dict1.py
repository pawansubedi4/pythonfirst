students=[
    {'name':'ram','address':'ktm'},
    {
        'name':"sophia",
        'address':{
            'permanent':"ktm",
            'temp':"lalitpur"
        }
    }
]
print(students)
print(f"my name is {students[1]['name']} \n I live in {students[1]['address']['temp']}")
print(type(students[1]))