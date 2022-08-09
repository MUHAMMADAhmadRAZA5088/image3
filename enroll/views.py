
from django.shortcuts import render
from .forms import photoload
from .models import image

# Create your views her
def uploader(request):
    if request.method=='POST':
        form=photoload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=photoload()
    img=image.objects.all()
    return render(request,'base.html',{'form':form,'image':img})