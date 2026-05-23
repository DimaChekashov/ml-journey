import numpy as np

W1 = np.random.randn(3, 4)
X = np.random.randn(5, 3)

output = X @ W1

W1_T = W1.T
print(W1_T.shape)

dot = np.dot(X[0], X[1])
print(dot)

Q = np.random.randn(1, 4)
K = np.random.randn(6, 4)
V = np.random.randn(6, 8)

scores = Q @ K.T

d_k = K.shape[1]
scores_scaled = scores / np.sqrt(d_k)

def softmax(x):
    e = np.exp(x - x.max())
    return e / e.sum()

weights = softmax(scores_scaled)

output = weights @ V
print(output.shape)