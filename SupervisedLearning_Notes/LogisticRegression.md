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


### Overfitting in classification

* when model does good on training data but gives high true error (on test data).
* large coefficient values can lead to overfitting in classification ie making model too certain about it's predictions.
* Penalize large coefficient values to avoid overfitting, we have to balance below equation.

Total quality = measure of fit ( data likelihood: large #, good fit to training data) - measure of magnitude of coefficients (large # = overfit)

#### # indicative of size of logistic regression coefficients

1. Sum of squares (L2 norm): W1^2 + W2^2 + ......
2. Sum of absolute values (L1 norm): |W1| + |W2| + .....

Both L1 and L2 norms penalizes large coefficients but L1 norm gives sparse solution.

#### L2 regularized logistic regression

* maximize l(w) - lambda*||w||^2
* Pick lambda using
1. validation set (for larger datasets)
2. cross-validation (for smaller datasets)
* When lambda is very large weights variance bias
* very small






