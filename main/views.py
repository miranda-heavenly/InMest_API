from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h>")

data = {
     'name': 'Miranda', 
     'email': 'miranda@gmail.com', 
     'phone_number': '099887766'
}

def user_profile(request):
    return JsonResponse(data)

def filter_queries(request, id):
    return JsonResponse({
    "id": id,
    "title": "Mrs.",
    "description": "CEO",
    "status": "Single",
    "submitted_by": "Miranda",
})

class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama declined Val shots"},
            {"id": 2, "title": "Samson declined Val shots"},
        ] 
    def get(self, request):       #the first arguement gives access to the instant of the class and the second argument gives access to the client request.
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse({"status": "ok"})
