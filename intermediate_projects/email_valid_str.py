# THIS PROJECT IS ABOUT EMAIL VALIDATION USING STRING IN PYTHON

email = input("Enter your Email: ")

a,b,c = 0,0,0

if len(email) >= 6:

    # [6] is because an email at least contain 6 variables
    # For Example: x@g.pk [This contain 6 variable for a valid email]
    # Look x=1, @=2, g=3, dot(.)=4 , p=5, k=6
    
    if email[0].isalpha():

        # The First variable of an email must contain an alphabet

        if ("@" in email) and (email.count("@") == 1):

            # Email must contain @ and it could be not more than 1

            if (email[-4] == ".") ^ (email[-3] == "."):

                # The index -4 is used [when we use .com] alse index -3 is used for [when we use .pk]
                # Also we used XOR (^) operator because dot (.) should be one of the position
                # Like dot will be with .com or it will be with .pk

                for i in email:

                    # To Check whether the space or capital lettor is in the email

                    if i.isspace():
                        a = 1
                    
                    elif i.isalpha():
                        
                        if i.isupper():
                            b = 1

                    elif i.isdigit():
                        continue

                    elif i == "_" or i == "." or i == "@":
                        continue

                    else:
                        c = 1

                if a == 1 or b == 1 or c ==1:
                    print("Invalid Email 5")

                else:
                    print("Valid Email")

            else:
                print("Invalid Email 4")
            

        else:
            print("Invalid Email 3")

       
    else:
        print("Invalid Email 2")

else:
    print("Invalid Email 1")