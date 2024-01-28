from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util
import random

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entry(request, entry_name):
    selected_entry = util.get_entry(entry_name)
    if selected_entry != None:
        md = Markdown()
        entry_text = md.convert(selected_entry)
        return render(request, "encyclopedia/entry.html",{
            "title": entry_name.capitalize(),
            "entry": entry_text
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": "No such entry found",
            "entry": "Page not found"
        })
        
def search(request):
    entrys = util.list_entries()
    query = request.GET["q"]
    matches = []
    if query in (entry.lower() for entry in entrys):
        return redirect("/wiki/" + query)
    for entry in entrys:
        if query in entry.lower():
            matches.append(entry)
    return render(request, "encyclopedia/search.html",{
        "query": query,
        "entrys": matches
    })

def random_entry(request):
    entrys = util.list_entries()
    selected_entry = random.choice(entrys)
    return redirect("/wiki/" + selected_entry)

def create_entry(request):
    if request.method == "GET" :
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST["title"]
        content = request.POST["entry"]
        entrys = util.list_entries()
        if title.lower() in (entry.lower() for entry in entrys):
            print("Da ba")
            return render(request, "encyclopedia/entry.html",{
                "title":"Entry already exists",
                "entry":"Entry already exists"
            })
        util.save_entry(title, content)
        return redirect("/wiki/" + title)
    
def update(request, entry_name):
    if request.method == "GET":
        entry = util.get_entry(entry_name)
        return render(request, "encyclopedia/create.html",{
            "title": entry_name,
            "entry": entry
        })
    title = request.POST["title"]
    content = request.POST["entry"]
    util.save_entry(title, content)
    return redirect("/wiki/"+title)