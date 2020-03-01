class Food:
    __food_value = 0
    def __init__(self):
        self.__food_value = 0
        print("Объект создан")

    @property
    def food_value(self):
        return self.__food_value
    @food_value.setter
    def food_value(self, value):
        self.__food_value = value

    def __str__(self):
        return "Объект класса Food"

    def get_food_value(self):
        return self.__food_value

class Vegetables(Food):
    __type = ""
    __food_value = 10
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Объект класса Vegetables"

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        if value in ["клубнеплод", "корнеплод", "капустный", "луковичный"]:
            self.__type = value
        else:
            print("Такого типа нет")
            self.__type = ""

class Onion(Vegetables):
    __type = "луковичный"
    __food_value = 6
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Объект класса Onion"

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if value in ["маленький", "средний", "большой"]:
            self.__size = value
        else:
            print("Такого типа нет")
            self.__type = ""

    def get_type(self):
        return self.__type

class Bread(Food):
    __food_value = 10
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Объект класса Bread"

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        if value in ["белый", "чёрный", "серый"]:
            self.__type = value
        else:
            print("Такого типа нет")
            self.__type = ""

class Meat(Food):
    __type = "курица"
    __food_value = 20
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Объект класса Meat"

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in ["баранина", "свинина", "курица", "крольчатина", "телятина", "медвежатина"]:
            self.__type = value
        else:
            print("Такого типа нет")
            self.__type = ""

class Lunch(Meat, Vegetables, Bread):
    __food_value = 60
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Объект класса Lunch"

    def eat(self):
        print("Ланч съеден")

    def get_food_value(self):
        return self.__food_value


food = Food()
vegs = Vegetables()
onion = Onion()
bread = Bread()
meat = Meat()
lunch = Lunch()
food.food_value = 0
vegs.food_value = 10
meat.type = "qwertyu"
print(food.food_value)
print(vegs.food_value)
print(onion.get_type())
print(meat.type)
print(bread)
print(lunch.get_food_value())
lunch.eat()