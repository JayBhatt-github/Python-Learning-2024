# Static Method in Python

class MyClass:
    # This is a static method. It does not have access to the class or instance.
    @staticmethod
    def staticMethod():
        print("This is a static method. It does not have access to the class or instance.")

# Calling the static method without creating an instance of the class.
MyClass.staticMethod()
