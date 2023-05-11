def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):

            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")


        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    x = input("Введите название ресторана :")
    y =input("Введите название кухни")
    res = Restaurant(x,y)


    res.open_restaurant()
    res.describe_restaurant()



def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Италиано", "итальянскую")
    restaurant2 = Restaurant("Суши Хаус", "японскую")
    restaurant3 = Restaurant("Шашлычная №1", "кавказскую")


    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}. Рейтинг: {self.rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

    restaurant1 = Restaurant("Италиано", "итальянскую", 4.5)
    restaurant2 = Restaurant("Суши Хаус", "японскую", 4.0)
    restaurant3 = Restaurant("Шашлычная №1", "кавказскую", 3.8)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant1.update_rating(4.8)
    restaurant1.describe_restaurant()
