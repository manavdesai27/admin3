from django.shortcuts import render

tasks = ["ID-CARD", "FOOD", "SLEEP"]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

