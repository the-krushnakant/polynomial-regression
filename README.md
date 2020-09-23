# polynomial-regression
The Polynomial Regression Module

Noticeably faster implementation than numpy.polyfit .

Uses the computational power of numpy. (to be faster than numpy :)) )

Hosted on pypi- https://pypi.org/project/polynomial-regression/

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

It returns a numpy.ndarray of len=n+1 , where c[i] is the coefficient of x\*\*i (x to the power of i) in the best fit polynomial of degree n.

For example, if you provide x,y,2 ; then the returned ndarray c will be such that c[0]+c[1]*x+c[2]*x*x is the best fit polynomial of degree 2 for y.

-------------------------------------------------------------------------------------

The Following Graph has time on y-axis and run number on x-axis. It shows time taken by pr.regress (in blue) and np.polyfit (in orange) to perform polynomial regression for 60000 length arrays x and y, for degree=1 (Linear Regression). You can see that pr.regress is about 6 to 7 times faster. 

![Degree 1](https://github.com/the-krushnakant/polynomial-regression/blob/master/degree1.png?raw=true)

For degree=2, i.e. quadratic regression, pr.regress is about 4 to 5 times faster.

![Degree 2](https://github.com/the-krushnakant/polynomial-regression/blob/master/degree2.png?raw=true)

