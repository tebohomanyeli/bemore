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
            # print(form.cleaned_data)

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']

            
            # Lead.objects.create(
            #     first_name = first_name,
            #     last_name = last_name,
            #     age = age,
            #     agent = agent
            # )

            form.save()
            print("Lead has been created")
            return redirect("/leads/")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)