from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    word_list=text.split()
    count_list =len(word_list)

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total':count_list,'dictionary' : word_dictionary.items()})