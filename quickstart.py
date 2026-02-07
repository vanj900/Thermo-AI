import random

class Agent:
    def __init__(self):
        self.energy = 100
        self.age = 0
        self.metabolic_constraints = random.randint(10, 30)

    def live(self):
        while self.energy > 0:
            self.age += 1
            self.energy -= self.metabolic_constraints
            print(f"Age: {self.age}, Energy: {self.energy}")
            
        print("Agent has died.")

if __name__ == "__main__":
    agent = Agent()
    agent.live()