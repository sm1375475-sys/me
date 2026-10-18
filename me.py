class student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id 
        self.__grade=grade 

    def get_grade(self):
        return self.__grade