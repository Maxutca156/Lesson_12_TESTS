from functions import salary, hello_who

if salary(2,10) != 40:
    print('Error')
if hello_who("Max") != "Hello, Max":
    print("Failed")
else:
    print("Good")
if hello_who("Leo") != "Hello, Leo":
    print("Failed")
else:
    print("Amazing")


'''print(hello_who('Max'))
print(salary(hours=2, salary_by_hour=10))'''