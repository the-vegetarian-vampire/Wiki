from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import markdown2

from . import util # imports from current directory


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_markdown(entry): # converts markdown to HTML
    content = util.get_entry(entry)
    markdown = markdown2.Markdown()
    if content == None:
        return None
    else:
        return markdown.convert(content)

def entry(request, title): # directs to error page
    html = convert_markdown(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": "404 Error - Page Not Found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
    })

def search(request):
    if request.method == "POST":
        entry = request.POST['q']
        html = convert_markdown(entry)
        if html != None:
            return render(request, "encyclopedia/entry.html", {
            "title": entry,
            "content": html
            })
        else:
            list = []
            entries = util.list_entries()
            for item in entries:
                if entry.lower() in item.lower():
                    list.append(item)
            return render(request, "encyclopedia/search.html", {
                "list": list
                })


def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        exists = util.get_entry(title)
        if exists != None:
            return render(request, "encyclopedia/error2.html", {
                "message": "Page already exists"
            })
        else:
            util.save_entry(title, content)
            html = convert_markdown(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html
            })
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": content
        })