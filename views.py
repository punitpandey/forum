from django.shortcuts import render,redirect
from dashboard.queryForm import queryForm
from dashboard.models import query,response
from django.shortcuts import render,redirect
from dashboard.queryForm import queryForm,responseForm
from dashboard.models import query,response
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/signup.html', {'form': form})

@login_required
def index(request):
    context=query.objects.all()
    return render(request,'dashboard/index.html',{'queries':context})

@login_required
def add_query(request):
    return render(request,'dashboard/query.html')

@login_required
def queryDetail(request,id):
    responses=response.objects.filter(query_id=id)
    responselist=[]
    for res in responses:
        responselist.append(res)
    context={
        'query':query.objects.get(id=id),
        'response':responselist
    }
    return render(request,'dashboard/detail.html',{'detail':context})
@login_required
def submitQuery(request):
    if request.method=='POST':
        success=False
        qform=queryForm(request.POST,request.FILES)
        if qform.is_valid():
            formdata=query()
            formdata.name=qform.cleaned_data["name"]
            formdata.subject=qform.cleaned_data["subject"]
            formdata.query=qform.cleaned_data["query"]
            formdata.image=qform.cleaned_data["image"]
            formdata.status='Active'
            formdata.lastactivedate=datetime.now().strftime('%Y-%m-%d')
            formdata.save()
            success=True
            message="Query posted successfully."
        else:
            qform=queryForm()
    return render(request,'dashboard/query.html',locals())

@login_required
def submitResponse(request,id):
    if request.method=='POST':
        success=False
        rform=responseForm(request.POST)
        if rform.is_valid():
            qb=query.objects.get(id=id)
            response.objects.create(response=rform.cleaned_data["response"],responseUser=request.user.username,responsedate=datetime.now().strftime('%Y-%m-%d'),query=qb)
            success=True
            message="Response Added Successfully."
        else:
            qform=responseForm()
    return render(request,'dashboard/query.html',locals())