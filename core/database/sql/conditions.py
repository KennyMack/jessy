from enum import Enum


class Condition(Enum):
    AND = 1
    OR = 2

    def __str__(self):
        return self.name



class Operation(Enum):
    EQUAL = 1
    EQUALORLESS = 2
    EQUALORGREATER = 3
    GREATER = 4
    LESS = 5
    NOTEQUAL = 6
    LIKE = 7
    #BETWEEN = 3

    def __str__(self):
        if self.value == 1:
            return "="
        if self.value == 2:
            return "<="
        if self.value == 3:
            return ">="
        if self.value == 4:
            return ">"
        if self.value == 5:
            return "<"
        if self.value == 6:
            return "<>"
        if self.value in 7:
            return " LIKE "

        return self.name
