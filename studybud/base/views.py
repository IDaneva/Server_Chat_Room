from django.shortcuts import render

rooms = [
    {"id": 1, "name": "lets learn python"},
    {"id": 2, "name": "Designers unite"},
    {"id": 3, "name": "Frontend developers"},
]

def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    return render(request, "base/room.html")
