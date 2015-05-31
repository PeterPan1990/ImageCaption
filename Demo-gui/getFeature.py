# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:03:33 2015
script for feature extraction with VGG-16 network
@author: young
"""


def initmodel():
    """
    description: to do ...
    """    
    
    # import modules
    import sys
    
    sys.path.append('/home/young/caffe-master/python/') # add caffe path
    sys.path.append('/usr/lib/python2.7/dist-packages/')
    sys.path.append('/media/young/225AD7985AD766D7/json/ImageCaption') # add neuraltalk root path
    import caffe
    
    # initiate the caffe model
    rootdir = '/home/young/Desktop/ImageCaption/'
    rootmodel = rootdir + 'python/'
    net = caffe.Net(rootmodel + 'deploy_features.prototxt', \
                    rootmodel + 'VGG_ILSVRC_16_layers.caffemodel')
                    
    return net

def predict(in_data, net):
    """
    Get the features for a image using network

    Inputs:
    in_data: data batch
    """

    out = net.forward(**{net.inputs[0]: in_data})
    features = out[net.outputs[0]].squeeze(axis=(2,3))
    return features

def extractFeature(filenames):
    """
    Get the features of the images from filename using a network

    Inputs:
    filenames: names of image files

    Returns:
    an array of feature vectors for the images in that file
    """
    
    import numpy as np
    from scipy.misc import imread, imresize
    
    net = initmodel()
    N, C, H, W = net.blobs[net.inputs[0]].data.shape
    F = net.blobs[net.outputs[0]].data.shape[1]
    Nf = len(filenames)
    Hi, Wi, _ = imread(filenames[0]).shape
    allftrs = np.zeros((Nf, F))
    for i in range(0, Nf, N):
        in_data = np.zeros((N, C, H, W), dtype=np.float32)

        batch_range = range(i, min(i+N, Nf))
        batch_filenames = [filenames[j] for j in batch_range]
        Nb = len(batch_range)

        batch_images = np.zeros((Nb, 3, H, W))
        for j,fname in enumerate(batch_filenames):
            im = imread(fname)
            if len(im.shape) == 2:
                im = np.tile(im[:,:,np.newaxis], (1,1,3))
            # RGB -> BGR
            im = im[:,:,(2,1,0)]
            # mean subtraction
            im = im - np.array([103.939, 116.779, 123.68])
            # resize
            im = imresize(im, (H, W))
            # get channel in correct dimension
            im = np.transpose(im, (2, 0, 1))
            batch_images[j,:,:,:] = im

        # insert into correct place
        in_data[0:len(batch_range), :, :, :] = batch_images

        # predict features
        ftrs = predict(in_data, net)

        for j in range(len(batch_range)):
            allftrs[i+j,:] = ftrs[j,:]

        #print 'Done %d/%d files' % (i+len(batch_range), len(filenames))

    return allftrs.transpose()

if __name__ == '__main__':
    
    filename = ['/media/young/225AD7985AD766D7/json/neuraltalk-master/example_images/7EGRMwN.jpg']
    feature = extractFeature(filename)
    
    
    
    
    