# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:06:36 2015

@author: young
"""

def getDetection():
    from scipy.io import loadmat, savemat
    import os
    import sys
    
    os.chdir('/usr/local/MATLAB/R2014a/bin')
    os.system('sh matlab -nosplash -nodesktop -r rcnn_demo')
    return
    
if __name__ == '__main__':
    getDetection()
    