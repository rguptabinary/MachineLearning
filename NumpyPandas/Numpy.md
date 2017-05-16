# Numpy

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

    All arithmetic operations are elementwise.
    ```Python
    # Elementwise operations
    a = np.arrange(5) # [0, 1, 2, 3, 4]

    a +=1 # [1, 2, 3, 4, 5]

    a = a**2 # [1, 4, 9, 25]

    # Comparing two arrays
    a == b # Generates a boolean mask

    np.array_equal(a, b)

    # Matrix multiplication
    a.dot(b)

    # Logical operations, returns boolean mask
    np.logical_or(a, b)

    np.logical_and(a, b)

    # Transpose of a matrix
    b = a.T
    ```

2. Reductions

    ```Python
    # axis = 0: row, axis = 1: column, think of sum as projection of other axis sollapsed on the specified axis
    a.sum(axis=0)

    # Extrema, axis can be provided
    a.max()
    a.min()
    a.argmax() # index of maximum element
    a.argmin() # index of minimum element

    # Logical operations
    np.all(a > 3) # Check conditions on all elements, return true if all are true
    
    np.any(a < 5)
    
    ((a <= b) & (b <= c)).all()
    
    # Statistics
    np.mean(a)

    np.median(a, axis = -1) # last axis from all available axis

    a.std() # Standard deviation
    ```

3. Broadcasting

    All the arithmetic operations in numpy are elementwise. Though it can be done on array of different size if these arrays are transformable using numpy broadcasting.

    ![example](http://www.scipy-lectures.org/_images/numpy_broadcasting.png)
    A lot of grid-based or network-based problems can also use broadcasting. For instance, if we want to compute the distance from the origin of points on a 10x10 grid, we can do below
    ```Python
    x, y = np.arange(5), np.arange(5)[:, np.newaxis]

    distance = np.sqrt(x ** 2 + y ** 2)
    ```

4. Shape manipulation

    ```Python
    # Flattening
    # Last dimension ravels out first
    a = np.array([[1, 2, 3], [4, 5, 6]])
    a.ravel()
    # array([1, 2, 3, 4, 5, 6])
    a.T.ravel()
    # array([1, 4, 2, 5, 3, 6])

    # Reshaping, it may return copy or view
    a.reshape((2, -1))    # unspecified (-1) value is inferred

    # Adding a dimension
    a[:, np.newaxis]

    # Resizing
    # size of a np array can be changed with resize, 
    # ***however it shouldn't be refrenced anywhere
    a = np.arange(4)
    a.resize((8,))
    a
    #array([0, 1, 2, 3, 0, 0, 0, 0])
    ```

5. Sorting

    ```Python
    # Inplace sort
    a.sort(axis=1)

    np.argsort() #indexes of elements in sorted order

    np.argmax() # Index of maximum element

    np.argmin() # Index of minimum element
    ```
