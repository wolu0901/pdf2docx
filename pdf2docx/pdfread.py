 # -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 02:32:04 2017

@author: wolu0
"""

from wand.image import Image

def convert_pdf_to_jpg(filename,shortfile):
    with Image(filename=filename,resolution=300) as img :
        #print('pages = ', len(img.sequence))
        leng=len(img.sequence)
        with img.convert('jpeg') as converted:
            converted.save(filename='{}/{}.jpeg'.format(shortfile,shortfile))   
        return leng

#convert_pdf_to_jpg('Amazon.pdf')