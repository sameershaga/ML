import numpy as np
X = np.array([[1, 2, 3], [10, 20, 30], [5, 5, 5], [4, 0, 0]])
y = np.array([0, 1, 1, 0])
X_test = np.array([[10, 10, 10 ]])


from sklearn.preprocessing import StandardScaler
#z-score normalization
scaler = StandardScaler()
print(Xsc := scaler.fit_transform(X))

print()
print()
print(X_test_sc := scaler.transform(X_test))

print(classes := np.unique(y))
num_classes = len(classes)





means = []
for c in classes :
    means.append(np.mean(Xsc[y==c], axis = 0))

means =np.array(means)
print()
print()
print(means)
print()
print()
#test_example=np.array([1, 1, 1])
print(np.sum((means - X_test_sc)**2, axis=1) ** 0.5)
