from django.shortcuts import redirect
from monApp.models import Contenir
from monApp.forms import ContenirForm, ContenirModifForm
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
  

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    @method_decorator(login_required)
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)