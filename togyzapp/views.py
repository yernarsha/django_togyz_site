from django.shortcuts import render

from .models import Blog

# Create your views here.

def catch_all(request):
#    current_url = request.build_absolute_uri()
    current_path = request.path

    if current_path == "/":
        current_path = "index.php"
        
    if len(current_path) > 0 and current_path[0] == '/':
        current_path = current_path[1:]

    article = Blog.objects.get(url=current_path)
    html = article.body
#    print(html)
    html = html.replace('href="images/', 'href="static/togyzapp/images/')
    html = html.replace('src="images/', 'src="static/togyzapp/images/')

    return render(request, "togyzapp/index.html", {'html': html})