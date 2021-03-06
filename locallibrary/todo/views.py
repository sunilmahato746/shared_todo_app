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
        data = request.POST.get('content')
        important =True if 'Important' in request.POST.get('checkbox2',' ') else False
        urgent = True if 'Urgent' in request.POST.get('checkbox1',' ') else False
        Datelogged = datetime.date.today()
        strdate= request.POST.get('duedate',None)
        if strdate:
            Targetdate=datetime.datetime.strptime(strdate,'%d-%m-%y')
        else:
            Targetdate=Datelogged
        if data not in ['',None]:
            new_item=TodoItem(content=data,Urgent=urgent,Important=important,\
                              Datelogged=Datelogged,Targetdate=Targetdate,Flag=False)
            new_item.save()
        return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def strikethroughTodo(request, todo_id):
    item_to_strike=TodoItem.objects.get(id=todo_id)
    item_to_strike.Flag= not item_to_strike.Flag
    item_to_strike.save()
    return HttpResponseRedirect('/todo/')

