import numpy as np
import pandas as pd
import random

def create_repeated_measure_df(num_size,num_repeat, y_x_beta, w_x_beta, w_z1_beta, w_z2_beta, int_y, int_w, s_y, s_x, s_me, seed=219):
    """create_repeated_measure_df
    args:
    """
    np.random.seed(seed=seed)
    df = pd.DataFrame()
    id = []
    point =[]
    y = []
    x = []
    w = []
    z1 = []
    z2 = []

    for i in range(num_size):
        z1_i=  np.random.binomial(1, 0.4)
        z2_i=  np.random.normal(30, 5)
        x_i = random.normalvariate(i, s_x)
        y_i = int_y + y_x_beta * x_i + random.normalvariate(0, s_y)
        for j in range(num_repeat):
            w_ij = int_w + w_x_beta * x_i + w_z1_beta * z1_i + w_z2_beta * z2_i + random.normalvariate(0, s_me)
            id.append(i+1)
            point.append(j+1)
            y.append(y_i)
            x.append(x_i)
            w.append(w_ij)
            z1.append(z1_i)
            z2.append(z2_i)
    df['id']= id
    df['point'] = point
    df['y'] = y
    df['x'] = x
    df['w'] = w
    df['z1'] = z1
    df['z2'] = z2 
    return df


if __name__ == '__main__':
    df = create_repeated_measure_df(num_size=100, num_repeat= 3, y_x_beta=2, w_x_beta= 0.9, w_z1_beta= 0.3, w_z2_beta=0.1, int_y=3, int_w=0.1, s_y = 2, s_x=1, s_me=0.2)
    print(df)