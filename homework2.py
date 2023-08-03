#Створити клас Human, в якому визначити метод drink.
#При ініціалізації, приймати вік людини; створити поле класу favorite_drink зі значенням 'beer'.

class Human:

    favorite_drink = 'beer'

    def __init__(self, age):
        self.age = age

    def drink(self):
        favorite_drink = self.favorite_drink  
        if self.age < 18:
            favorite_drink = 'juice'
        print(favorite_drink)
        print(f'Human likes to drink {favorite_drink}')
        
#Створити клас Worker, віднаслідувавши його від Human, та додавши при ініціалізації зарплату
        
class Worker(Human):
    
    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if self.salary > 1000:
           self.favorite_drink = 'whiskey'

human1 = Human(77)
human1.drink()  

human2 = Human(17)
human2.drink()  

worker1 = Worker(45, 1001)
worker1.drink()  

worker2 = Worker(22, 800)
worker2.drink()