class Duck:
    def talk(self):
        print("Quack Quack! I am a duck")

class Human:
    def talk(self):
        print("Hello this function is called for the human")


def callTalk(obj):
    obj.talk();


d = Duck()
callTalk(d)

h = Human()
callTalk(h)
