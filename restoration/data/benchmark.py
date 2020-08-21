import os
from data import common
from data import srdata
import glob
import numpy as np
import scipy.misc as misc

import torch
import torch.utils.data as data

class Benchmark(srdata.SRData):
    def __init__(self, args, train=True):
        super(Benchmark, self).__init__(args, train, benchmark=True)

    # def _scan(self):
    #     list_hr = []
    #     list_lr = [[] for _ in self.scale]
    #     for entry in os.scandir(self.dir_hr):
    #         filename = os.path.splitext(entry.name)[0]
    #         list_hr.append(os.path.join(self.dir_hr, filename + self.ext))
    #         for si, s in enumerate(self.scale):
    #             list_lr[si].append(os.path.join(self.dir_lr, filename + self.ext))
    #             # list_lr[si].append(os.path.join(
    #             #     self.dir_lr,
    #             #     'X{}/{}x{}{}'.format(s, filename, s, self.ext)
    #             # ))
    #
    #     list_hr.sort()
    #     for l in list_lr:
    #         l.sort()
    #
    #     return list_hr, list_lr

    # def _scan(self):
    #     list_hr = []
    #     list_lr = []
    #     for s in self.scale:
    #         list_hr.append(sorted(glob.glob(self.dir_hr.format(s, self.color))))
    #         list_lr.append(sorted(glob.glob(self.dir_lr.format(s, self.color))))
    #
    #     return list_hr, list_lr
    #
    # def _set_filesystem(self, dir_data):
    #     self.apath = os.path.join(dir_data, 'super_resolution/Test', self.args.data_test)
    #     self.dir_hr = self.apath + '_X{}_high{}/*.png'
    #     self.dir_lr = self.apath + '_X{}_low{}/*.png'
    #     self.ext = '.png'

    def _scan(self):
        list_hr = []
        list_lr = []
        for s in self.scale:
            list_hr.append(sorted(glob.glob(self.dir_hr + '/*.png')))
            list_lr.append(sorted(glob.glob(self.dir_lr + '/X{}/*.png'.format(s))))

        return list_hr, list_lr

    def _set_filesystem(self, dir_data):
        self.apath = os.path.join(dir_data, 'super_resolution/benchmark', self.args.data_test)
        self.dir_hr = os.path.join(self.apath, 'HR')
        self.dir_lr = os.path.join(self.apath, 'LR_bicubic')
        self.ext = ('', '.png')
