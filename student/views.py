from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'sonam'
    request.session['lname'] = 'Jha'
    return render(request, 'student/setsession.html')



def getsession(request):
    name = request.session.get('name')
    return render(request, 'student/getsession.html', {'name':name})




def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')