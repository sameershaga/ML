import numpy as np
X = np.array([[1, 2, 3], [10, 20, 30], [5, 5, 5], [4, 0, 0]])
y = np.array([0, 1, 1, 0])
classes = np.unique(y)
num_classes = len(classes)

means = []
for c in classes :
    means.append(np.mean(X[y==c], axis = 0))

means =np.array(means)
print(means)
test_example=np.array([1, 1, 1])
print(np.sum((means - test_example)**2, axis=1) ** 0.5)
