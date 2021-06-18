from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView 

#from django.contrib.auth.forms import UserCreationForm ######
from django.contrib.auth import login

from django.urls import reverse_lazy

from .models import User_Db
from .forms import CustomAuthForm, CustomUserCreationForm

class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterView(FormView):

    template_name = 'register.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomUserCreationForm
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).get(*args, **kwargs)

class Upload(LoginRequiredMixin,CreateView):

    template_name = 'upload.html'
    model = User_Db
    fields = ['user','image']
    success_url = reverse_lazy('upload')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Upload, self).form_valid(form)

class DeleteView(LoginRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = User_Db
    context_object_name = 'user'
    success_url = reverse_lazy('home')

class HomeView(LoginRequiredMixin,ListView):

    model = User_Db
    #context_object_name = 'data_obj' # name to be used in templates (html)
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        data = User_Db.objects.all() 
        context['data'] = data
        
        return context