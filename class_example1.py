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
        elif self.occupation == "project manager":
            print(self.name, "manages projects")

    def speaks(self): # This is the second method
        print(self.name, "says, how are you?")
