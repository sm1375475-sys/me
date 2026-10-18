class student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id 
        self.__grade=grade 

    def get_grade(self):
        return self.__grade
    def add_grade(self, grade):
        return self.__grade.append(grade)