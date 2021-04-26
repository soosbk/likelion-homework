from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def result(request):
    sentence = str(request.POST.get('sentence'))
    words = sentence.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] +=1
        else:
            word_counts[word] = 1
    word_counts = list(word_counts.items())
    
    word_counts.sort(key = lambda t : -t[1])

    return render(request, 'result.html', { 'word_counts': word_counts})