import re

email_condition = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
email = input("Type an Email: ")

if re.search(email_condition, email):
    print("Valid Email")
else:
    print("Invalid Email")
