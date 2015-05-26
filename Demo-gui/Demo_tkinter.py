# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:31:33 2015
reference: http://tkinter.unpythonic.net/wiki/

@author: young
"""
# modules for tkinter gui
import PIL
from Tkinter import *
import tkFileDialog
import shutil
import sys
sys.path.append('/home/young/anaconda/lib/python2.7/site-packages')
import requests

from getFeature import extractFeature
from rnnPredict import main

class Demo(Frame):
    
    def __init__(self, root):
        Frame.__init__(self, root)
        self.master.resizable(False, False) 
        #self.master.title('Image Caption')
        
        
        # left-up: choose the image
        lbl_label_url = Label(self, text='Enter an image URL')        
        lbl_label_upload = Label(self, text='Upload an image')
        lbl_label_url.grid(row=0, column=1, padx=0, pady=10)
        lbl_label_upload.grid(row=0, column=2, padx=50)
        
        self.lbl_entry_url = Entry(self, text='image url', width=20)
        lbl_cFile_but = Button(self, text='Choose Image', command=self.onButtonCF)
        #lbl_cFile_but.bind("<Button-1>", onButtonCF)
        self.lbl_entry_url.grid(row=1, column=1)
        lbl_cFile_but.grid(row=1, column=2)
        
        lbl_down_but = Button(self, text='Download Image', command=self.onButtonDL)
        #lbl_down_but.bind("<Button-1>", self.onButtonDL)
        lbl_up_but = Button(self, text='Upload Image', command=self.onButtonUL)
        #lbl_up_but.bind("<Button-1>", onButtonUL)
        lbl_down_but.grid(row=2, column=1, padx=0, pady=10)
        lbl_up_but.grid(row=2, column=2, padx=0, pady=10)
        
        # left-down: choose the example image
        lbl_label_exam = Label(self, text='Example Images: click to generate text')
        lbl_label_exam.grid(columnspan=2, padx=5)
        
        #length_exam = 200
        
        #exam_ori1 = PIL.Image.open('example1.jpg')
        #exam_ori1 = exam_ori1.resize((length_exam, length_exam))
        #exam_ori1.save('example1.gif', 'GIF') # convert the jpg file to gif file
        photo1 = PhotoImage(file='example1.gif')
        exam_but1 = Button(self, image=photo1, command=self.onButtonEx1)
        exam_but1.image = photo1
        #exam_but1.bind("<Button-1>", onButtonEx1)
        exam_but1.grid(row=4, column=1, pady=5)
        
        #exam_ori2 = PIL.Image.open('example2.jpg')
        #exam_ori2 = exam_ori2.resize((length_exam, length_exam))
        #exam_ori2.save('example2.gif', 'GIF') # convert the jpg file to gif file
        photo2 = PhotoImage(file='example2.gif')
        exam_but2 = Button(self, image=photo2, command=self.onButtonEx2)
        exam_but2.image = photo2
        #exam_but2.bind("<Button-1>", onButtonEx2)
        exam_but2.grid(row=4, column=2)
        
        #exam_ori3 = PIL.Image.open('example3.jpg')
        #exam_ori3 = exam_ori3.resize((length_exam, length_exam))
        #exam_ori3.save('example3.gif', 'GIF') # convert the jpg file to gif file
        photo3 = PhotoImage(file='example3.gif')
        exam_but3 = Button(self, image=photo3, command=self.onButtonEx3)
        exam_but3.image = photo3
        #exam_but3.bind("<Button-1>", onButtonEx3)
        exam_but3.grid(row=5, column=1, pady=5)

        #exam_ori4 = PIL.Image.open('example4.jpg')
        #exam_ori4 = exam_ori4.resize((length_exam, length_exam))
        #exam_ori4.save('example4.gif', 'GIF') # convert the jpg file to gif file
        photo4 = PhotoImage(file='example4.gif')
        exam_but4 = Button(self, image=photo4, command=self.onButtonEx4)
        exam_but4.image = photo4
        #exam_but4.bind("<Button-1>", onButtonEx4)
        exam_but4.grid(row=5, column=2)        
        
        # right-up: show the choosed image
        lbl_label_choo = Label(self, text='Choosed Images: ')
        lbl_label_choo.grid(row=0, column=3, columnspan=2, padx=180, sticky='e')
        
        #self.staImage = 'init.jpg'
        #showimage = PIL.Image.open('init.jpg')
        #showimage = showimage.resize((250, 250))
        #showimage.save('init.gif', 'GIF') # convert the jpg file to gif file
        self.iamge_path = 'init.gif'
        
        image_show = PhotoImage(file=self.iamge_path)
        self.lbl_label_show = Label(self, image=image_show)
        self.lbl_label_show.image = image_show
        self.lbl_label_show.grid(row=1, column=3, rowspan=4, columnspan=3, padx=120, pady=0, sticky='n')
        
        # right-down: show the results
        #lbl_label_tag = Label(master, text='Detected Tags: ')
        #lbl_label_tag.grid(row=5, column=3, padx=0, sticky='n')
        result_frame = Frame(self)
        result_frame.grid(row=5, column=3, columnspan=3, padx=80, sticky='nw')
        
        lbl_gen_but = Button(result_frame, text="Generate Text", command=self.onButtonGEN, bg='green', width=14, font=('Helvetica', 12))
        #lbl_gen_but.bind("<Button-1>", onButtonGEN)
        lbl_gen_but.grid(row=0, column=0, columnspan=2, sticky='e')        
        
        lbl_label_tag = Label(result_frame, text="Tags:", font=("Helvetica", 14))
        lbl_label_tag.grid(row=1, column=0, sticky='w')
        self.lbl_label_detect = Label(result_frame, text="cats, dogs, person, child", font=(12))
        self.lbl_label_detect.grid(row=1, column=1, padx=10)
        
        lbl_label_sen = Label(result_frame, text="Top 5 Generated sentence>", font=("Helvetica", 14))
        lbl_label_sen.grid(row=2, column=0, columnspan=3, pady=3, sticky='w')
        
        self.lbl_label_gensen1 = Label(result_frame, text="a dog was running")
        self.lbl_label_gensen1.grid(row=3, column=0, columnspan=2, padx=5, sticky='w')
        self.lbl_label_gensen2 = Label(result_frame, text="a cat was running")
        self.lbl_label_gensen2.grid(row=4, column=0, columnspan=2, padx=5,sticky='w')
        self.lbl_label_gensen3 = Label(result_frame, text="a person was running")
        self.lbl_label_gensen3.grid(row=5, column=0, columnspan=2, padx=5,sticky='w')
        self.lbl_label_gensen4 = Label(result_frame, text="two dogs was running")
        self.lbl_label_gensen4.grid(row=6, column=0, columnspan=2, padx=5,sticky='w')
        self.lbl_label_gensen5 = Label(result_frame, text="two cats was running")
        self.lbl_label_gensen5.grid(row=7, column=0, columnspan=2, padx=5,sticky='w')
        
        # deal with the data

    def onImageshow(self, show_path):
        #print 'image show'
        #print self.iamge_path
        temp_path = 'temp.gif'
        self.image = PIL.Image.open(show_path)
        self.image = self.image.resize((250, 250))
        self.image.save(temp_path, 'GIF')
        
        refresh_image = PhotoImage(file=temp_path)
        self.lbl_label_show['image'] = refresh_image
        self.lbl_label_show.image = refresh_image
        #print self.iamge_path
        #os.remove(temp_path)

    def onButtonCF(self):
        #print 'cf'
        ftypes = [('Image Files', '*.gif *.jpg *.png')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        #print filename     
        self.iamge_path = filename
        self.onImageshow(filename)
        
    def onButtonDL(self):
        #print 'dl'
        url = self.lbl_entry_url.get()
        
        
        response = requests.get(url, stream=True)
        out_file = 'url.jpg'
        with open(out_file, 'wb') as out:
            shutil.copyfileobj(response.raw, out)
        del response
        
        showimage = PIL.Image.open('url.jpg')
        showimage = showimage.resize((250, 250))
        showimage.save('url.gif', 'GIF') # convert the jpg file to gif file
        self.iamge_path = out_file
        self.onImageshow('url.gif')
            
    def onButtonUL(self):
        #print 'ul'
        self.onImageshow(self.iamge_path)
            
    def onButtonEx1(self):
        #print 'ex1'
        self.iamge_path = 'example1.jpg'
        self.onImageshow('example1.gif')
    
    def onButtonEx2(self):
        #print 'ex2'
        self.iamge_path = 'example2.jpg'
        self.onImageshow('example2.gif')
        
    def onButtonEx3(self):
        #print 'ex3'
        self.iamge_path = 'example3.jpg'
        self.onImageshow('example3.gif')
    
    def onButtonEx4(self):
        #print 'ex4'
        self.iamge_path = 'example4.jpg'
        self.onImageshow('example4.gif')
    
    def onButtonGEN(self):
        #print 'gen'
        feature = extractFeature([self.iamge_path]) # use extractFeature function to get feature
        
        dict_sentence = main(feature) # use main function to get sentence
        
        self.lbl_label_detect['text'] = 'young' # reset the detected tags
        
        # set the generated sentence
        self.lbl_label_gensen1['text'] = dict_sentence.get('4').get('imgblobs')[0].get('candidate').get('text')
        self.lbl_label_gensen2['text'] = dict_sentence.get('1').get('imgblobs')[0].get('candidate').get('text')
        self.lbl_label_gensen3['text'] = dict_sentence.get('2').get('imgblobs')[0].get('candidate').get('text')
        self.lbl_label_gensen4['text'] = dict_sentence.get('3').get('imgblobs')[0].get('candidate').get('text')
        self.lbl_label_gensen5['text'] = dict_sentence.get('4').get('imgblobs')[0].get('candidate').get('text')        
        #print self.lbl_label_gensen1['text']
        print 'Done'
"""
def getfeature(filename):
    feature = getFeature.extractFeature(filename)
    return feature
    
def getText(feature):
    dict_sen = main(feature)
    
    return dict_sen
"""
 
if __name__ == '__main__':
    root = Tk()
    #root = Toplevel() # avoid TclError: image "pyimage3" doesn't exist
    root.title("Image Caption")
    root.minsize(800, 600)
    Demo(root).pack()
    root.mainloop()