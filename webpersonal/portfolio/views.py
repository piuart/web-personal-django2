from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request,"portfolio/portfolio.html", {'projects':projects})


def project_detail(request,id):
    project_detail = Project.objects.get(
        id = id
    )
    print(project_detail.id)
    return render(request, 'portfolio/page.html', {'project_detail':project_detail} )