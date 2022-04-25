# This programme is a user gudie to python Symbols.

import sys
var = "This is my global variable."
var2 = "This is my second global variable."


def selector():
    types = ['and', 'as', 'assert', 'pass', 'break', 'class', 'continue', 'def', 'del', 'elif',
     'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
     'lambda', 'not', 'or', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

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
    elif "global" == choice:
        global1()
    elif "if" == choice:
        if1()
    elif "import" == choice:
        import1()
    elif "in" == choice:
        in1()
    elif "is" == choice:
        is1()
    elif "lambda" == choice:
        lambda1()
    elif "not" == choice:
        not1()
    elif "or" == choice:
        or1()
    elif "print" == choice:
        print1()
    elif "raise" == choice:
        raise1()
    elif "return" == choice:
        return1()
    elif "try" == choice:
        try1()
    elif "while" == choice:
        while1()
    elif "with" == choice:
        with1()
    elif "yield" == choice:
        yield2()
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
    play = input(" Hit enter to search for another word.")
    selector()

def as1():
    print("\n")
    print("Description")
    print("\n")
    print("""Part of the with-as statement. For example, with X as Y: Pass """)
    print("")
    print("\n")
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
    selector()

def exec1():
    print("\n")
    print("exec - execute code. ")
    print("It is sort of like running python, in python.")
    print("\n")
    exec("print('Ive used exec to print this sentence.')")
    print("\n")
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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
    play = input(" Hit enter to search for another word.")
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

    play = input(" Hit enter to search for another word.")
    selector()

def global1():
    print("\n")
    print("A variable that is created outside of a function is called a global variable.")
    print(f"I can call a global variable inside any function. -> {var}.")
    print("\n")
    print("""If you want to amend a variable inside a funtion you need to write 'global variable_name' inside your function.
    global var2
    var2 = "edited variable"
    print(f"Python has used the '{var2}' because I wrote 'global var2' in the function.")""")
    print("\n")
    #The working code is below.
    global var2
    var2 = "edited variable"
    print(f"Python has used the '{var2}' because I wrote 'global var2' in the function.")
    print("\n")

    play = input(" Hit enter to search for another word.")
    selector()

def if1():
    print("\n")
    print("An 'if' statement is used when you want a decision to be made.")
    print("""
    a = int(input())

    if a == 2:
        print("Python has checked 'if' you entered 2. In this case you did.")
    elif a != 2:
        print("Python has checked 'if' you entered 2. In this case you did not.")
    """)

    #The working code is below.
    print("Please enter the number '2' below. Python will use the if statement to see if you have entered '2'.")
    a = int(input())
    if a == 2:
        print("Python has checked 'if' you entered 2. In this case you did.")
    elif a != 2:
        print("Python has checked 'if' you entered 2. In this case you did not.")
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def import1():
    print("\n")
    print("Import is used when you want to import a module to use in your programme.")
    print("\n")
    print("These can be common modules such as 'NumPy', 'Pandas' or 'Django'.")
    print("Or you can create and use your own modules.")
    print("To insall a module you would need to use pip install on your terminal.")
    print("\n")
    print("""This is how you would import the module. I have created a module named 'yourname'
    in that module it has a function 'namer' as shown below.

    def namer(name):
        print(f"Hello {name}, nice to meet you.")

    to import this into your file you would use the below code.

    import yourname
    yourname.namer("Rob")
        """)
    #The working code is below.
    import yourname
    yourname.namer("Rob")

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def in1():
    print("\n")
    print("'in' as in 'for character in text' or 'for i in range'.")
    print(".")
    print("In the example below the loop that runs from 0 to 4. Each time it loops it will print 'i' the number.")
    print("\n")
    print("""
    for i in range(5):
        print i
        """)
    print("\n")
    #The working code is below.
    for i in range(5):
        print (i)
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def is1():
    print("\n")
    print("This is operator in Python is use to test if something is true or false.")
    print("For example 1 is 1 == True. Because 1 does equal 1.")
    print(""" With the below code we are asking if x and c are the same value.
    x = 1
    c = 1

    if (x is c):
        print("Both X and C have a value of 1.")
    else:
        print("X and C have different values.")  """)
    print("\n")
    #The working code is below.
    x = 1
    c = 1

    if (x is c):
        print("Both X and C have a value of 1.")
    else:
        print("X and C have different values.")
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def lambda1():
    print("\n")
    print("A Lambda function is an anonymous function. This would be a function that doesn't use 'def'.")
    print("Below we have defined the function 'double' without using def. we have then run the function with the argument '10'.")
    print("""
    double = lambda n:n*2
    print(double(10))
    """)
    print("\n")
    #The working code is below.
    double = lambda n:n*2
    print(double(10))

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def not1():
    print("\n")
    print("not in python is logic. not true == false.")
    print("The script below asks the user for an input. Depending on the input it will decide if the value is 'not' more than 10.")
    print("""
    print("Please type your value for A")
    a = int(input())
    if not a > 10:
        print("The value you entered is 10 or less.")
    else:
        print("The value you entered is greater than 10.")
               """)

    print("\n")
    #The working code is below.
    print("Please type your value for A")
    a = int(input())
    if not a > 10:
        print("The value you entered is 10 or less.")
    else:
        print("The value you entered is greater than 10.")

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def or1():
    print("\n")
    print("Description")
    print("\n")
    print("""Logical Or. For example, True or False == True """)
    print("only 1 would have to be true to be true. Sort of like the opposite of 'and'.")
    print("Below is a working example, it will test if either A or B == 10.")
    #The working code is below.
    print("Please type your value for A")
    a = int(input())
    print("Please type your value for B")
    b = int(input())
    if a == 10 or b == 10:
        print("Atleast 1 of the numbers you entered was 10.")
    else:
        print("None of the numbers you entered were 10.")
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def print1():
    print("\n")
    print("You would use the 'print' string to ask python to output something you have wrote.")#
    print("""
    print("This is what a string looks like")
    print(f"This is how you write a string that can include variables {variable_name}.)
    """)
    #The working code is below.
    variable_name = "Hello, this is a working variable."
    print(f"look.. {variable_name}")
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()
    print("\n")

def raise1():
    print("\n")
    print("You would use 'raise' to raise an exception in the programme.")
    print("""This is what your code should look like for a cash machine.
    try:
        a = int(input())
        if a>100:
            raise exception
        else:
            print("Thank you, please take your cash.")
    except:
        print("The amount exceeds your £100 limit.")
    """)
    print("\n")
    print("Please type in the amount you would like to withdraw - £100 limit.")
    #The working code is below.
    try:
        a = int(input())
        if a>100:
            raise exception
        else:
            print("Thank you, please take your cash.")
    except:
        print("The amount exceeds your £100 limit.")



    play = input(" Hit enter to search for another word.")
    selector()
    print("\n")

def return1():
    print("\n")
    print("You can use the return function if you want to call a variable outside of the function it is in.")
    print("For example, below is a function called pancakes.")
    print("""
    def pancakes():
        cakes = 10
        return cakes

    # The function above will give us an output of 10.

    pancake_tracker = pancakes() #Here we have created a variable that runs pancakes()
    print(pancake_tracker)

    # Because we used 'return', when we call the variable pancake_tracker it will
    run the function and give us an output of '10'

    """)
    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()
    print("\n")

def try1():
    print("\n")
    print("You would use the 'try' function in conjunction with 'try, finally, except.'")
    print("The try part basically means try to run this code, you would then use finally or execpt as alternatives if it doesn't run.")
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
    play = input(" Hit enter to search for another word.")
    selector()

def while1():
    print("\n")
    print("While is a type of loop. ")
    print("A while loop will loop until a certain condition is met.")
    print(""" In this example we are telling python to loop until the condition gets to 10.
    condition = 10 #This is just a variable and can be any name.
    while condition < 10:
        print(condition)
        condition += 1  # This is the same as condition = condition + 1.
            """)
    print("\n")
    #The working code is below.
    condition = 1
    while condition < 10:
        print(condition)
        condition += 1

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def with1():
    print("\n")
    print("The 'with' statement is used to open files in Python. ")
    print("The advantage of using the with statement is that the file is closed automatically.")
    print("""
    with open("with.txt") as file_obj:
        for line in file_obj:
            print(line)
            """)
    print("\n")

    with open("with.txt") as file_obj:
        for line in file_obj:
            print(line)

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

def yield1():
    #The working code is below.
    print("\n")
    yield 9000
    yield 8000
    yield ['You', 'Can', 'Yield', 'From', 'A', 'List']
    yield 7000

def yield2():
    print("\n")
    print("Yield from. This is a syntax that allows you to use delegation from generators.")
    print("It allows you to generate from multiple lists within the same loop.")
    print("""
    def yield1():
        yield 9000
        yield 8000
        yield ['You', 'Can', 'Yield', 'From', 'A', 'List']
        yield 7000
    # Above would be in its own function

    # Below is how you call the list in another function.
    for thing in yield1():
        print(f"Testing, testing.. {thing}")    """)

    #The working code is below and in the function def yield2()
    print("\n")
    for thing in yield1():
        print(f"Testing, testing.. {thing}")

    print("\n")
    play = input(" Hit enter to search for another word.")
    selector()

selector()
