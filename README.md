# polynomial-regression
The Polynomial Regression Module

Noticeably faster than numpy.polyfit or numpy.Polynomial.polynomial.polynomial.fit for small and large ndarrays alike.

Uses the computational power of numpy. (to be faster than numpy lol!)

See Usage at-  https://github.com/the-krushnakant/polynomial-regression

-----------------------------------------------------------------------------------


Usage:
-----------------------------------------------------------------------------------


To install:

`pip3 install polynomial_regression`


-----------------------------------------------------------------------------------

In your file, to use polynomial_regression, import like this:

`from polynomial_regression.polyregress import polynomial_regression as pr`

`coefficients=pr.regress(x,y,n)`

Here, x should be the list(preferred type=ndarray) of x co-ordinates, and y, of y co-ordinates of the points you need to fit to a n-degree curve. 

len(x) should be equal to len(y) and n must be lesser than or equal to both.

It returns a np.ndarray of len=n+1 , where c[i] is the coefficient of x\*\*i (x to the power of i) in the best fit polynomial of degree n.


-------------------------------------------------------------------------------------

![alt text](https://github.com/the-krushnakant/polynomial-regression/blob/master/degree1.png?raw=true)
