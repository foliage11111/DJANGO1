from django.shortcuts import render
import django.http.response
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(req):
   # return HttpResponse('test1.html',{'user':'jjjj','title':'this is first prama'})
     return render_to_response('test1.html',{'user':'jjjj','title':'this is first prama'})