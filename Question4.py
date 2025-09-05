# Dog class
class Dog:
    def make_sound(self):
        return "Woof! 🐶"

# Cat class
class Cat:
    def make_sound(self):
        return "Meow! 🐱"

# Function that works with any object that has make_sound()
def process_sound(sound_object):
    print(sound_object.make_sound())

# Example usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    process_sound(dog)  # Output: Woof! 🐶
    process_sound(cat)  # Output: Meow! 🐱
