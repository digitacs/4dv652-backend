import tensorflow.compat.v1 as tf
import posenet

def handle_video_upload(f):  
    with open('media/video/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def tf_version(): 
    return tf.__version__