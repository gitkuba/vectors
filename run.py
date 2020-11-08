from vector import Vector
import math

if __name__ == "__main__":
    print("\n>Adding example")
    vector_one = Vector([8.218, -9.341])
    vector_two = Vector([-1.129, 2.111])
    resultVector = vector_one.add(vector_two)
    print("Adding result is " + str(resultVector))

    print("\n>Substract example")
    vector_one = Vector([7.119, 8.215])
    vector_two = Vector([-8.223, 0.878])
    resultVector = vector_one.substract(vector_two)
    print("Substract result is " + str(resultVector))

    print("\n>Multiply example")
    vector = Vector([1.671, -1.012, -0.318])
    resultVector = vector.multiply(7.41)
    print("Multiply result is " + str(resultVector))

    print("\n>Magnitude example")
    vector = Vector([-0.221, 7.437])
    print("Magnitude 1 is " + str(vector.magnitude()))

    vector = Vector([8.813, -1.331, -6.247])
    print("Magnitude 2 is " + str(vector.magnitude()))

    print("\n>Normalization example 1")
    vector = Vector([5.581, -2.136])
    print("Normalization 1: " + str(vector.normalize()))

    print("\n>Normalization example 2")
    vector = Vector([1.996, 3.108, -4.554])
    print("Normalization 2: " + str(vector.normalize()))

    print("\n>Dot product example 1")
    vector_one = Vector([7.887, 4.138])
    vector_two = Vector([-8.802, 6.776])
    dot_product = vector_one.dot_product(vector_two)
    print("Dot product 1: " + str(dot_product))

    print("\n>Dot product example 2")
    vector_one = Vector([-5.955, -4.904, -1.874])
    vector_two = Vector([-4.496, -8.755, 7.103])
    dot_product = vector_one.dot_product(vector_two)
    print("Dot product 2: " + str(dot_product))

    print("\n>Angle example 1")
    vector_one = Vector([3.183, -7.627])
    vector_two = Vector([-2.668, 5.319])
    angle = vector_one.angle(vector_two)
    print(
        "Angle 1 is " + str(angle) + " rad / " + str(math.degrees(angle)) + " degrees"
    )

    print("\n>Angle example 2")
    vector_one = Vector([7.35, 0.221, 5.188])
    vector_two = Vector([2.751, 8.259, 3.985])
    angle = vector_one.angle(vector_two)
    print(
        "Angle 2 is " + str(angle) + " rad / " + str(math.degrees(angle)) + " degrees"
    )

    print("\n>Parallelism & Orhogonality exemple 1")
    vector_one = Vector([-7.579, -7.88])
    vector_two = Vector([-22.737, 23.64])
    print("V1 and V2 orthogonal: " + str(vector_one.is_orthogonal_to(vector_two)))
    print("V1 and V2 parallel: " + str(vector_one.is_parallel_to(vector_two)))

    print("\n>Parallelism & Orhogonality exemple 2")
    vector_one = Vector([-2.029, 9.97, 4.172])
    vector_two = Vector([-9.231, -6.639, -7.245])
    print("V1 and V2 orthogonal: " + str(vector_one.is_orthogonal_to(vector_two)))
    print("V1 and V2 parallel: " + str(vector_one.is_parallel_to(vector_two)))

    print("\n>Parallelism & Orhogonality exemple 3")
    vector_one = Vector([-2.328, -7.284, -1.214])
    vector_two = Vector([-1.821, 1.072, -2.94])
    print("V1 and V2 orthogonal: " + str(vector_one.is_orthogonal_to(vector_two)))
    print("V1 and V2 parallel: " + str(vector_one.is_parallel_to(vector_two)))

    print("\n>Parallelism & Orhogonality exemple 4")
    vector_one = Vector([2.118, 4.827])
    vector_two = Vector([0, 0])
    print("V1 and V2 orthogonal: " + str(vector_one.is_orthogonal_to(vector_two)))
    print("V1 and V2 parallel: " + str(vector_one.is_parallel_to(vector_two)))
