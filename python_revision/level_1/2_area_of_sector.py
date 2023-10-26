# Python program to find Area of a Sector
  
def SectorArea(radius, angle):
    pi = 22 / 7
      
    # Constraint or Limit
    if angle >= 360:
        print("Angle not possible")
        return
      
    # Calculating area of the sector
    else:
        sector = (pi * radius ** 2) * (angle / 360)
        print(sector)
        return
  
# Driver code 
radius = int(input('Enter radius of sector : '))
angle = int(input('Enter the angle of the sector : '))
SectorArea(radius, angle)
