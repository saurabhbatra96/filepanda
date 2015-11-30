from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf                         #Cross-site Request Forgery
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.contrib import auth
from filepanda.forms import MyRegistrationForm

def login(request):
    c = {}                                                              #Empty Dictionary
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    #If you don't find a valid value, return empty string to vars. Stops script from crashing
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    #checks for user 
    user = auth.authenticate(username=username, password=password) 

    if user is not None:
        auth.login(request,user)                                             #Sets login=true 
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/login/')

#def loggedin(request):
 #   t = get_template('loggedin.html')
  #  html = t.render(Context({'full_name': request.user.username }))
   # return HttpResponse(html)

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)                                                #Sets login=false
    #return render_to_response('logout.html')
    return HttpResponseRedirect('/accounts/login/')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')

    args = {}
    args.update(csrf(request))

    #args['form'] = MyRegistrationForm()

    return render_to_response('register.html', args)
    #return render_to_response('register.html')

def register_success(request):
    #return render_to_response('register_success.html')
    return HttpResponseRedirect('/accounts/login/')
