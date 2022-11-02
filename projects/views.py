from django.shortcuts import render, redirect
from . import models
from . import form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def projects(request):
    q = ''
    if request.GET.get('q'):
        q = request.GET.get('q')

    all_projects = models.Project.objects.distinct().filter(
        Q(title__icontains=q) | Q(developer__name__icontains=q) | Q(tags__name=q))
    return render(request, 'projects/projects.html', {'title': 'home page', 'projects': all_projects})


def project(request, pk):
    Project = models.Project.objects.get(id=pk)

    if request.method == 'POST':
        print(request.POST)
        reviewform = form.ReviewForm(request.POST)
        review = reviewform.save(commit=False)
        review.owner = request.user.profile
        review.project = Project
        review.save()
        Project.getVoteCount
        return redirect('projects', pk=Project.id)


    print(request.user.profile.id in Project.reviewers)
    print(request.user.profile.id)
    tags = Project.tags.all()
    reviewform = form.ReviewForm()

    return render(request, 'projects/project.html',
                  {'title': Project.title, 'project': Project, 'tags': tags, 'reviewform': reviewform})


@login_required(login_url='user_login')
def create_project(request):
    project_form = None
    if request.method == 'POST':
        project_form = form.ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.developer = request.user.profile
            project_form.save()
            messages.success(request, 'project added successfully')

            return redirect('user_account')

    project_form = form.ProjectForm()
    context = {'project_form': project_form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='user_login')
def update_project(request, pk):
    project = models.Project.objects.get(id=pk)
    project_form = None
    if request.method == 'POST':
        project_form = form.ProjectForm(request.POST, request.FILES, instance=project)
        if project_form.is_valid():
            project_form.save()
            messages.success(request, 'project updated successfully')
            return redirect('user_account')

    project_form = form.ProjectForm(instance=project)
    context = {'project_form': project_form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='user_login')
def delete_project(request, pk):
    project = models.Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'project deleted successfully')
        return redirect('user_account')

    context = {'object': project}
    return render(request, 'delete_template.html', context)
