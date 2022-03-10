
import pandas as pd
import numpy as np
frames=[]
# 1st dim == frame num, 2nd dim == xforce grid(0), yforce grid(1), zforce grid(2)
# Each grid is 2 dim array. 1st dim is row, 2nd dim is column of pillars.

def get_grids(pillar_data):
    xgrid=np.empty(0)
    ygrid=np.empty(0)
    zgrid=np.empty(0)
    for i, pillar in enumerate(pillar_data):
        pillar_list = pillar.split('\r\n')
        fx = pillar_list[10].split(':')
        fx = float(fx[1])
        fy = pillar_list[11].split(':')
        fy = float(fy[1])
        fz = pillar_list[12].split(':')
        fz = float(fz[1])
        xgrid = np.append(xgrid,fx)
        ygrid = np.append(ygrid,fy)
        zgrid = np.append(zgrid,fz)
    xgrid = list(xgrid.reshape(3,3))
    ygrid = list(ygrid.reshape(3, 3))
    zgrid = list(zgrid.reshape(3, 3))
    return xgrid,ygrid,zgrid

def main():
    name_of_csv_file_written = 'hub_0-sensor_0.csv'
    dataframe = pd.read_csv(name_of_csv_file_written)
    data = dataframe.to_numpy()
    for sample in data:
        pillar_data = sample[6]
        pillar_data = pillar_data.strip('[]')
        pillar_data = pillar_data.split(',')
        xgrid, ygrid, zgrid = get_grids(pillar_data)
        frames.append([xgrid, ygrid, zgrid])
    return frames
    print(frames)


if __name__ == "__main__":
    main()