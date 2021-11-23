from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BookListForm
from .models import BookList

# Create your views here.
def booklist(request):
    obj = BookList.objects.all()
    context = {
        'object' : obj
    }

    return render(request,'booklist/basic.html',context)

def booklist_post(request):
    if request.method == 'POST':
        form = BookListForm(request.POST ,request.FILES)
        print(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index') 
        else:
            form = BookListForm()
        return render(request, 'booklist/bookpost.html', {'form': form})    

def searchbynameview(request):
    if request.method == "GET":
        name = request.GET.get


    return render(request,'booklist/bookpost.html',{'form':form})        
        
         
    