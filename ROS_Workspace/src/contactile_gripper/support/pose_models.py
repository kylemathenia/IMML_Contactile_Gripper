"""Models to make pose predictions"""

import pandas as pd
import numpy as np
import math
from collections import namedtuple

Pose = namedtuple("Pose", 'position', 'orientation')


class LinearAnalytical:
    """Produces linear regression from the contact/no contact points."""
    def __init__(self):
        self.pil_point_map = {0:[1,1], 1:[1,0], 2:[1,-1], 3:[0,1], 4:[0,0], 5:[0,-1], 6:[-1,1], 7:[-1,0], 8:[-1,-1]}


    def predict(self,sensors):
        self.poses = []
        self.contact_list = []
        for sensor in sensors:
            for pillar in sensor.pillars:
                self.contact_list.append(pillar.in_contact)
            self.contact_to_points()
            self.points_to_pose()
        return self.combine_sensor_poses()

    def contact_to_points(self):
        self.x_points, self.y_points = [], []
        # Create a list of Booleans for contact/no contact
        for pil_num in range(len(self.contact_list)):
            if self.contact_list[pil_num]:
                point = self.pil_point_map[pil_num]
                self.x_points.append(point[0])
                self.y_points.append(point[1])

    def points_to_pose(self):
        #TODO if this is the second sensor, need to reflect the pillars...
        if len(self.x_points) <= 2:
            self.poses.append([None,None])
        # Do linear regression on contact points.
        z = np.polyfit(self.x_points, self.y_points, 1)
        p = np.poly1d(z)
        if len(p.c) == 1: # Slope is zero.
            slope = 0
            intercept = p.c[0]
        else:
            slope = p.c[0]
            intercept = p.c[1]
        ang = math.degrees(math.atan(slope))
        pos = intercept
        self.poses.append([pos,ang])

    def combine_sensor_poses(self):
        if self.poses[0].position is None and self.poses[1].position is None:
            return [None,None]
        elif self.poses[0].position is None and self.poses[1].position is not None:
            return [self.poses[1].position,self.poses[1].orientation]
        elif self.poses[0].position is not None and self.poses[1].position is None:
            return [self.poses[0].position, self.poses[0].orientation]
        elif self.poses[0].position is not None and self.poses[1].position is None:
            return [self.poses[0].position, self.poses[0].orientation]
        else:
            return self.average_poses()

    def average_poses(self):
        position = (self.poses[0].position + self.poses[1].position) / 2
        orientation = (self.poses[0].orientation + self.poses[1].orientation) / 2
        return [position,orientation]

def main():
    pass

if __name__ == '__main__':
    main()
