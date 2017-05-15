# Notes

## Numpy

[Notes of content (link)](http://www.scipy-lectures.org/intro/numpy/index.html)

1. Definition

    Numpy provides extension package for python for multidimensional array. It provides memory efficient containers (closer to hardware) for fast numeric computations.

    ```python
    # Manyfold better time complexity than python lists
    a = np.arrange(1000)
    %timeit a**2
    ```

2. Getting help

    We can use the below functions to get help and documentation for numpy fn/objects.
    ```python
    # For help
    np.array?
    np.con*?
    np.lookfor('create array')
    ```

3. Creating numpy arrays
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

4. Indexing

    For numpy array indexing works same as python sequences.
    ```Python
    # 1D array, below will return the element at corresponding index
    a[3], a[-1] # last element

    # 2D array, to get a pirticular element we have to give index like
    a[2,2]

    # 2D array,  below will return all elements at the give index
    a[1] # returns [1, 2, 3, 4, 5]

    # reversing a list
    a[::-1] # a[start, end, step]
    ```

5. Slicing

    Numpy array can be sliced like other python sequences
    ```Python
    a[start: end: step]
    # Default values of start = 0, end = last, step = 1
    ```

6. Views

    Slicing just create a view over the array data, i.e. memory is shared.
    ```Python
    np.may_share_memory(a, b) 
    # To check if two np array share memory
    ```

7. Copies

    ```Python
    a[::2].copy()
    ```

8. Boolean mask, indexing with array of index

    ```Python
    # Boolean mask
    mask = (a > 3) # Creates a boolean array of same size
    
    extract_from_a = a[mask]
    # Above create copies not views

    # Assigning new values to sub-array
    a[a % 3 == 0] = -1

    # Indexing with array: same index can be repeated many times
    a[[2, 3, 2, 4, 2]]  
    # note: [2, 3, 2, 4, 2] is a Python list

    # assigning values
    a[[1, 2]] = 3
    ```

Numerical operations on numpy arrays

1. Elementwise operations

    ```Python

    ```

2. Reductions

    ```Python

    ```

3. Broadcasting

    ```Python

    ```

4. Elementwise operations

    ```Python

    ```

5. Shape manipulation

    ```Python

    ```

6. Sorting

    ```Python

    ```
