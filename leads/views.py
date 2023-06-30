from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead
from .models import Agent
from .forms import LeadForm, LeadModelForm


# Create your views here.
def lead_list(request):

    leads = Lead.objects.all()
    context = {  "leads" : leads  }



    # return HttpResponse("Hello World")
    return render(request, "leads/lead_list.html",context)


def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)
    context = {  "lead" : lead  }
    return render(request, "leads/lead_detail.html",context)



def lead_create(request):
    form = LeadModelForm()

    if request.method == "POST":        #Proccess the form
        print('Receiving a post request')
        form = LeadModelForm(request.POST)

        if form.is_valid():
            print("The form is valid")

            form.save()

            print("Lead has been created")
            return redirect("/leads/")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)



def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)

    form = LeadForm()

    if request.method == "POST":        #Proccess the form
        print('Receiving a post request')
        form = LeadForm(request.POST)

        if form.is_valid():
            print("Valid Update form")

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
         

            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.save()

            print("Lead has been created")
            return redirect(f"/leads/{pk}")

    
    context = {
        "form": form,
        "lead":lead
    }
    return render(request, "leads/lead_update.html", context)