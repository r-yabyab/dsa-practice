class Person():
    def __init__(self, age, height):
        self.age = age
        self.height = height
    
    def speak(self):
        print("talk")

    def imperial(self):
        # height = self.height
        imperial_height = self.height/12 + self.height%12
        return imperial_height
    


def main():
    bobby = Person(50, 80)
    print(bobby.age)
    print(bobby.imperial())

main()