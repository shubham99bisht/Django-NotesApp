from django.shortcuts import get_object_or_404, render, redirect
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

def update_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id, user=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.note = request.POST['note']
        note.color = request.POST['color']
        note.save()
        return redirect('home')

def delete_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id, user=request.user)
    note.delete()
    return redirect('home')
