import pandas as pd

numbers = [4.43, 2.23, 23.5, 22.1]

s = pd.Series(numbers)
print(s)

# sum numbers
print(s.sum())

# sum values and divide by the total numbers available
print(s.mean())

print(s.product())
