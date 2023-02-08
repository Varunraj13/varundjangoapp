from django.shortcuts import render

from .form import messageForms

# Create your views here.



def home(request,*args,**kwargs):

    print(args,kwargs)

    print(request.user)

    #return HttpResponse("<h1>Hello World Django</h1>")

    return render(request,"index.html")





def contact_form(request,*args,**kwargs):

    print(args,kwargs)

    print(request.user)

    #return HttpResponse("<h1>Hello World Django</h1>")

    return render(request,"contact_form.html")




def contact_formtest(request):
    form = messageForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = messageForms


    context = {
        'form' : form
    }


    return render(request,'contact_form_test.html',context)

def contact_form2(request):
    form = messageForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = messageForms


    context = {
        'form' : form
    }


    return render(request,'contact_form2.html',context)
