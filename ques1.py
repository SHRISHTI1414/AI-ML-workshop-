import numpy as np
robot_parts=np.array([5,10,15,20])
needed_parts=np.array([3,8,10,18])
extra_parts=np.array(robot_parts-needed_parts)
print(extra_parts)