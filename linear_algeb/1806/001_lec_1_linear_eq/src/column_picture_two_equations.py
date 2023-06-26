import matplotlib.pyplot as plt
import numpy as np

V = np.array([[2,-1], [-1,2], ])
origin = np.array([[0, 0],[0, 0]]) # origin point
plt.quiver(*origin, V[0][0], V[0][1], color=['r'], label='col1', scale=15)
plt.quiver(*origin, V[1][0], V[1][1], color=['b'], label='col2', scale=15)

plt.title('Column picture')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(alpha=.4,linestyle='--')
plt.legend()

plt.savefig('column_pic_two_cols.png', bbox_inches='tight')

vsum = V[0] + 2*V[1]
plt.quiver(*origin, vsum[0], vsum[1], color=['g'], label='col1 + 2*col2', scale=15)
plt.legend() 
plt.savefig('column_pic_two_cols_soln.png', bbox_inches='tight')

plt.show()
