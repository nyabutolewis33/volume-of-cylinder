pi = float(input("Enter pi: "))
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

def volume_of_cylinder(pi, r, h):
    volume = pi * (r * r) * h
    print("Volume is", volume)

volume_of_cylinder(pi, r, h)