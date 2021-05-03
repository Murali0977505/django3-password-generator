from django.shortcuts import render
import random
# Create your views here.
def hello(request):
    if(request.method!='POST'):
        return render(request, 'generator/home.html')
    else:        
        password1=''
        length=int(request.POST.get('length'))
        characters=list('abcdefghijklmnopqrstuvwxyz')
        if request.POST.get('isCapitals'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.POST.get('isNumbers'):
            characters.extend(list('0123456789'))
        if request.POST.get('isSpecialchars'):
            characters.extend(list('~!@#$%^&*()_+=-'))    
        for i in range(length):
            password1+=random.choice(characters)
        return render(request, 'generator/genpwd.html', {'password':password1})

