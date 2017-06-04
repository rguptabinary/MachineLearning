# Linear classifiers

While building a linear classifier we are trying to predict a decison boundary which can seperate input data to some given classes. For example, in sentiment analysis of reviews we would like to have a hyperplane which can classify a review as positive or negative based on its word features.

`Generalized linear models` are the models in which we squash the score between [0,1] to output a probability of a label given a review. `Sigmoid` is one of the function we can use.

## Learning algorithms for logistic regression (Gradient Ascent)

Approach here is to start with some random weights (selected smartly) and follow the gradient till we reach an optimal value.
Our quality metric (ikelihood function) here is a multiplication of probabilities for Xi in our dataset.

```python
init W(1) at t=1
while ||gradient of likelihood fn|| < tolerance:
    for j in range(0,D):
        partial[j] = calculate partial derivative of likelihood fn wrt W(j) at one time stamp before
        w[j](t+1) = w[j](t) + alpha * partial[j]
    t += 1
```

### Chossing learning rate(alpha) for gradient descent/ascent



