from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def result(request):
    #print(request.GET.get('sentence'))
    sentence = str(request.POST.get('sentence'))
    words = sentence.split()
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] +=1
        else:
            word_counts[word] = 1
    #print(word_counts)
    word_counts_list=list(word_counts.items())
    word_counts_list.sort(key = lambda t : -t[1])
    response={
        'word_counts': word_counts_list
    }
    

    return render(request, 'result.html', response)