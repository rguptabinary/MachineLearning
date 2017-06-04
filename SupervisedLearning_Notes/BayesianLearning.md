# Bayesian network

* BN is a directed acyclic graphs whose nodes represents the random variables (X1, X2, X3,..., Xn).
* For each node Xi we have a CPD with parent nodes.
* A BN represents a joint probability distribution via the chain rule for bayesian network.

### Active trails in a BN

A trail X1, X2, X3,..., Xn is active given Z if

* we have an activated v structure, ie for any v structure (Xi-1 -> Xi <- Xi+1), Xi or its descendants belongs to Z.
* no other Xi is in Z.

### Naive Bayes

Aim of a machine learning algorithm is to predict a decision surface on the given data. This decision surface seperates one class from the other class, in a way it generalize to the data not seen before.

### Bayesian learning

Learn the best (most probable) hypothesis on a given Data given some domain knowledge.

argmax Pr(h | D), h E H, D E Data, H is all hypothesis space.

[Conditional probability](https://www.khanacademy.org/math/statistics-probability/probability-library#conditional-probability-independence)

P(h|D) = [ P(D|h) * P(h) ] / P(D)

* P(h|D) : probability of some hypothesis given some data.
* P(D)   : our prior belief of seeing some data (domain knowledge).
* P(D|h) : data given the hypothesis, likelihood of seeing some data in a world where we know a hypothesis is true. Given the x what's the probability to see a pirticular label. We can also imagine it selecting a hypothesis how accurately it is labeling the data.
* P(h)    : It's our prior beleif a pirticular hypothesis is better than other (domain knowledge). It tends to assign higher probability to hypothesis grouping things in a pirticular way.


#### Cites

[Daphne Koller course on Coursera](https://www.coursera.org/learn/probabilistic-graphical-models)