class Formation:
    def __init__(self, name, description, teachers):
        self.__name = name
        self.__description = description
        self.__teachers = teachers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        self.__teachers = teachers
