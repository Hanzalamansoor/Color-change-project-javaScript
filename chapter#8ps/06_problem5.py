# 6. Write a python function which converts inches to cms.
def conversion(n):
  i =  n
  cm = i * 2.54
  return f"The converted value is {cm}cm"

final = conversion(6)
print(final)