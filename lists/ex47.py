#Python prrogram to inset an element before each element of a list 
color = ['Red', 'Green', 'Black']
print("Priginal List: ", color)
color = [ v for elt in color for v in ('c', elt)]
print("Original List: ", color)
