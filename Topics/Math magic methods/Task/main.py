class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        self.description += '\n'
        self.description += other.description

        self.team += ', '
        self.team += other.team
        return self
