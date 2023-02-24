class Campus:
    def _init_(self, name, location, num_buildings, num_students):
        self.name = name
        self.location = location
        self.num_buildings = num_buildings
        self.num_students = num_students
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def remove_building(self, building):
        self.buildings.remove(building)

class Building:
    def _init_(self, name, location, num_floors, num_classrooms, num_labs):
        self.name = name
        self.location = location
        self.num_floors = num_floors
        self.num_classrooms = num_classrooms
        self.num_labs = num_labs
        self.classrooms = []
        self.labs = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def add_lab(self, lab):
        self.labs.append(lab)

    def remove_lab(self, lab):
        self.labs.remove(lab)

class Classroom:
    def _init_(self, name, location, capacity, equipment):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.equipment = equipment
        self.course = None

    def assign_course(self, course):
        self.course = course

    def unassign_course(self):
        self.course = None

class Laboratory:
    def _init_(self, name, location, capacity, equipment):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.equipment = equipment

class Library:
    def _init_(self, name, location, num_books):
        self.name = name
        self.location = location
        self.num_books = num_books