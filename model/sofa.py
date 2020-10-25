class Sofa:
    def __init__(self,  width_in_cm=0, length_in_cm=0,color="", brand=""):
        self.width_in_cm = width_in_cm
        self.length_in_cm = length_in_cm
        self.color = color
        self.brand = brand

    def __str__(self):
        return f"Sofa:\t width: {self.width_in_cm}, length: {self.length_in_cm},color: {self.color}, brand:{self.brand}"
