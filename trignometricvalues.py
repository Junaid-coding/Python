import math
angle_deg = float(input("Enter the angle in degrees"))
angle_rad = math.radians(angle_deg)
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)
print("Sin(", angle_deg, ") =", sin_val)
print("Cos(", angle_deg, ") =", cos_val)
print("Tan(", angle_deg, ") =", tan_val)