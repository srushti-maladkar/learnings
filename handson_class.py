# class Employee(object):
#     _id = "IN_123"
#     name = "XYZ"
#     employer = "Google"
#     location = "Mumbai"

#     def eat(self):
#         print("Eating...")

#     def typee(self):
#         print("Coding coding coding...")

#     def leave(self):
#         print("Sick leave...")
#         print("Sick leave...")


# sm = Employee()
# print(sm.name)
# print(sm._id)
# print(sm.location)
# print(sm.employer)
# print(sm.eat())
# print(sm.typee())
# print(sm.leave())
# print

print("Single Level Inheritence")


class Grandparent:
    skill = "Drawing"


class Parent(Grandparent):
    Grandparent.skill


sm = Parent()
print(sm.skill)


print("Multilevel Inheritence")


class Grandparent:
    print("I am Grandparent...")


class Parent(Grandparent):
    print("I am Parent...")


class Child(Parent):
    print("I am child...")


(Child())


print("Multilevel Inheritence")


class Mother:
    print("I am Mum...")


class Father:
    print("I am Pop...")


class Brother:
    print("I am Bro...")


class Me(Father, Mother, Brother):
    print("I am Child...")


(Me())


print("Hierarchical Inheritance")


class SomeGrandParent:
    print("I am SomeGrandParent...")


class Uncle(SomeGrandParent):
    print("I am Uncle...")


class Aunty(SomeGrandParent):
    print("I am Aunty...")


(Aunty())


print("Hybrid Inheritence")


class God:
    print("I am God...")


class Mother(God):
    print("I am Mum...")


class Father(God):
    print("I am Papa...")


class Child(Father, Mother):
    print("I am Child")


(Child())
