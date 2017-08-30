# Write a program that turns a sentence into camel case
# print a warning message if the input will not produce a valid Python variable name.
#test for a few common issues, such as starting with a number, or invalid characters such as # or + or ".
def main():
    print("  Howdy. Let's learn about camel case. \nYou will use it a lot when writing code.")
    print("\t\tExciting, isn't it?!")#intro and welcome
    print("\n")#blank space for easier readability
    print("Camel case looks like, well, camelCase. \nEvery word except the first is capitalized.")
    print("And there are no spaces between the words.")
    print("Go ahead, give it a try!\n")#instructions for user
    message = input("enter some shit: ")
    #message = print("Please type a few words or short sentence, then press enter: ")
    print("ok, you entered: " + message)#confirm the user entry, easier for them to compare to result

    validData(message)

    message = message.title()
    print(message)
    noSpaceMessage = message.replace(" ", "")
    print(noSpaceMessage)
    lowerCaseChar = noSpaceMessage[:1]
    lowerCaseChar = lowerCaseChar.lower()
    camelCaseMessage = lowerCaseChar + noSpaceMessage[1:]
    print(camelCaseMessage)

    print("working hard on code here.")# thanks Clara

def validData(message):
    #confirm all valid char in user input
    if (message) == "":
        print("Error! please enter some words")
    elif "!" in message:
        print("not allowed")

main()