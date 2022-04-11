# This programme is a user gudie to python Symbols.

import sys

def selector():
    types = ['and', 'as', 'assert', 'pass', 'break', 'class', 'continue', 'def', 'del', 'elif',
     'else', 'except', 'exec', 'finally', 'for', 'from']

    print("\n")
    print("Python has many symbols and words to learn. This program has been designed to help you if you get stuck.")
    print("Please see source code for working examples on each word.")
    print("\n")
    print(f"Here are some to choose from.. {types}")
    print("\n")
    print("Please type the word or symbol you would like more detail on.")
    print("\n")
    choice = input("> ")

    if "and" == choice:
        and1()
    elif "as" == choice:
        as1()
    elif "assert" == choice:
        assert1()
    elif "pass" == choice:
        pass1()
    elif "break" == choice:
        break1()
    elif "class" == choice:
        class1()
    elif "continue" == choice:
        continue1()
    elif "def" == choice:
        def1()
    elif "del" == choice:
        del1()
    elif "elif" == choice:
        elif1()
    elif "else" == choice:
        else1()
    elif "except" == choice:
        except1()
    elif "exec" == choice:
        exec1()
    elif "finally" == choice:
        finally1()
    elif "for" == choice:
        for1()
    elif "from" == choice:
        from1()
    else:
        selector()

def and1():
    print("\n")
    print("Description")
    print("\n")
    print("""Logical and. For example, True and False == False """)
    print("Both would have to be True to be True.")
    print("Below is a working example")
    #The working code is below.
    print("Please type your value for A")
    a = int(input())
    print("Please type your value for B")
    b = int(input())
    if a == b and b == a:
        print("Becuase you entered the same values then this is true")
    elif a != b:
        print("Becuase you entered different values then this is false.")
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def as1():
    print("\n")
    print("Description")
    print("\n")
    print("""Part of the with-as statement. For example, with X as Y: Pass """)
    print("")
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def pass1():
    print("\n")
    print("Description")
    print("\n")
    print("A pass statement can be used in development, sometimes your code would produce an error.")
    print("If you include the pass statement, python will ignore the fucntion")
    print(""" For example, if you wrote.
    def cars():
        x + y = 2 # Your programme would generally give a syntex error.
        pass # Using pass allows you to ignore this bit of code.

        Once you have finished the function you can remove the pass""")
    #The working code is below.
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def assert1():
    global passport_number
    print("\n")
    print("Description")
    print("\n")
    print("""Assert (ensure) that something is true. For example, is the assert is false it gives you an 'Error!' """)
    print("\n")
    print("UK passport numnbers are 9 digits. This progamme will ask you for your passport number,")
    print("it must be 9 digits so we can use assert.")
    print("** Warning, if you do not enter 9 digits the programme will crash. **")
    print("\n")
    #The working code is below.
    passport_number = input("Hello, please enter your passport number. ")
    assert len(passport_number)==9
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def break1():
    print("\n")
    print("Breaks can be used in for loops and while loops")
    print("They can break the loop when a certain value is encountered")
    print("""If you create a loop like this one
    count_to_ten = ["1","2","3","4","5","6","7","8","9","10"]
    while count_to_ten:
        numbers = count_to_ten.pop()
        if numbers == "7": break""")
    #The working code is below.
    print("\n")
    count_to_ten = ["1","2","3","4","5","6","7","8","9","10"]
    while count_to_ten:
        numbers = count_to_ten.pop()
        if numbers == "7": break
        print(numbers)

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def class1():
    print("\n")
    print("The easiest way to describe a class in python is like creating your own module to use in your programmes.")
    print("Inside a 'class' you can define functions or in object orientated terminology they are called methods.")
    print("\n")
    print("""
    This is an example of a class file. This class is relating to a human. The properties are name and occupation.
    The methods are a way of producing an outcome based on the arguments that are passed.

    class human:
        # def __init__(self, n, o): is classed as properties.
        def __init__(self, n, o): #init = initialise. name and occupation are arguments to the function.
            self.name = n # n is for name
            self.occupation = o # o is for occupation.

        def do_work(self): # This is a method
            if self.occupation == "tennis player":
                print(self.name, "plays tennis")
            elif self.occupation == "actor":
                print(self.name, "shoots a film")

        def speaks(self): # This is the second method
            print(self.name, "says, how are you?")

    # you can have as many methods as you want, however just 2 for this example.

    tom = human("tom cruise", "actor" )
    # self is always passed as the argument so you only need the argument for 'n' and 'o'.

    tom.do_work()
    # now you are running the script for the 'do_work' method using the arguments you have passed above.
    tom.speaks()
    """)
    #The working code is below.
    print("\n")
    import class_example1
    human = class_example1.human("tom cruise", "actor")
    human.do_work()
    human.speaks()

    human = class_example1.human("lisa Russell", "project manager")
    human.do_work()
    human.speaks()

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def continue1():
    print("\n")
    print("Continue can be used in for loops and while loops")
    print("whereas 'break' stops the loop and goes to the end,")
    print("'continue' will skip the whatever is in the if statement and 'continue' with the rest of the list.")
    print("\n")
    print("""If you create a loop like this one
    count_to_ten = ["1","2","3","4","5","6","7","8","9","10"]
    while count_to_ten:
        numbers = count_to_ten.pop()
        if numbers == "7": continue""")
    #The working code is below.
    print("\n")
    count_to_ten = ["1","2","3","4","5","6","7","8","9","10"]
    while count_to_ten:
        numbers = count_to_ten.pop()
        if numbers == "7": continue
        print(numbers)

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()
    pass

def def1():
    print("\n")
    print("Def if used when you want to define a function. ")
    print("You should always use these as it makes your code a lot easier to read.")
    print("\n")
    print(""" This is what a function looks like.
    def calc:
        a = 2
        b = 4
        c = a + b
        print(f" This is the calculation of a + b = {c}"") """)
    #The working code is below.
    print("\n")
    print("You can then use that function anywhere in your script by typing clac()")

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def del1():
    print("\n")
    print("Del - You would use del to delete values from a 'dictonary' a dictonary is a bit like a list. ")
    print("The difference being a dictonary has a key value pair. For example..")
    print("Football teams. 'Liverpool - The Reds', Arsenal - The Gunners")
    print("Now lets put them in a dictorary and use del to delete one.")
    print("\n")
    print(""" This is the code you would use to create a dictonary and use del to delete.
    my_dict = {"liverpool" : "The Reds", "arsenal" : "The Gunners", "leicester" : "The Foxes", "southampton" : "The Saints"}
    #This is our dictonary.
    del my_dict["leicester"]
    print(f"{my_dict}")""")
    #The working code is below.
    print("\n")
    my_dict = {"liverpool" : "The Reds", "arsenal" : "The Gunners", "leicester" : "The Foxes", "southampton" : "The Saints"}
    #This is our dictonary.
    del my_dict["leicester"]
    print(f"{my_dict}")
    print("\n")
    print("As you will be able to see, I ran the script and Leicester has been deleted from the dictonary")
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def elif1():
    print("\n")
    print("elif = else is a condition")
    print("elif would generally be used after if. For example if if is not true use this 'elif'. ")
    print("\n")
    print(""" This is some example code for 'elif' the actually code is used below.

    print("Please type a number between 1 and 100")
    choice = int(input("> "))

    if choice > 0 and choice < 26:
        print("That is a very low number.")
    elif choice > 26 and choice < 50:
        print("That is a low number.")
    elif choice > 50 and choice < 75:
        print("That is a high number.")
    elif choice > 75 and choice < 100:
        print("That is a very high number.")
    else:
        elif1()""")
    #The working code is below.
    print("Please type a number between 1 and 100")
    choice = int(input("> "))

    if choice > 0 and choice < 26:
        print("That is a very low number.")
    elif choice > 26 and choice < 50:
        print("That is a low number.")
    elif choice > 50 and choice < 75:
        print("That is a high number.")
    elif choice > 75 and choice < 100:
        print("That is a very high number.")
    else:
        elif1()

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def else1():
    print("\n")
    print("The 'else' condition is like the if and elif conditions and would generally be used after these.")
    print("\n")
    print("""  Here is some example code below,
    print("Type 'A', 'B', 'C' or 'D'.")
    choice = input("> ")

    if choice == "A" or choice == "a":
        print("Great, you selected 'A'.")
    elif choice == "B" or choice == "b":
        print("Great, you selected 'B'.")
    elif choice == "C" or choice == "c":
        print("Great, you selected 'C'.")
    elif choice == "D" or choice == "d":
        print("Great, you selected 'D'.")
    else:
        else()              """)

    #The working code is below.
    print("Type 'A', 'B', 'C' or 'D'.")
    choice = input("> ")

    if choice == "A" or choice == "a":
        print("Great, you selected 'A'.")
    elif choice == "B" or choice == "b":
        print("Great, you selected 'B'.")
    elif choice == "C" or choice == "c":
        print("Great, you selected 'C'.")
    elif choice == "D" or choice == "d":
        print("Great, you selected 'D'.")
    else:
        else1()

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def except1():
    print("\n")
    print("You would use 'except' where you could possibly get a syntax error.")
    print("Below I have given the value of x but asked to print 'x' and 'y'.")
    print(""" Instead of the programme actually giving the syntax error, it uses 'except' to print 'An exception occurred'

    x = 10
    try:
        print(x)
        print(y)
    except:
        print("An exception occurred")    """)
    print("\n")
    #The working code is below.
    x = 10
    try:
        print(x)
        print(y)
    except:
        print("An exception occurred")

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def exec1():
    print("\n")
    print("exec - execute code. ")
    print("It is sort of like running python, in python.")
    print("\n")
    exec("print('Ive used exec to print this sentence.')")
    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def finally1():
    print("\n")
    print("The finally block will run regadless of the outcome of your code. As in 'finally' do this no matter what.")
    print("""This can be used a long with 'Try' and 'Except'
    x = 10
    try:
        print(x)
        print(y)
    except:
        print("An exception occurred")
    finally:
        print("This will print regardless of whether there is a syntax error or not.")     """)
    print("\n")
    #The working code is below.
    x = 10
    try:
        print(x)
        print(y)
    except:
        print("An exception occurred")
    finally:
        print("This will print regardless of whether there is a syntax error or not.")

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def for1():
    print("\n")
    print("'for' as in 'for loop'.")
    print("A for loop is used to loop a sequence or list.")
    print("In the example below the loop is printing each letter at a time until it comes to the end of the sequence.")
    print("\n")
    print("""
    text = "python"

    for character in text:
        print(character)""")
    #The working code is below.
    text = "python"

    for character in text:
        print(character)

    print("\n")
    play = input(" Hit enter to search for another Symbol.")
    selector()

def from1():
    print("\n")
    print("You will need to import modules in python all the time.")
    print("Sometimes it is better to import just the function you need from that module.")
    print("""For example I have created a module called 'from_example' and created 3 different functions

    This is what the module looks like.
    def fruit1():
        apple = 1
        print(f"You have {apple} apple.")

    def fruit2():
        apple = 2
        print(f"You have {apple} apples.")

    def fruit3():
        apple = 3
        print(f"You have {apple} apples.")

    Each function gives a different value for apple. In our example we want to import def fruit2 only.
    This is what our from statement looks like.

    from from_example import fruit2
    print(fruit2())'     """)
    print("\n")
    #The working code is below.
    from from_example import fruit2
    print(fruit2())
    print("\n")

    play = input(" Hit enter to search for another Symbol.")
    selector()

selector()
