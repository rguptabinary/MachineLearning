# Notes

## Numpy
Numpy provides extension package for python for multidimensional array. It provides memory efficient containers (closer to hardware) for fast numeric computations.

```python
# Manyfold better time complexity than python lists
a = np.arrange(1000)
%timeit a**2
```
We can use the below functions to get help and documentation for numpy fn/objects.
```python
# For help
np.array?
np.con*?
np.lookfor('create array')
```

Creating numpy arrays
```python
# By passing an array
a = np.array([1, 2, 3])

a = np.array([[1, 2, 3], [4, 5, 6]])

# end is exclusive
a = np.arrange(start, end, steps)

a = np.arrange(10) # [0, 1, 2,...., 8, 9]

a = np.linspace(start, end, num_points)

# Common array
a = np.zeros((3, 3))

a = np.ones((3, 3))

a = np.eye(5) # Identity matrix

a = np.diag([1, 2, 3, 4, 5]) # Diagonal matrix

# Random array
a = np.random.rand(size) # Uniform in [0,1]

a = np.random.randn(size) # Gaussian distribution

a = np.empty(shape) # faster than np.zero as it doesn't initialize each values to zero, left for user.

# Seeding, so that it produce same random numbers, useful for debugging
np.random.seed(123)
```
[Identity matrix](https://en.wikipedia.org/wiki/Identity_matrix)

[Diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix)

