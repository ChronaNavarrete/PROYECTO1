from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from cabildos.forms import Cabildo_OnlineForm


# Create your views

#def Cabildo_OnlineView(request):
 #   if request.method == "POST" : 
  #      form = Cabildo_OnlineForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #   return redirect("template:calendario")
    #else:
     #   form = Cabildo_OnlineForm()
    #return render(request, "template/calendario.html", {"form" : form})