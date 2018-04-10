#Python program to convert lists to list of dictionaries.
import sys 
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#0000000", "#FF0000", "#80000", "#FFF00"]
print([{'color_name': f, 'color_code': c} for f , c in zip(color_name, color_code)])
