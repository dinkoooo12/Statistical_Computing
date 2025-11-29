x=int(input("Enter the first number \n"))
y=int(input("The second nu \n"))

if x > y:
    print(str(x) + " is greater than " + str(y))

elif x < y:
    print(str(x) + " is less than " + str(y))
else:
    print(" they are equal")
    # comme
    '''
    dfghjkl;67y8uiop
    dfghjkl
    dfghjk
#     '''

text = "fghjklghjkl dfghjkl wertyuiop first. dfghjkl mbvcxzxcv second. wertyuio dfghjk qwertyu third. wertyui dfghjkl fourth. fghjyu fghjkdfgh last"
for val in text.split("."):
    print(val.split()[-1])

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
for sentence in lorem.split("."):
    for word in sentence.split():
        word = list(word)
        print(word[-1])

