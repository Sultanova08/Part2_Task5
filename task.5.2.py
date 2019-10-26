class_a = int(input("Enter the number of the students in A class: "))
class_b = int(input("Enter the number of the students in B class: "))
class_c = int(input("Enter the number of the students in C class: "))

class_a += 1
class_b += 1
class_c += 1
class_a //= 2
class_b //= 2
class_c //= 2
print(
    "For the A class we need {0} desks\nFor the B class we need {1} desks\nFor the C class we need {2} desks\n ".format(
        class_a, class_b, class_c
    )
)
print(" Desks in total: " + str(class_a + class_b + class_c))
    ``