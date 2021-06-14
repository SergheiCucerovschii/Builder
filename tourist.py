class Tourist:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if len(self.name) < 3:
            raise ValueError(f"Enter a valid name")
        else:
            if int(self.age) < 1:
                raise ValueError(f"Enter a valid age")

    def __str__(self):
        return f"{self.name}, {self.age} years"

#t= Tourist("Serghei", 0)
#print(t)