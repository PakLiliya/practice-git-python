# 1. Iterator using iter() and next()  (W3Schools example)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# 2. Loop through an Iterator (W3Schools example)

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


# 3. Create an Iterator (Class with __iter__ and __next__) (W3Schools example)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# 4. Generator using yield (GeeksforGeeks example)

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)


# 5. Generator Expression (W3Schools example)

mygenerator = (x * x for x in range(5))

for i in mygenerator:
    print(i)