from functions import salary, hello_who

assert hello_who("Max") == "Hello, Max", ("Hello who Error")
assert hello_who("Leo") == "Hello, Leo", ("Hello who Error")
assert hello_who("Nikita") == "Hello, Nikita", ("Hello who Error")
assert salary(hours=2, salary_by_hour=1) == 4
assert salary(hours=2, salary_by_hour=2) == 8