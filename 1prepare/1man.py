class Man:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def getSex(self):
        print(self.sex)

    def goodbye(self):
        print("Good-bye " + self.name + "!")


m = Man("David", "male")
m.hello()
m.getSex()
m.goodbye()
