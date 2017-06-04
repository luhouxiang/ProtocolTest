from django.http import HttpResponse
from django.shortcuts import render
from web_json import WebJson

def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def add2(request):
    print(request.POST)
    return HttpResponse(request.POST)

def getdata(request):
    web = WebJson()
    url = "http://192.168.230.10:21800/api/gm-service/reqGameConf/select/100000?uid=2"
    data = web.get(url)
    return HttpResponse(data)
def testpost1(request):
    print(request.POST)
    return HttpResponse(request.POST)    
    
def testpost2(request):
    if request.method == 'POST':
        drugs = request.POST.get('drugs')
        print("打印drugs:[", drugs, "]")
        return HttpResponse(drugs)   
    else:
        return render(request, 'index.html')
    
def send(request):
    if request.method == 'POST':
        web = WebJson()
        url = request.POST.get('inputurl')
        print("打印send: ", url)
        method = request.POST.get('method')
        if(method == 'GET'):
            data = web.get(url)
        else:
            postdata = request.POST.get('postdata')
            data = web.post(params, postdata)
        return HttpResponse(data)
        
        