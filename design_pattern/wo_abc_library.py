from abc import ABCMeta, abstractmethod

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def howling(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog, cat = Dog(), Cat()
# print(f'dog: {dog.speak()}, cat:{cat.speak()}')


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def howling(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Woof!"


dog, cat = Dog(), Cat()
print(f'dog: {dog.speak()}, cat:{cat.speak()}')
