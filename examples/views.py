from django.shortcuts import render
from .forms import ExampleForm02, ExampleForm03

# Create your views here.
def form_example01(request):
    # QueryDict can have multiple values for a key, so we use the `getlist` function
    # to get them all
    for name in request.POST:
        print("{} {}".format(name, request.POST.getlist(name)))
    return render(request, 'form-example01.html', {'method': request.method})

def form_example02(request):
    form = ExampleForm02()
    
    for name in request.POST:
        print("{} {}".format(name, request.POST.getlist(name)))
    
    return render(request, 'form-example02.html', {'method': request.method, 'form': form})

def form_example03(request):
    if request.method == "POST":
        form = ExampleForm03(request.POST)
    else:
        form = ExampleForm03()
        
    if request.method == 'POST':
        form = ExampleForm03(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    # else:
    #     form = ExampleForm03()  
        
    return render(request, "form-example03.html", {'method': request.method, 'form:':form})