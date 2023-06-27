

# Notes
## Row picture for two equations
Let's say we have following two equations

```math
\begin{array}{lcl} 
    2x -y & = & 0 \\ 
    -x + 2y & = & 3\end{array}
```
Now this can be written as a matrix notation

```math 
    \begin{bmatrix} 2 & -1 \\ 
                    -1 & 2 
    \end{bmatrix} 
    \times
    \left[ 
    \begin{array}{c} x \\ y \end{array} 
    \right] 
    =
    \left[ \begin{array}{c} 0 \\ 3 \end{array} 
    \right]
```
So we can write it as 
```math 
Ax = b
``` 

where A is matrix, x is vector of unknowns and b is the vector on the right side.

Lets draw a row picture of this. For the  equation $`2x -y  =  0`$ We can draw a picture as following

![First equation picture](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/row_pic_y_2x.png)


If we plot the second equation $` -x + 2y = `3 $ here along with $` 2x -y = 0`$ then we have following picture.
![Second equation picture](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/row_pic_y_2x_plus_other.png)

In this picture, the intersection of the two lines is the solotion to the system of the linear equations.

## Column Picture

We can write the above system of linear equations as a column picture

```math 
    x
    \left[ 
    \begin{array}{c} 2 \\ -1 \end{array} 
    \right]
    + 
    y
     \left[ 
    \begin{array}{c} -1 \\ 2 \end{array} 
    \right]
    =
    \left[ \begin{array}{c} 0 \\ 3 \end{array} 
    \right]
```    

So we can find the linear combination of x and y that will statisfy our system of linear equation. 
First we can draw column picture of col1 and col2 as below (not to scale)
![two columns plotted](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/column_pic_two_cols.png)

Then we can combine col1 and col2, here take one of col1 and 2 of col2 to get the answer - which we know from row picture section. 
(not to scale)
![two columns with soln](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/column_pic_two_cols_soln.png)

The green vector is the solotion of vector col1 and col2.

## Equation with 3 variables 

Now lets think about equations with 3 unknowns. Say following equation 
```math
\begin{array}{lcl} 
    2x -y & = & 0 \\ 
    -x + 2y -3z & = & -1 \\
       -3y  +4z & = & 4 \\
    
    \end{array}
```

We can write this as 
So we can write it as 
```math 
Ax = b\\ 
A = \begin{bmatrix} 2 & -1 & 0\\ 
                    -1 & 2 & -1 \\
                    0 & -3 & 4\\  
    \end{bmatrix} \\
b = \left[ 
  \begin{array}{c}  0 \\ -1 \\ 4 \end{array} 
  \right] \\
x = \left[ 
  \begin{array}{c}  x \\ y \\ z \end{array} 
  \right] \\
``` 

For this equation, the row picture for one of the equaion $` -x + 2y -z = -1 `$. If we plot all the points that solve the equation will form a plane. 
Each row in a 3 x3 matrix gives us a plane in 3 dimensions. If we have the equation in 3 dimensions, then we have two planes intersecting at some point, then 
intersection of those two planes give us a line. if all three planes intersect, they meet at a point and that is the solotion. Row picture is hard to visualize 
for more than 3 dimesions. 

Now lets write a column picture for above equations


```math 
    x
    \left[ 
    \begin{array}{c} 2 \\ -1 \\ 0\end{array} 
    \right]
    + 
    y
     \left[ 
    \begin{array}{c} -1 \\ 2 \\ 3\end{array} 
    \right]
    +
    z
     \left[ 
    \begin{array}{c} 0 \\ -1 \\ 4\end{array} 
    \right]
    =
    \left[ \begin{array}{c} 0 \\ -1 \\ 4 \end{array} 
    \right]
```    

Here the linear combination of the three vectos with right combination will produce b. Here x = 0, y=0 and z = 4.

Another question is can I always solve for $`Ax=b`$ ? Do the linear combinations of the column fill 3 dimensional space ?

One goal we have is to take linear combinations of the vectos and trying to find b. 

There are times when one might not be able to produce a solotion for $`b`$.  

If the 3 columns are in same plane then the combination is in same plane. We can solve if b is in same plane  as all the vectors in $`A`$. 
But if b is not in the same plane as vector in A (in this particular) case then b is not reachable. So here matrix A is not invertible and anwer will be NULL.

## Matrix Multiplication

Back to our equation $`Ax=b`$. We have to multiply a matrix with a vector. Say 

```math
\begin{bmatrix} 2 & 5 \\ 
                1 & 3 
    \end{bmatrix} 
    \left[ 
    \begin{array}{c} 1 \\ 2 \end{array} 
    \right] 
```

Using column picture we can do following 

```math
    1 \left[  \begin{array}{c} 2 \\ 1 \end{array} \right] 
    + 
    2 \left[  \begin{array}{c} 5 \\ 3 \end{array} \right] 
    = 
    \left[  \begin{array}{c} 12 \\  7 \end{array} \right] 
```

So $`Ax`$ is linear combination of columns of $`A`$.

We can also do it using rows and dot product.

# Links 
[1. The Geometry of Linear Equations](https://www.youtube.com/watch?v=J7DzL2_Na80)
