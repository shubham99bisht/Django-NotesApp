from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'userNotes/index.html')
    else:
        return redirect('login')