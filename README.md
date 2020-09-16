# polynomial-regression
The Polynomial Regression Module

See Usage at-  https://github.com/the-krushnakant/polynomial-regression

-----------------------------------------------------------------------------------


Usage:
-----------------------------------------------------------------------------------


To install:

`pip3 install --upgrade polynomial_regression`

-----------------------------------------------------------------------------------

In your file, to use polynomial_regression, import like this:

`from polynomial_regression.polyregress import polynomial_regression as pr`

`coefficients=pr.regress(x,y,n)`

Here, x should be the list(preferred type=ndarray) of x co-ordinates, and y, of y co-ordinates of the points you need to fit to a n-degree curve. 

len(x) should be equal to len(y) and n must be lesser than or equal to both.



