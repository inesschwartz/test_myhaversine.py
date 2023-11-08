#practice from lecture 5

def main():
    x = int(input("What's x? "))
    print("x square rooted is", sqrt(x))

#definition of mysqrt
def sqrt(n):
    return n ** 0.5
if __name__ == "__main__":
    main()

#write test cases for  five functions: mysqrt, mycos, myarcsin, mysin, and myhaversine

def main():
    x = int(input("What's x? "))
    print("x square rooted is", sqrt(x))

#definition of mysqurt
def sqrt(n):
    return n ** 0.5
if __name__ == "__main__":
    main()


#def of myarcsin
def myarcsin(x):
    if x < -1:
        return -90  # If x is less than -1, the result is -90 degrees
    elif x > 1:
        return 90   # If x is greater than 1, the result is 90 degrees

    # For values between -1 and 1, calculate the approximate arcsin
    radians = 0  # Initialize the result in radians
    n = 1
    term = x

    while term != 0:
        radians += term
        n += 2
        term *= (x ** 2) * (-1) * (n - 2) / (n * (n - 1))

    degrees = radians * (180 / 3.14159265359)  # Convert radians to degrees
    return degrees

# Example usage:
x = 0.5  # Replace with the value for which you want to calculate arcsin
arcsin_value = myarcsin(x)
print(f"The arcsin of {x} is approximately {arcsin_value} degrees")


#def mysin
def mycos(angle_degrees):
    # Convert the angle from degrees to radians
    angle_radians = angle_degrees * (3.14159265359 / 180)  # Approximate value of pi

    # Initialize the cosine value
    cosine_value = 1  # The initial value of cosine for n = 0

    # Calculate the cosine using a Taylor series expansion
    n = 2
    term = angle_radians ** 2
    sign = -1

    while term != 0:
        cosine_value += (sign * term) / n
        n += 2
        term *= (angle_radians ** 2) * (angle_radians ** 2) / (n * (n - 1))
        sign *= -1

    return cosine_value

# Example usage:
angle_degrees = 60  # Replace with the angle in degrees for which you want to calculate cosine
cosine_value = mycos(angle_degrees)
print(f"The cosine of {angle_degrees} degrees is approximately {cosine_value}")


#def myhaversin

#create a file for all of these to be tested using pytest
#install pytest