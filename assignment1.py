# Base class
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.age}-year-old from {self.nationality}."

# Derived Class
class Footballer(Person):
    def __init__(self, name, age, nationality, club, position, goals):
        super().__init__(name, age, nationality)
        self.club = club
        self.position = position
        self.goals = goals

    def player_info(self):
        return f"{self.name} plays as a {self.position} for {self.club}. He has scored {self.goals} goals."

    def score_goal(self):
        self.goals += 1
        return f"{self.name} scored! Total goals: {self.goals}"

messi = Footballer(
    name="Lionel Messi",
    age=36,
    nationality="Argentinian",
    club="Inter Miami",
    position="Forward",
    goals=800
)

# Demonstrate the functionality
print(messi.introduce())
print(messi.player_info())
print(messi.score_goal())
print(messi.score_goal())
