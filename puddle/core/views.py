from django.shortcuts import render, redirect

from item.models import Item, Category
# Create your views here.
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_available=True)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
   
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page after successful signup
            return redirect('/login/')
    else:
        form = SignupForm()
    # If the request method is GET, create an empty form instance
   

    return render(request, 'core/signup.html', {
       'form': form,
   })