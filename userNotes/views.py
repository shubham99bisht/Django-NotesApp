from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    user = request.user

    if request.method == 'POST':
        title = request.POST['title']
        note = request.POST['note']
        color = request.POST['color']
        pass

    if user.is_authenticated:
        return render(request, 'userNotes/index.html')
    else:
        return redirect('login')