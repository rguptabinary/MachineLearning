# Regression

Regression is a methodology  of supervised learning where we try to find a mathematical relation (in the form of model) between continuous inputs and outputs (not discrete).

We aim to have a function approximation of the relationship between the input and output (continuos data).

The main challenge here is to find a best surface or line fitting the data. We can use calculus to minize the error here and better approximate the fit.

It's important we carefully select the rrder of polynomial we are fitting over the data. We don't want our model to be very simple (low order polynomial) and have bias, also we don't want it to overfit (high order polynomial) and have high variance.

````python
    X w = Y
    X.t X w = X.t Y
    w = (X.t X)^-1 X.t Y
````

Data on which we are making model may have inherent errors because of different reasons. e.g. sensor errors, false dat points, transcription errors etc.

We need a model which is complex enough to find patterns in the data but general enough to make predictions on unseen data. Using cross validation data we can tackle this problem. Further we can use k fold cross validation to further improve the reliablity/accuracy of the model.

### Parametric regression
It's a way of building a model based on parameters. After traing we can use this equation, put our input and get the predictions. No nedd to store all the training values. But we have to retrain our model every time some new data is added to dataset. Training is slow but predictions are fast. Useful when we are able to see some mathematical relationship between input and output.

### K nearest neighbours (Instance based)
In this method we identify k nearest points (x) of a given point and use the mean of their y values. One advantage is training is fast but we have to store all the data. It fits the data very well.

### Kernel regression (Instance based)
In this instead of taking mean of k nearest neighbour we wait the contribution of each points based on how distant they are.