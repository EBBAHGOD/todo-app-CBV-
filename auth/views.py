from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout,login
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
 


class login_view(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    fields='__all__'
   
    def get_success_url(self):
        return reverse_lazy('home')
        return redirect()
    


class  Form_view(FormView):
    template_name='signup.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        new_user=form.save() #after saving form.save returns an instance of the model 
        if new_user is not None:
            login(self.request,new_user)
        return super().form_valid(form)
    
    def get(self,*args,**kwargs):  # when the get method is called because a get http request is sent 
        if self.request.user.is_authenticated: # we will check if the user is authenticated
            return redirect('home') #if he is we redirect back to the home page 
        return super().get(*args,**kwargs) # if he isnt we call the get of the parent class to continue handling the get request




def logout_view(request):
    logout(request)
    return redirect('home')
