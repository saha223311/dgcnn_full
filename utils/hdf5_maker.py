import scipy.io
import h5py
import argparse
from PIL import Image
from pathlib import Path
import numpy as np
import os

class H5pyWriter(h5py.File):
    def __init__(self, file_name):
        super().__init__(file_name, 'w')

    def __del__(self):
        super().close()

    def add_group_hdf5(self, group_name, points, labels):
        g = self.create_group(group_name)
        g.create_dataset(name="point_coords", data=points, dtype=np.dtype(float))
        g.create_dataset(name="point_labels", data=labels, dtype=np.dtype(int))


class ShapeNetData:
    def __init__(self, config):
        self.data_dir = Path(config.data_dir)
        self.points_dir = Path(config.points_dir)
        self.labels_dir = Path(config.labels_dir)
        self.h5py_writer = H5pyWriter(config.hdf5_file_name)

    def get_point_coords(self, file):
        with open(file) as f:
            rows = [rows.strip() for rows in f]
    
        raw_points = rows
        coords_set = [point.split() for point in raw_points]

        points = [list([float(point) for point in coords]) for coords in coords_set]

        return points

    def get_point_labels(self, file):
        with open(file) as f:
            rows = [rows.strip() for rows in f]

        raw_labels = rows
        labels = [int(label) for label in raw_labels]

        return labels


    def _fill_data(self):
        for group in os.listdir(self.points_dir):
            self.h5py_writer.add_group_hdf5(group, )

