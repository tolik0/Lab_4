class Building:
    """
    Class which represent building in total
    """

    def __init__(self, address):
        self.address = address


class House(Building):
    """
    Class which represent living house
    """

    def __init__(self, address, list_with_flats):
        self.address = super().__init__(address)
        self.flats = list_with_flats


class AcademicBuilding(Building):
    """
    Class for classroom representation
    """

    def __init__(self, address, classrooms):
        """
         (AcademicBuilding, str, list) -> NoneType
        Create new building
        classrooms - list of Classroom
        """
        self.classrooms = classrooms[:]
        self.address = super().__init__(address)

    def total_equipment(self):
        """
         (AcademicBuilding) -> list
        Return list of tuples where first element is name of equipment and
        second is amount of it in building
        """
        tot_equipment = dict()
        for i in self.classrooms:
            for equip in i.equipment:
                if equip in tot_equipment:
                    tot_equipment[equip] += 1
                else:
                    tot_equipment[equip] = 1
        return [(i, tot_equipment[i]) for i in tot_equipment]

    def __str__(self):
        """
         (AcademicBuilding) -> str
        Return string with information about building in comfortable for
        user way
        """
        return self.address + "\n" + "\n".join(
            [str(i) for i in (self.classrooms)])


class Classroom:
    """
    Class for classroom representation
    """

    def __init__(self, number, capacity, equipment):
        """
         (Classroom, str, int, list) -> NoneType
        Create new classroom
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment[:]

    def is_larger(self, c):
        """
        (Classroom, Classroom) -> boolean
        Show in what classroom there is larger capacity
        Return True if first classroom is larger
        """
        return True if self.capacity > c.capacity else False

    def equipment_differences(self, c):
        """
        (Classroom, Classroom) -> list
        Show equipment from first classroom that is not in second
        Return list of it
        """
        return [i for i in self.equipment if i not in c.equipment]

    def __str__(self):
        """
        (Classroom) -> str
        Return information about classroom in comfortable way for user
        """
        return "Classroom {} has a capacity of {} persons and has the \
following equipment: {}.".format(self.number, self.capacity, ", ".join(
            self.equipment))

    def __repr__(self):
        """
        (Classroom) -> str
        Return information about classroom in comfortable way for developer
        """
        class_name = type(self).__name__
        return "{} ({},{},{})".format(class_name, self.number, self.capacity,
                                      self.equipment)
