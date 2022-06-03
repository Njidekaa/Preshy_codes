class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        print("The first student's details are", name, int(age), tracks, float(score))

    #method for the above class

    def change_name(self, another_name):
        self.name = another_name
        

    def change_age(self, another_age):
        self.age = int(another_age)
    
    def add_track(self, another_track):
        self.track = self.tracks.append(another_track)

    def get_score(self):
        return self.score

    def result(self):
        print("The Second Student's details are", self.name, self.age, self.tracks, self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
Bob.result()