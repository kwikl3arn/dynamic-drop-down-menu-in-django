from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from kwiklapp.models import main_menu, sub_menu


# Create your views here.

def countown(request):
    return render(request, 'count.html')


def maninmenu(request):
    menu = main_menu.objects.all()
    submenu=sub_menu.objects.all()
    return render(request, 'menu.html', {'menu': menu,'submenu':submenu})


def mainsave(request):
    if request.method == 'POST':
        mname = request.POST['menu_name']
        mlink = request.POST['mn_link']
        main_menu.objects.create(m_menu_name=mname, m_menu_link=mlink)
        # return HttpResponse("created")
        return redirect('mainmenu')
    else:
        return redirect('mainmenu')


def subsave(request):
    if request.method == 'POST':
        menuid=request.POST['parent']
        sname=request.POST['sub_menu_name']
        slink=request.POST['sub_menu_link']
        sub_menu.objects.create(m_menu_id=menuid,s_menu_name=sname,s_menu_link=slink)
        return redirect('mainmenu')
    else:
        return redirect('mainmenu')

def dynamic_menu(request):
    menu = main_menu.objects.all()
    submenu = sub_menu.objects.all()
    return render(request, 'dynamic_menu.html', {'menu': menu, 'submenu': submenu})