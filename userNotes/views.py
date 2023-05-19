from django.shortcuts import render, redirect
from .models import Notes

# Create your views here.
def index(request):
    user = request.user

    if request.method == 'POST':
        title = request.POST['title']
        note = request.POST['note']
        color = request.POST['color']
        
        newnote = Notes(user=request.user, title=title, note=note, color=color)
        newnote.save()

    if user.is_authenticated:
        all_notes = Notes.objects.filter(user=request.user)
        return render(request, 'userNotes/index.html', {'all_notes': all_notes})
    else:
        return redirect('login')