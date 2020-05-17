import numpy as np

#input height in metrics
height = float(input('Enter your height: '))
if 260>height>100:
    height=height*0.01
elif 0.8<height<8.53:
    height=height*30.48

height=round(height,2)
print(height)
