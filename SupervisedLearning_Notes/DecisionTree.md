# Decision tree

Aim here is to find a decision tree which minimizes the classification error. Exponentially large number of possible trees makes decision tree learning NP hard problem.

## Recursive greedy algorithm

1. start with an empty tree
2. select a feature to split the data [problem: feature split selection]
3. for each split of the tree
    * if nothing more to split make predictions [problem: stopping condition for recursion]
    * else go to step 2 and continue on this split.


### Feature split learning (Decision stump learning)

* for each feature calculate the total classification error on the splitted data.
* pick the feature having the lowest classification error.

### When to stop recursing?

1. All the node in the data has same Y value.
2. or If we run out of features.

## Learning decision tree with continuous inputs

use threshold value to split the data into category.

### Threshold split selection algorithm

1. sort the value of the feature
2. for i in range(N):
    * consider split ti = (Vi + Vi+1)/2
    * Compute the classification error for the ti
3. Select the threshold value with the lowest error


# TODO

## Difference between Classification and regression

### ID3
Method

Concept of Entropy

Information gain

Linearly seperable data

Multiple linear questions

Coding a decision tree

Data impurity and Entropy

Minimizing impurity in splitting

Entropy calculation

Information gain

Tuning criterion parameter

DT strngth and weaknesses