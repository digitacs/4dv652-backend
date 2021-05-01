
def handle_video_upload(file):  
    with open('media/video/'+file.name, 'wb+') as destination:  
        for chunk in file.chunks():  
            destination.write(chunk)