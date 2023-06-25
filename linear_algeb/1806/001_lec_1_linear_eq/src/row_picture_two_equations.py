import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(-10,10,1))
y = 2*x 

# Create the plot
plt.plot(x,y,label='2x - y = 0')


plt.title('Row picture')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(alpha=.4,linestyle='--')
plt.legend()

plt.savefig('row_pic_y_2x.png', bbox_inches='tight')

plt.plot(x,  (3+x)/2 ,label='-x + 2y = 3') 
plt.legend() 

plt.savefig('row_pic_y_2x_plus_other.png', bbox_inches='tight')

plt.show()
