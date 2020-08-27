from django.shortcuts import render
from django.http import StreamingHttpResponse
from app.Integrations import get_frame

def index(request):
    return render(request, 'app/index.html')

def StreamView(Integrations):
    while True:
        frame = Integrations.get_frame()
        yield(b'--frame\r\n'
            b'content-type: image\r\n\r\n' + frame + b'\r\n\r\n')

def VideoFeed(request):
    return StreaminHttpResponse(StreamView(), content_type = 'multipart/x-mixed-replace; boundary=frame')

