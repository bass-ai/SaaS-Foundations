import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    #queryset = PageVisit.objects.all()
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title" : my_title,
        "page_visit_count" : page_qs.count(),
        "percent":(page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count(), 
    }
    path = request.path
    print("path", path)
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    
    return render(request, html_template, my_context)








def about_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title,
    }
    
    html_template = "about.html"
    return render(request, html_template, my_context)






















def old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title
    }
    
    html_ = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>
</head>
<body>
    <h1>{page_title}</h1>
</body>
</html>
    """.format(**my_context)
    #html_file_path =this_dir / "home.html"
    #html_ = html_file_path.read_text()
    
    return HttpResponse(html_)