from winreg import REG_WHOLE_HIVE_VOLATILE
from django.shortcuts import render
from . models import quiz,choices_and_answers
from django.db.models import Q

# Create your views here.

def questions(request):
    if request.method == 'POST':
        value1 = request.POST['choice1']
        value2 = request.POST['choice2']
        q_id = request.POST['q_id']
    
        for n in q_id:
            print(n)
        
        print(value1,value2)
        
        try:
            answer1 =   quiz.objects.filter()
        except quiz.DoesNotExist:
            return()
    question = quiz.objects.all()
    choices = choices_and_answers.objects.all()
    
    return render(request, 'questions.html',{"question" : question,"choices":choices})
    