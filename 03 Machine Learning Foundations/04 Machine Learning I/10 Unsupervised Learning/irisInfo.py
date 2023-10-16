#import codecademylib3_seaborn
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()

'''
Column 0: Sepal length
Column 1: Sepal width
Column 2: Petal length
Column 3: Petal width
'''
print(iris.data)
print("--------")
print(iris.target)
print("--------")
print(iris.data[0, :], iris.target[0])
print("--------")
print(iris.DESCR)