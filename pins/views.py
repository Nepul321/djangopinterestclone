from django.shortcuts import render

# Create your views here.
def AllPinsView(request, *args, **kwargs):
    template = "pins.html"
    context = {

    }
    return render(request, template, context)