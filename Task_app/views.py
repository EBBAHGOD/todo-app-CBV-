from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from. import models
from django.urls import reverse_lazy


# Create your views here.
class task_list(ListView): 
    model=models.Task_list
    template_name='home.html'
    context_object_name="tasks"
   
    def get_queryset(self): #this method is to help us filter the queryset that is being passsed to the templates
        if self.request.user.is_authenticated:
            User=self.request.user
            searched=self.request.GET.get('search_string') or ''
            if searched:
                    return models.Task_list.objects.filter(user=User,task_name__icontains=searched)

            else:
                 return models.Task_list.objects.filter(user=User)
  

        
   
  

        
        
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        searched=self.request.GET.get('search_string')
        if self.request.user.is_authenticated:
            context['count']=models.Task_list.objects.filter(user=self.request.user,task_status=False).count
            context['searched']=searched
            return context
    


class detail_view(DetailView):
    model=models.Task_list
    template_name='detail.html'
    context_object_name='tasks'

class update_view(UpdateView):
    model=models.Task_list
    template_name='update_task.html'
    fields=['task_name','task_description','task_status']
    success_url='/'


class create_view(CreateView):
    model=models.Task_list
    template_name='new_task.html'
    fields=['task_name','task_description']
    success_url="/"
    def form_valid(self, form): # this method is called when the form is submitted and is valid.It helps us to add some extra logic before the form is saved to the database
        form.instance.user=self.request.user
        return super(create_view,self).form_valid(form)
        

class delete_view(DeleteView):
    template_name='delete.html'
    model=models.Task_list
    success_url='/'
    context_object_name='task'
   

    
        