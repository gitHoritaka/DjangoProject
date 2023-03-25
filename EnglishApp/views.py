from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView 
from . import API 
from .models import Word

# Create your views here.

class Index(ListView):
    model = Word
    data = API.Create_Descriptions()
    descriptions = []
    urls = []
    for description,url in data:
        descriptions.append(description)
        urls.append(url)
    extra_context = {'Descriptions':descriptions ,'Urls':urls}
    def post(self,request):
        checked_data = request.POST.getlist('checkbox')
        checked_word = []
        for tmp in checked_data:
            index,word_index = map(int,tmp.split('/'))
            word = Index.data[index][0][word_index]
            used_befores = Word.objects.filter(saved_word=word)
            checked_word.append(word)
            if used_befores:
                for used in used_befores:
                    used.word_count =  1 + used.word_count
                    used.save()
            else:
                obj = Word(saved_word=word)
                obj.save()
        context = {'checked_words':checked_word}
        return render(request,'EnglishApp/selected_word.html',context)

class WordView(ListView):
    model = Word


        




    

