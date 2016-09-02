from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect

from .forms import UserResponseForm
from .models import Question,Answer

# Create your views here.
def single(request,id):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print request.POST
            question_id = form.cleaned_data.get('question_id') #form.cleaned_data['question_id']
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id = question_id)
            answer_instance = Answer.objects.get(id = answer_id)
            print answer_instance,question_instance
            next_q = Question.objects.all().order_by("?").first()
            return redirect("question_single",id=next_q.id)
        instance = get_object_or_404(Question,id=id)
        context = {
			#"queryset": queryset,
            "instance":instance,
            "form":form,
		}
        return render(request, "questions/single.html", context)
    else:
        raise Http404

def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            question_id = form.cleaned_data.get('question_id') #form.cleaned_data['question_id']
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id = question_id)
            answer_instance = Answer.objects.get(id = answer_id)
            print answer_instance,question_instance

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
			#"queryset": queryset,
            "instance":instance,
            "from":form,
		}
        return render(request, "questions/home.html", context)
    else:
        raise Http404
