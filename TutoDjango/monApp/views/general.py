from django.shortcuts import redirect
from monApp.forms import ContactUsForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render


def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monApp.com'],)
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'param':titreh1, 'form':form})

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['param'] = f"Hello {self.kwargs.get('param')}"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['param'] = "About us..."
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class EmailView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(EmailView, self).get_context_data(**kwargs)
        context['param'] = "Email reçu !!!"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)