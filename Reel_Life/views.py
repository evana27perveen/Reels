from django.shortcuts import render, HttpResponseRedirect, reverse


def cover(request):
    return render(request, 'Reel_Life/cover.html')