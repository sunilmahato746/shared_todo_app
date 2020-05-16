from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
def todoView(request):
    all_todo_items=TodoItem.objects.all()
    return render(request,'todo.html',{"all_items":all_todo_items})

def addTodo(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        data = request.POST.get('content')
        important =True if 'Important' in request.POST.get('checkbox2',' ') else False
        urgent = True if 'Urgent' in request.POST.get('checkbox1',' ') else False
        Datelogged = datetime.date.today()

        if data not in ['',None]:
            new_item=TodoItem(content=data,Urgent=urgent,Important=important,Datelogged=Datelogged,Flag=False)
            new_item.save()
        return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def strikethroughTodo(request, todo_id):
    item_to_strike=TodoItem.objects.get(id=todo_id)
    item_to_strike.Flag=True
    item_to_strike.save()
    return HttpResponseRedirect('/todo/')

