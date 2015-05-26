# -*- coding: utf-8 -*-
"""
Created on Sat May 23 20:04:11 2015

@author: young
"""

import  os
import  wx
from PIL import Image 

import shutil
import requests

#---------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "JPEG (*.jpg)|*.jpg|"     \
           "PNG (*.png)|*.png|" \
           "BMP (*.bmp)|*.bmp|" \
           "All files (*.*)|*.*"
           
class Demo(wx.Frame):
    def __init__(self):
        #self.log = log
        wx.Frame.__init__(self, None, -1, 'Demo for Image Caption', size=(800, 600))
        panel = wx.Panel(self, -1)
        

        image_url_st = wx.StaticText(panel, -1, 'Enter an image URL', pos=(70, 30))
        image_up_st = wx.StaticText(panel, -1, 'Upload an image', pos=(270, 30)) # Text for image url
        image_url_C = wx.TextCtrl(panel, -1, 'image url', pos=(60, 55), size=(135,20))  
        image_url_C.Bind(wx.EVT_TEXT, self.evtText)        
        
        image_up_B = wx.Button(panel, -1, "Choose Image", pos=(270,55)) # buttion for image upload
        self.Bind(wx.EVT_BUTTON, self.onButtonCF, image_up_B)
        
        gen1 = wx.Button(panel, -1, "Download", pos=(80,90)) # buttion for url image text generate
        gen1.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        gen1.Bind(wx.EVT_BUTTON, self.OnButtonGT_url) # bind the button to image choose 
        #self.Bind(wx.EVT_BUTTON, self.OnButtonGT_url, gen1)
        
        gen2 = wx.Button(panel, -1, "Upload", pos=(280,90)) # button for up image text generate
        gen2.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        gen2.Bind(wx.EVT_BUTTON, self.OnButtonGT_cf) # bind the button to image choose 
        #self.Bind(wx.EVT_BUTTON, self.OnButtonGT_cf, gen2)
        
        image_url_exam = wx.StaticText(panel, -1, 'Example Images: click to generate text', pos=(100, 140))
                     
        examImage1 = wx.Image(os.getcwd() + '\example1.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()  
        examIma_but1 = wx.BitmapButton(panel, -1, examImage1, pos=(20, 180), size=(170, 170))
        examIma_but1.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        examIma_but1.Bind(wx.EVT_BUTTON, self.OnButtonC1) # bind the button to image choose 1
        #self.Bind(wx.EVT_BUTTON, self.OnButtonC1, examIma_but1)
        
        examImage2 = wx.Image(os.getcwd() + '\example2.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()  
        examIma_but2 = wx.BitmapButton(panel, -1, examImage2, pos=(220, 180), size=(170, 170))
        examIma_but2.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        examIma_but2.Bind(wx.EVT_BUTTON, self.OnButtonC2) # bind the button to image choose 1
        #self.Bind(wx.EVT_BUTTON, self.OnButtonC2, examIma_but2)
        
        examImage3 = wx.Image(os.getcwd() + '\example3.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()  
        examIma_but3 = wx.BitmapButton(panel, -1, examImage3, pos=(20, 370), size=(170, 170))
        examIma_but3.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        examIma_but3.Bind(wx.EVT_BUTTON, self.OnButtonC3) # bind the button to image choose 1
        #self.Bind(wx.EVT_BUTTON, self.OnButtonC3, examIma_but3)
        
        examImage4 = wx.Image(os.getcwd() + '\example4.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()  
        examIma_but4 = wx.BitmapButton(panel, -1, examImage4, pos=(220, 370), size=(170, 170))
        examIma_but4.Bind(wx.EVT_BUTTON, self.showImage) # bind the button to image show
        examIma_but4.Bind(wx.EVT_BUTTON, self.OnButtonC4) # bind the button to image choose 1
        #self.Bind(wx.EVT_BUTTON, self.OnButtonC4, examIma_but4)
        
        image_show = wx.StaticText(panel, -1, 'Chossed Image: ', pos=(520, 30))
        
        
        generate = wx.Button(panel, -1, "Generate Text", pos=(550,280)) # buttion for url image text generate
        self.Bind(wx.EVT_BUTTON, self.OnButtonGT, generate)
        
        self.image_path = 'init.jpg' 
        #self.image_path = u'C:\\Users\\young\\Desktop\\Demo-gui\\examples.jpg'
        Image = wx.wx.Image(self.image_path, wx.BITMAP_TYPE_ANY)
        Image = Image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
        Image = Image.ConvertToBitmap()
        self.Image = wx.StaticBitmap(panel, bitmap=Image, pos=(500, 65))
        
    def evtText(self, evt):
        # download image form internet with the url
        
        url = evt.GetString()
        response = requests.get(url, stream=True)
        out_file = 'url.jpg'
        with open(out_file, 'wb') as out:
            shutil.copyfileobj(response.raw, out)
        del response
        
        self.image_path = out_file
        
        evt.Skip()    

    def showImage(self, evt):
        
        image = wx.Image(self.image_path, wx.BITMAP_TYPE_ANY)
        image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
        image = image.ConvertToBitmap()
        
        self.Image.SetBitmap(image)
        
        self.Refresh()
        evt.Skip()
        
    def OnButtonC1(self, evt):
        
        self.image_path = 'example1.jpg'    
        evt.Skip()
        
        
    def OnButtonC2(self, evt):
        
        self.image_path = 'example2.jpg'     
        evt.Skip()
        
         
    def OnButtonC3(self, evt):
        
        self.image_path = 'example3.jpg'       
        evt.Skip()
        
    
    def OnButtonC4(self, evt):
        
        self.image_path = 'example4.jpg'       
        evt.Skip()
        
    
    def onButtonCF(self, evt):
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
           # url = dlg.GetPaths()

            self.image_path = dlg.GetPaths()[0]
            
            #print self.image_path
        
        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()
        #evt.Skip()
        
    def OnButtonGT_url(self, evt):
        
        #self.image_path = 'test.jpg'
        #self.image_path = evt.
        """
        dlg = wx.MessageDialog(self, self.image_path, 'A Message Box', 
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        """
        evt.Skip()
        
        
    def OnButtonGT_cf(self, evt):
        #self.image_path = 'C:\Users\young\Desktop\Demo-gui\test.jpg'
        #self.image_path = 'example1.jpg'        
        """
        dlg = wx.MessageDialog(self, self.image_path, 'A Message Box', 
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        """
        evt.Skip()
        
         
    def OnButtonGT(self, evt):
        
        #self.image_path = 'example1.jpg'       
        
        dlg = wx.MessageDialog(self, self.image_path, 'A Message Box', 
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        evt.Skip()
    
#---------------------------------------------------------------------------


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Demo()  
    frame.Show()  
    app.MainLoop()  
