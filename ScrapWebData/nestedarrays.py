# you need to import numpy mododule if you encounter ModuleNotFoundError: run the below command on your terminal
# pip install numpy
import numpy

# pring numpy version
print(numpy.__version__)

matrix = [[1,2,3],[7,8,9], [4,5,6]]
flateend = [num for row in matrix for num in row]
print(flateend)