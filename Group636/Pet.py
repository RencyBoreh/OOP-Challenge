class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 7  
        self.energy = 7  
        self.happiness = 7 
        self.tricks = []  
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍽️ {self.name} is eating! Hunger decreased, happiness increased! 🥳")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"💤 {self.name} is sleeping! Energy restored! 😴")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"🎾 {self.name} is playing! Happiness up, but energy and hunger changed! 🐶")

    def get_status(self):
        print(f"📊 {self.name}'s Status:")
        print(f"💖 Happiness: {self.happiness}/10")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"🎓 {self.name} learned '{trick}'! Happiness increased! 🏆")

    def show_tricks(self):
        if self.tricks:
            print(f"🤹 {self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"😅 {self.name} hasn't learned any tricks yet!")

