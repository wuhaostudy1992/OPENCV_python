'''
1. Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
2. Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for
vector operations.
3. Exploit the cache coherence.
4. Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.
Even after doing all these operations, if your code is still slow, or use of large loops are inevitable, use additional
libraries like Cython to make it faster.
'''
