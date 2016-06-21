from django.shortcuts import render
from django.http import HttpResponse
from .models import status


def index(request):
    name_list = status.objects.order_by('id')
    context = {'name_list': name_list}
    return render(request, 'staff/index.html', context)
	
def hello(request):
    return HttpResponse("""<html>
<body>

<h2 style="background-color:red">
Background-color set by using red
</h2>

<h2 style="background-color:orange">
Background-color set by using orange
</h2>

<h2 style="background-color:yellow">
Background-color set by using yellow
</h2>

<h2 style="background-color:blue;color:white">
Background-color set by using blue
</h2>

<h2 style="background-color:cyan">
Background-color set by using cyan
</h2>

</body>
</html>
""")	
def detail(request, a,b):
    
   
    return HttpResponse("%s     %s"%(a,b))
	



