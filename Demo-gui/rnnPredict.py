# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:03:33 2015
script for feature extraction with VGG-16 network
@author: young
"""

"""
This script is used to predict sentences for arbitrary images
that are located in a folder we call root_folder. It is assumed that
the root_folder contains:
- the raw images

Then point this script at the folder and at a checkpoint model you'd
like to evaluate.
"""

def main(feature):
    """
    description
    """
    
    import cPickle as pickle
    #from scipy.io import loadmat
    import sys
    sys.path.append('/media/young/225AD7985AD766D7/json/ImageCaption')
    #sys.path.append('I:\json\neuraltalk-master\imagernn')
    from imagernn.solver import Solver
    from imagernn.imagernn_utils import decodeGenerator, eval_split

    #rootdir = 'I:\json\neuraltalk-master'
    #mat = loadmat(r'I:\json\neuraltalk-master\model\vgg_feats.mat')
    #feature = mat.get('feats')
    N = 1
    
    # deal with images and predict sentence
    # load the checkpoint

    checkpoint_path_top5 = [r'/media/young/225AD7985AD766D7/json/ImageCaption/model/model_checkpoint_coco_Caicai-PC_baseline_15.97.p', \
                            r'/media/young/225AD7985AD766D7/json/ImageCaption/model/model_checkpoint_coco_Caicai-PC_baseline_16.71.p', \
                            r'/media/young/225AD7985AD766D7/json/ImageCaption/model/model_checkpoint_coco_Caicai-PC_baseline_18.47.p', \
                            r'/media/young/225AD7985AD766D7/json/ImageCaption/model/model_checkpoint_coco_Caicai-PC_baseline_24.56.p', \
                            r'/media/young/225AD7985AD766D7/json/ImageCaption/model/model_checkpoint_coco_Caicai-PC_baseline_24.64.p']
                            
    blob_top5 = {} # dict to store the top5 generated sentences
    for i in range(5):

        checkpoint_path = checkpoint_path_top5[i]
        #print 'loading checkpoint %s' % (checkpoint_path, )
        checkpoint = pickle.load(open(checkpoint_path, 'rb'))
        #print checkpoint.keys()
        checkpoint_params = checkpoint['params']
        dataset = checkpoint_params['dataset']
        model = checkpoint['model']
        misc = {}
        misc['wordtoix'] = checkpoint['wordtoix']
        ixtoword = checkpoint['ixtoword']
    
        # output blob which we will dump to JSON for visualizing the results
        blob = {} 
        blob['params'] = {}
        blob['checkpoint_params'] = checkpoint_params
        blob['imgblobs'] = []
    
        BatchGenerator = decodeGenerator(checkpoint_params)
        for n in xrange(1):
            print 'image %d/%d:' % (n+1, N)
    
            # ecode the image
            img = {}
            img['feat'] = feature[:, n]
            #img_names = open(test_file, 'r').read().splitlines()
            img['local_file_path'] = 'test.jpg'
    
            # perform the work. heavy lifting happens inside
            kwparams = { 'beam_size' : 2 }
            Ys = BatchGenerator.predict([{'image':img}], model, checkpoint_params, **kwparams)
    
            # build up the output
            img_blob = {}
            img_blob['img_path'] = img['local_file_path']
    
            # encode the top prediction
            top_predictions = Ys[0] # take predictions for the first (and only) image we passed in
            top_prediction = top_predictions[0] # these are sorted with highest on top
            candidate = ' '.join([ixtoword[ix] for ix in top_prediction[1] if ix > 0]) # ix 0 is the END token, skip that
            print 'PRED: (%f) %s' % (top_prediction[0], candidate)
            img_blob['candidate'] = {'text': candidate, 'logprob': top_prediction[0]}    
            blob['imgblobs'].append(img_blob)
    
        blob_top5[str(i)] = blob
        
    return blob_top5
    
if __name__ == '__main__':
    
    result = main(feature)




    
    
