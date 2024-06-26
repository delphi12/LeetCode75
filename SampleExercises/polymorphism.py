class MyClass:
    def method(self, x):
        print(f"Method with one argument {x}")

    def method(self, x, y):
        print(f"Method with two arguments {x} {y}")


MyClass1 = MyClass()
MyClass1.method(10,20)