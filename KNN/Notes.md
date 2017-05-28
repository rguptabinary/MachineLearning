# KNN

### Instance based learning

In methods such as regression, given a set of points we aim to learn a function (line, space) which represents the data and then we throw the data away. When we get a point in future we try to predict the labels without any refrence to the original data.

Given a point, to predict price of a house, eg on google maps, we can look in the neighbourhood of this point to find how much other houses were sold for. In pirticular we can look for k nearest neighbours and based on the distances and counts we can estimate which class this pirticular point belongs to. Here distance can mean google map distance, walking distance etc. Here we are using distance as a standard for similarity. We can add other features also (bedroom, bathroom etc) to estimate similarity.

```python
    Given: Training data D = {xi, yi}
           Distance Metric d(q, x) # Representing our domain knowledge representing our notion of simillarity 
           Number of neighbours K
           Query point q
    Find:  NN = { i:d(q, xi) k smallest} # Points closest to query point
    Return:Classification: weighted votes of the yi E NN (weighted based on distances) # Plurality
           Regression: mean of the yi E NN
```

[Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)

In the above algorithm lot of things are left to designes. eg. distance metric, number of nearest numbers. We can take weighted distances of the meighbourhood points, ie enabling us to distinguish the contribution of points based on their distances.

Depending on distance metric (Euclidean, Manhattan etc) we can get different answers.

### KNN Bias

Preference bias: Why we prefer one hypothesis over another (smaller tree, smoother functions). In KNN following are preference biases.

* Locality: In KNN we are taking k nearest points as similar. But the nearest points really depends upon the distance metric used (Euclidean etc). There are good and bad distance metric for a problem, how we chose one depends upon our domain knowledge of the problem.
* Smoothness: by averaging we are assuming the function is smooth.
* All features matter equally: eg in euclidean, manhatten metric we considered equal contribution from x1 and x2.

### Curse of dimensionality

As the number of features or dimension grows, the amount of data we need to generalize accurately grows exponentially.

### Important

* Choice of distance funtion really matters (Euclidean, Manhattan, weighted). Our domain knowledge really matters in defining this distance function in defining simillarity. eg given an image of a person we can line up eyes, hair, nose etc as parameters in our distance function.

* K = n: weighted averages or locally weighted regression, KNN allows to take local information and build concept around it to fit a complicated function.

### Summary

* Instance based learning
* Lazy vs eager learnings
* Nearest neighbour: similarity (way to capture domain knnowledge!)
* Locally weighted functions
* Curses of dimensionality