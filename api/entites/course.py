class Course:
    def __init__(self, name, description, published_at, formation):
        self.__name = name
        self.__description = description
        self.__published_at = published_at
        self.__formation = formation

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
    def published_at(self):
        return self.__published_at

    @published_at.setter
    def published_at(self, published_at):
        self.__published_at = published_at

    @property
    def formation(self):
        return self.__formation

    @formation.setter
    def formation(self, formation):
        self.__formation = formation
