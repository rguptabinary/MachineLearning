# Naive Bayes

Aim of a machine learning algorith is to predict a drcision surface on the given data. Thus decision surface one class from the other class in a way it generalize to the data not seen before.

### Bayesian learning

Learn the best (most probable) hypothesis given Data and some domain knowledge.

argmax Pr(h | D), h E H, D E Data, H is all hypothesis space.

[Conditional probability](https://www.khanacademy.org/math/statistics-probability/probability-library#conditional-probability-independence)

P(h|D) = [ P(D|h) * P(h) ] / P(D)

* P(h|D) : probability of some hypothesis given some data.
* P(D)   : our prior belief of seeing some data (domain knowledge).
* P(D|h) : data given the hypothesis, likelihood of seeing some data in a world where we know a hypothesis is true. Given the x what's the probability to see a pirticular label. We can also imagine it selecting a hypothesis how accurately it is labeling the data.
* P(h)    : It's our prior beleif a pirticular hypothesis is better than other (domain knowledge). It tends to assign higher probability to hypothesis grouping things in a pirticular way.


