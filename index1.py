class Superhero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
    
    def use_power(self, power_name):
        if power_name in self.powers:
            print(f"{self.name} uses {power_name}!")
        else:
            print(f"{self.name} doesn't have {power_name} power.")
    
    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.secret_identity}.")


class TheFlash(Superhero):
    def __init__(self):
        super().__init__(
            name="The Flash",
            secret_identity="Barry Allen",
            powers=["Super Speed", "Time Travel"]
        )
        self.speed = 100  # Speed in mph
    
    def run_fast(self):
        print(f"⚡ {self.name} runs at {self.speed} mph! ⚡")
    
    def time_travel(self):
        if "Time Travel" in self.powers:
            print(f"{self.name} travels through time!")
        else:
            print(f"{self.name} can't time travel yet!")


# Demonstration
print("=== Superhero ===")
hero = Superhero("Superman", "Clark Kent", ["Super Strength", "Flight"])
hero.use_power("Flight")
hero.reveal_identity()

print("\n=== The Flash ===")
flash = TheFlash()
flash.use_power("Super Speed")
flash.run_fast()
flash.time_travel()
flash.reveal_identity()
