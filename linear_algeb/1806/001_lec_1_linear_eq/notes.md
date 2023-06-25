

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
    \begvin{bmatrix} 2 & -1 \\ 
                    -1 & 2 
    \end{bmatrix} 
    
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

Lets draw a row picture of this. For the  equation $2x -y & = & 0$ We can draw a picture as following

![First equation picture](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/row_pic_y_2x.png)


If we plot the second equation $ -x + 2y = 3 $ here along with $ 2x -y = 0$ then we have following picture.
![Second equation picture](https://github.com/awanm2/math/blob/main/linear_algeb/1806/001_lec_1_linear_eq/src/row_pic_y_2x_plus_other.png)

In this picture, the intersection of the two lines is the solotion to the system of the linear equations.



# Links 
[1. The Geometry of Linear Equations](https://www.youtube.com/watch?v=J7DzL2_Na80)
