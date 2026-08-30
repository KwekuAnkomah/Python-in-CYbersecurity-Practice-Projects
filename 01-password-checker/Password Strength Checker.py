print('%'* 45)
print('PASSWORD STRENGTH CHECKER')
print('-'*45)

special_chars = "! @ # $ % ^ & * '"
the_digits = "1 2 3 4 5 6 7 8 9 0"
list_digits = the_digits.split()
list_chars = special_chars.split()


while True:
    passwd = input('Enter Password: ')
    rules_passed = 0
    has_special = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(passwd) < 8:
        print("Length: ❌") 
    else:
        print("Length: ✅")
        rules_passed += 1
    for i in passwd:
        if i in list_chars:
           has_special = True
    if has_special:
        print("Special Character: ✅")
        rules_passed += 1
    else:
        print("Special Character: ❌")
    for i in passwd:
        if i.isupper():
            has_upper = True
    if has_upper:
        print("Uppercase: ✅")
        rules_passed += 1
    else:
         print("Uppercase Letter: ❌")
    for i in passwd:
        if i.islower():
            has_lower = True
    if has_lower:
        print("Lowercase: ✅")
        rules_passed += 1
    else:
        print("Lowercase Letter: ❌")
    for i in passwd:
        if i in list_digits:
            has_digit = True
    if has_digit:
        print("Digit: ✅")
        rules_passed += 1
    else:
        print("Digit: ❌")

    print(f"{rules_passed} Rules Passed!...")
    if rules_passed == 5:
        print("Strong Password ✅✅✅✅✅")
    elif rules_passed in [3,4]:
        print("You Can Do Better")
    else:
        print("TERRIBLE PASSWORD!!!!")

    quit_option = input("Would You Like To Quit?(Y/N)")
    if quit_option.lower() == 'y':
        break