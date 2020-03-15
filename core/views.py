from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *


# View functions
def reset(request):
    About.objects.using('demo_db').exclude(user_id=1).delete()
    AboutMe.objects.using('demo_db').exclude(user_id=1).delete()
    Services.objects.using('demo_db').exclude(user_id=1).delete()
    Pricing.objects.using('demo_db').exclude(user_id=1).delete()
    Facts.objects.using('demo_db').exclude(user_id=1).delete()
    Clients.objects.using('demo_db').exclude(user_id=1).delete()
    Contact.objects.using('demo_db').exclude(user_id=1).delete()
    Category.objects.using('demo_db').exclude(user_id=1).delete()
    Works.objects.using('demo_db').exclude(user_id=1).delete()
    Skills.objects.using('demo_db').exclude(user_id=1).delete()
    Experience.objects.using('demo_db').exclude(user_id=1).delete()
    Education.objects.using('demo_db').exclude(user_id=1).delete()
    WorkExprerience.objects.using('demo_db').exclude(user_id=1).delete()
    return redirect('core:home')

def home(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        about = AboutMe.objects.using('default').last()
        services = Services.objects.using('default').last()
        pricing = Pricing.objects.using('default').last()
        facts = Facts.objects.using('default').last()
        clients = Clients.objects.using('default').all()
        aboutme = About.objects.using('default').last()
    else:
        about = AboutMe.objects.using('demo_db').last()
        services = Services.objects.using('demo_db').last()
        pricing = Pricing.objects.using('demo_db').last()
        facts = Facts.objects.using('demo_db').last()
        clients = Clients.objects.using('demo_db').all()
        aboutme = About.objects.using('demo_db').last()

    context = {
        'about': about,
        'services': services,
        'pricing': pricing,
        'facts': facts,
        'clients': clients,
        'aboutme': aboutme,
    }

    return render(request, 'core/home.html', context)

def contact(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        contacts = Contact.objects.using('default').last()
        aboutme = About.objects.using('default').last()
    else:
        contacts = Contact.objects.using('demo_db').last()
        aboutme = About.objects.using('demo_db').last()

    context = {
        'contacts': contacts,
        'aboutme': aboutme,
    }

    return render(request, 'core/contactme.html', context)

def blog(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        blog = Blog.objects.using('default').all()
        aboutme = About.objects.using('default').last()
    else:
        blog = Blog.objects.using('demo_db').all()
        aboutme = About.objects.using('demo_db').last()
    context = {
        'blog': blog,
        'aboutme': aboutme,
    }
    return render(request, 'core/myblog.html', context)

def works(request, category_slug=None):
    if request.user.is_superuser or not request.user.is_authenticated:
        category = None
        work = Works.objects.using('default').all()
        categoryis = Category.objects.using('default')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            work = Works.objects.using('default').filter(category=category)
        aboutme = About.objects.using('default').last()
    else:
        category = None
        work = Works.objects.using('demo_db').all()
        categoryis = Category.objects.using('demo_db')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            work = Works.objects.using('demo_db').filter(category=category)
        aboutme = About.objects.using('demo_db').last()
    context = {
        'work': work,
        'categoryis': categoryis,
        'category': category,
        'aboutme': aboutme,
    }

    return render(request, 'core/myworks.html', context)

def resume(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        experience = Experience.objects.using('default').last()
        skills = Skills.objects.using('default').all()
        education = Education.objects.using('default').all()
        workexperience = WorkExprerience.objects.using('default').all()
        aboutme = About.objects.using('default').last()
    else:
        experience = Experience.objects.using('demo_db').last()
        skills = Skills.objects.using('demo_db').all()
        education = Education.objects.using('demo_db').all()
        workexperience = WorkExprerience.objects.using('demo_db').all()
        aboutme = About.objects.using('demo_db').last()

    context = {
        'experience': experience,
        'skills': skills,
        'education': education,
        'workexperience': workexperience,
        'aboutme': aboutme,
    }

    return render(request, 'core/resume.html', context)

# Change home page functions
@login_required(login_url='/admin/')
def home_change(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        about = AboutMe.objects.using('default').last()
        services = Services.objects.using('default').last()
        pricing = Pricing.objects.using('default').last()
        facts = Facts.objects.using('default').last()
        clients = Clients.objects.using('default').all()
        aboutme = About.objects.using('default').last()
    else:
        about = AboutMe.objects.using('demo_db').last()
        services = Services.objects.using('demo_db').last()
        pricing = Pricing.objects.using('demo_db').last()
        facts = Facts.objects.using('demo_db').last()
        clients = Clients.objects.using('demo_db').all()
        aboutme = About.objects.using('demo_db').last()
    context = {
        'about': about,
        'services': services,
        'pricing': pricing,
        'facts': facts,
        'clients': clients,
        'aboutme': aboutme,
    }

    return render(request, 'core/dash/change/home_change.html', context)

@login_required(login_url='/admin/')
def about_me_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            a_form = AboutMeCreateForm(request.POST)
            if a_form.is_valid():
                a = a_form.save(commit=False)
                a.user = request.user
                a.save(using='default')
                a_form = AboutMeCreateForm()
        else:
            a_form = AboutMeCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            a_form = AboutMeCreateForm(request.POST)
            if a_form.is_valid():
                a = a_form.save(commit=False)
                a.user = request.user
                a.save(using='demo_db')
                a_form = AboutMeCreateForm()
        else:
            a_form = AboutMeCreateForm()
    context = {
        'a_form': a_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/about_me_change.html', context)

@login_required(login_url='/admin/')
def about_me_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        a_query = AboutMe.objects.using('default')
        a_obj = get_object_or_404(a_query, id=id)
        a_form = AboutMeCreateForm(request.POST or None, instance=a_obj)
        if a_form.is_valid():
            a = a_form.save(commit=False)
            a.user = request.user
            a.save(using='default')
            return redirect('core:home_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        a_query = AboutMe.objects.using('demo-db').all
        a_obj = get_object_or_404(a_query, id=id)
        a_form = AboutMeCreateForm(request.POST or None, instance=a_obj)
        if a_form.is_valid():
            a = a_form.save(commit=False)
            a.user = request.user
            a.save(using='demo_db')
            return redirect('core:home_change')

    context = {
        'a_form': a_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/about_me_change.html', context)

@login_required(login_url='/admin/')
def about_me_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = AboutMe.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = AboutMe.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:home_change')

@login_required(login_url='/admin/')
def my_services_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            s_form = ServicesCreateForm(request.POST)
            if s_form.is_valid():
                s = s_form.save(commit=False)
                s.user = request.user
                s.save(using='default')
                s_form = ServicesCreateForm()
        else:
            s_form = ServicesCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            s_form = ServicesCreateForm(request.POST)
            if s_form.is_valid():
                s = s_form.save(commit=False)
                s.user = request.user
                s.save(using='demo_db')
                s_form = ServicesCreateForm()
        else:
            s_form = ServicesCreateForm()
    context = {
        's_form': s_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/my_services_change.html', context)

@login_required(login_url='/admin/')
def my_services_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        s_query = Services.objects.using('default').all()
        s_obj = get_object_or_404(s_query, id=id)
        s_form = ServicesCreateForm(request.POST or None, instance=s_obj)
        if s_form.is_valid():
            s = s_form.save(commit=False)
            s.user = request.user
            s.save(using='default')
            return redirect('core:home_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        s_query = Services.objects.using('demo_db').all()
        s_obj = get_object_or_404(s_query, id=id)
        s_form = ServicesCreateForm(request.POST or None, instance=s_obj)
        if s_form.is_valid():
            s = s_form.save(commit=False)
            s.user = request.user
            s.save(using='demo_db')
            return redirect('core:home_change')

    context = {
        's_form': s_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/my_services_change.html', context)

@login_required(login_url='/admin/')
def my_services_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = Services.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = Services.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:home_change')

@login_required(login_url='/admin/')
def pricing_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            p_form = PricingCreateForm(request.POST)
            if p_form.is_valid():
                p = p_form.save(commit=False)
                p.user = request.user
                p.save(using='default')
                p_form = PricingCreateForm()
        else:
            p_form = PricingCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            p_form = PricingCreateForm(request.POST)
            if p_form.is_valid():
                p = p_form.save(commit=False)
                p.user = request.user
                p.save(using='demo_db')
                p_form = PricingCreateForm()
        else:
            p_form = PricingCreateForm()

    context = {
        'p_form': p_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/pricing_change.html', context)

@login_required(login_url='/admin/')
def pricing_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        p_query = Pricing.objects.using('default').all()
        p_obj = get_object_or_404(p_query, id=id)
        p_form = PricingCreateForm(request.POST or None, instance=p_obj)
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.user = request.user
            p.save(using='default')
            return redirect('core:home_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        p_query = Pricing.objects.using('demo_db').all()
        p_obj = get_object_or_404(p_query, id=id)
        p_form = PricingCreateForm(request.POST or None, instance=p_obj)
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.user = request.user
            p.save(using='demo_db')
            return redirect('core:home_change')

    context = {
        'p_form': p_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/pricing_change.html', context)

@login_required(login_url='/admin/')
def pricing_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = Pricing.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = Pricing.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:home_change')

@login_required(login_url='/admin/')
def facts_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            f_form = FactsCreateForm(request.POST)
            if f_form.is_valid():
                f = f_form.save(commit=False)
                f.user = request.user
                f.save(using='default')
                f_form = FactsCreateForm()
                return redirect('core:home_change')
        else:
            f_form = FactsCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            f_form = FactsCreateForm(request.POST)
            if f_form.is_valid():
                f = f_form.save(commit=False)
                f.user = request.user
                f.save(using='demo_db')
                f_form = FactsCreateForm()
                return redirect('core:home_change')
        else:
            f_form = FactsCreateForm()
    context = {
        'f_form': f_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/facts_change.html', context)

@login_required(login_url='/admin/')
def facts_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        f_query = Facts.objects.using('default').all()
        f_obj = get_object_or_404(f_query, id=id)
        f_form = FactsCreateForm(request.POST or None, instance=f_obj)
        if f_form.is_valid():
            f = f_form.save(commit=False)
            f.user = request.user
            f.save(using='default')
            return redirect('core:home_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        f_query = Facts.objects.using('demo_db').all()
        f_obj = get_object_or_404(f_query, id=id)
        f_form = FactsCreateForm(request.POST or None, instance=f_obj)
        if f_form.is_valid():
            f = f_form.save(commit=False)
            f.user = request.user
            f.save(using='demo_db')
            return redirect('core:home_change')

    context = {
        'f_form': f_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/facts_change.html', context)

@login_required(login_url='/admin/')
def facts_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = Facts.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = Facts.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:home_change')

@login_required(login_url='/admin/')
def client_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            c_form = ClientsCreateForm(request.POST, request.FILES)
            if c_form.is_valid():
                c = c_form.save(commit=False)
                c.user = request.user
                c.save(using='default')
                return redirect('core:home_change')
        else:
            c_form = ClientsCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            c_form = ClientsCreateForm(request.POST, request.FILES)
            if c_form.is_valid():
                c = c_form.save(commit=False)
                c.user = request.user
                c.save(using='demo_db')
                return redirect('core:home_change')
        else:
            c_form = ClientsCreateForm()
    context = {
        'c_form': c_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/client_change.html', context)

@login_required(login_url='/admin/')
def client_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        c_query = Clients.objects.using('default').all()
        c_obj = get_object_or_404(c_query, id=id)
        c_form = ClientsCreateForm(request.POST or None, request.FILES or None, instance=c_obj)
        if c_form.is_valid():
            c = c_form.save(commit=False)
            c.user = request.user
            c.save(using='default')
            return redirect('core:home_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        c_query = Clients.objects.using('demo_db').all()
        c_obj = get_object_or_404(c_query, id=id)
        c_form = ClientsCreateForm(request.POST or None, request.FILES or None, instance=c_obj)
        if c_form.is_valid():
            c = c_form.save(commit=False)
            c.user = request.user
            c.save(using='demo_db')
            return redirect('core:home_change')

    context = {
        'c_form': c_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/client_change.html', context)

@login_required(login_url='/admin/')
def client_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = Clients.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = Clients.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:home_change')

# Change contact page functions
@login_required(login_url='/admin/')
def contact_change(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        contacts = Contact.objects.using('default').last()
        aboutme = About.objects.using('default').last()
    else:
        contacts = Contact.objects.using('demo_db').last()
        aboutme = About.objects.using('demo_db').last()
    context = {
        'contacts': contacts,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/contact_change.html', context)

@login_required(login_url='/admin/')
def contact_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            co_form = ContactCreateForm(request.POST)
            if co_form.is_valid():
                co = co_form.save(commit=False)
                co.user = request.user
                co.save(using='default')
                co_form = ContactCreateForm()
                return redirect('core:contact_change')
        else:
            co_form = ContactCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            co_form = ContactCreateForm(request.POST)
            if co_form.is_valid():
                co = co_form.save(commit=False)
                co.user = request.user
                co.save(using='demo_db')
                co_form = ContactCreateForm()
                return redirect('core:contact_change')
        else:
            co_form = ContactCreateForm()
    context = {
        'co_form': co_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/contact_me_change.html', context)

@login_required(login_url='/admin/')
def contact_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        co_query = Contact.objects.using('default')
        co_obj = get_object_or_404(co_query, id=id)
        co_form = ContactCreateForm(request.POST or None, instance=co_obj)
        if co_form.is_valid():
            co = co_form.save(commit=False)
            co.user = request.user
            co.save(using='default')
            co_form = ContactCreateForm()
            return redirect('core:contact_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        co_query = Contact.objects.using('demo_db')
        co_obj = get_object_or_404(co_query, id=id)
        co_form = ContactCreateForm(request.POST or None, instance=co_obj)
        if co_form.is_valid():
            co = co_form.save(commit=False)
            co.user = request.user
            co.save(using='demo_db')
            co_form = ContactCreateForm()
            return redirect('core:contact_change')
    context = {
        'co_form': co_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/contact_me_change.html', context)

@login_required(login_url='/admin/')
def contact_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        obj = Contact.objects.using('default').get(id=id)
        obj.delete()
    else:
        obj = Contact.objects.using('demo_db').get(id=id)
        obj.delete()
    return redirect('core:contact_change')

# Change works page functions
@login_required(login_url='/admin/')
def works_change(request, category_slug=None):
    if request.user.is_superuser or not request.user.is_authenticated:
        category = None
        work = Works.objects.using('default').all()
        categoryis = Category.objects.using('default')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            work = Works.objects.using('default').filter(category=category)
        aboutme = About.objects.using('default').last()
    else:
        category = None
        work = Works.objects.using('demo_db').all()
        categoryis = Category.objects.using('demo_db')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            work = Works.objects.using('demo_db').filter(category=category)
        aboutme = About.objects.using('demo_db').last()
    context = {
        'work': work,
        'categoryis': categoryis,
        'category': category,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/my_works_change.html', context)

@login_required(login_url='/admin/')
def work_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            w_form = WorksCreateForm(request.POST, request.FILES)
            if w_form.is_valid():
                w = w_form.save(commit=False)
                w.user = request.user
                w.save(using='default')
                w_form = WorksCreateForm()
        else:
            w_form = WorksCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            w_form = WorksCreateForm(request.POST, request.FILES)
            if w_form.is_valid():
                w = w_form.save(commit=False)
                w.user = request.user
                w.save(using='demo_db')
                w_form = WorksCreateForm()
        else:
            w_form = WorksCreateForm()
    context = {
        'w_form': w_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/works_change.html', context)

@login_required(login_url='/admin/')
def work_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        w_query = Works.objects.using('default')
        w_obj = get_object_or_404(w_query, id=id)
        w_form = WorksCreateForm(request.POST or None, request.FILES or None, instance=w_obj)
        if w_form.is_valid():
            w = w_form.save(commit=False)
            w.user = request.user
            w.save(using='default')
            w_form = WorksCreateForm()
            return redirect('/myworks/change/web-development/')
    else:
        aboutme = About.objects.using('demo_db').last()
        w_query = Works.objects.using('demo_db')
        w_obj = get_object_or_404(w_query, id=id)
        w_form = WorksCreateForm(request.POST or None, request.FILES or None, instance=w_obj)
        if w_form.is_valid():
            w = w_form.save(commit=False)
            w.user = request.user
            w.save(using='demo_db')
            w_form = WorksCreateForm()
            return redirect('/myworks/change/web-development/')
    context = {
        'w_form': w_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/works_change.html', context)

@login_required(login_url='/admin/')
def work_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        work = Works.objects.using('default').get(id=id)
        work.delete()
    else:
        work = Works.objects.using('demo_db').get(id=id)
        work.delete()
    return redirect('/myworks/change/web-development/')

@login_required(login_url='/admin/')
def cat_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            cat_form = CategoryCreateForm(request.POST)
            if cat_form.is_valid():
                cf = cat_form.save(commit=False)
                cf.user = request.user
                cf.save(using='default')
                cat_form = CategoryCreateForm()
                return redirect('/myworks/change/web-development/')
        else:
            cat_form = CategoryCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            cat_form = CategoryCreateForm(request.POST)
            if cat_form.is_valid():
                cf = cat_form.save(commit=False)
                cf.user = request.user
                cf.save(using='demo_db')
                cat_form = CategoryCreateForm()
                return redirect('/myworks/change/web-development/')
        else:
            cat_form = CategoryCreateForm()
    context = {
        'cat_form': cat_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/cat_change.html', context)

@login_required(login_url='/admin/')
def cat_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        cat_query = Category.objects.using('default')
        cat_obj = get_object_or_404(cat_query, id=id)
        cat_form = CategoryCreateForm(request.POST or None, instance=cat_obj)
        if cat_form.is_valid():
            cat = cat_form.save(commit=False)
            cat.user = request.user
            cat.save(using='default')
            cat_form = CategoryCreateForm()
            return redirect('/myworks/change/web-development/')
    else:
        aboutme = About.objects.using('demo_db').last()
        cat_query = Category.objects.using('demo_db')
        cat_obj = get_object_or_404(cat_query, id=id)
        cat_form = CategoryCreateForm(request.POST or None, instance=cat_obj)
        if cat_form.is_valid():
            cat = cat_form.save(commit=False)
            cat.user = request.user
            cat.save(using='demo_db')
            cat_form = CategoryCreateForm()
            return redirect('/myworks/change/web-development/')
    context = {
        'cat_form': cat_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/cat_change.html', context)

@login_required(login_url='/admin/')
def cat_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        cat = Category.objects.using('default').get(id=id)
        cat.delete()
    else:
        cat = Category.objects.using('demo_db').get(id=id)
        cat.delete()
    return redirect('/myworks/change/web-development/')

# Change resume page functions
@login_required(login_url='/admin/')
def resume_change(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        experience = Experience.objects.using('default').last()
        skills = Skills.objects.using('default').all()
        education = Education.objects.using('default').all()
        workexperience = WorkExprerience.objects.using('default').all()
        aboutme = About.objects.using('default').last()
    else:
        experience = Experience.objects.using('demo_db').last()
        skills = Skills.objects.using('demo_db').all()
        education = Education.objects.using('demo_db').all()
        workexperience = WorkExprerience.objects.using('demo_db').all()
        aboutme = About.objects.using('demo_db').last()
    context = {
        'experience': experience,
        'skills': skills,
        'education': education,
        'workexperience': workexperience,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/resume_change.html', context)

@login_required(login_url='/admin/')
def exp_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            e_form = ExperienceCreateForm(request.POST)
            if e_form.is_valid():
                e = e_form.save(commit=False)
                e.user = request.user
                e.save(using='default')
                e_form = ExperienceCreateForm()
                return redirect('core:resume_change')
        else:
            e_form = ExperienceCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            e_form = ExperienceCreateForm(request.POST)
            if e_form.is_valid():
                e = e_form.save(commit=False)
                e.user = request.user
                e.save(using='demo_db')
                e_form = ExperienceCreateForm()
                return redirect('core:resume_change')
        else:
            e_form = ExperienceCreateForm()
    context = {
        'e_form': e_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/exp_change.html', context)

@login_required(login_url='/admin/')
def exp_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        e_query = Experience.objects.using('default')
        e_obj = get_object_or_404(e_query, id=id)
        e_form = ExperienceCreateForm(request.POST or None, instance=e_obj)
        if e_form.is_valid():
            e = e_form.save(commit=False)
            e.user = request.user
            e.save(using='default')
            e_form = ExperienceCreateForm()
            return redirect('core:resume_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        e_query = Experience.objects.using('demo_db')
        e_obj = get_object_or_404(e_query, id=id)
        e_form = ExperienceCreateForm(request.POST or None, instance=e_obj)
        if e_form.is_valid():
            e = e_form.save(commit=False)
            e.user = request.user
            e.save(using='demo_db')
            e_form = ExperienceCreateForm()
            return redirect('core:resume_change')
    context = {
        'e_form': e_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/exp_change.html', context)

@login_required(login_url='/admin/')
def exp_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        exp = Experience.objects.using('default').get(id=id)
        exp.delete()
    else:
        exp = Experience.objects.using('demo_db').get(id=id)
        exp.delete()
    return redirect('core:resume_change')

@login_required(login_url='/admin/')
def skill_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            s_form = SkillsCreateForm(request.POST)
            if s_form.is_valid():
                s = s_form.save(commit=False)
                s.user = request.user
                s.save(using='default')
                s_form = SkillsCreateForm()
                return redirect('core:resume_change')
        else:
            s_form = SkillsCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            s_form = SkillsCreateForm(request.POST)
            if s_form.is_valid():
                s = s_form.save(commit=False)
                s.user = request.user
                s.save(using='demo_db')
                s_form = SkillsCreateForm()
                return redirect('core:resume_change')
        else:
            s_form = SkillsCreateForm()
    context = {
        's_form': s_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/skill_change.html', context)

@login_required(login_url='/admin/')
def skill_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        s_query = Skills.objects.using('default')
        s_obj = get_object_or_404(s_query, id=id)
        s_form = SkillsCreateForm(request.POST or None, instance=s_obj)
        if s_form.is_valid():
            s = s_form.save(commit=False)
            s.user = request.user
            s.save(using='default')
            s_form = ServicesCreateForm()
            return redirect('core:resume_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        s_query = Skills.objects.using('demo_db')
        s_obj = get_object_or_404(s_query, id=id)
        s_form = SkillsCreateForm(request.POST or None, instance=s_obj)
        if s_form.is_valid():
            s = s_form.save(commit=False)
            s.user = request.user
            s.save(using='demo_db')
            s_form = ServicesCreateForm()
            return redirect('core:resume_change')

    context = {
        's_form': s_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/skill_change.html', context)

@login_required(login_url='/admin/')
def skill_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        skill = Skills.objects.using('default').get(id=id)
        skill.delete()
    else:
        skill = Skills.objects.using('demo_db').get(id=id)
        skill.delete()
    return redirect('core:resume_change')

@login_required(login_url='/admin/')
def edu_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            ed_form = EducationCreateForm(request.POST)
            if ed_form.is_valid():
                ed = ed_form.save(commit=False)
                ed.user = request.user
                ed.save(using='default')
                ed_form = EducationCreateForm()
                return redirect('core:resume_change')
        else:
            ed_form = EducationCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            ed_form = EducationCreateForm(request.POST)
            if ed_form.is_valid():
                ed = ed_form.save(commit=False)
                ed.user = request.user
                ed.save(using='demo_db')
                ed_form = EducationCreateForm()
                return redirect('core:resume_change')
        else:
            ed_form = EducationCreateForm()
    context = {
        'ed_form': ed_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/edu_change.html', context)

@login_required(login_url='/admin/')
def edu_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        ed_query = Education.objects.using('default')
        ed_obj = get_object_or_404(ed_query, id=id)
        ed_form = EducationCreateForm(request.POST or None, instance=ed_obj)
        if ed_form.is_valid():
            ed = ed_form.save(commit=False)
            ed.user = request.user
            ed.save(using='default')
            ed_form = ServicesCreateForm()
            return redirect('core:resume_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        ed_query = Education.objects.using('demo_db')
        ed_obj = get_object_or_404(ed_query, id=id)
        ed_form = EducationCreateForm(request.POST or None, instance=ed_obj)
        if ed_form.is_valid():
            ed = ed_form.save(commit=False)
            ed.user = request.user
            ed.save(using='demo_db')
            ed_form = ServicesCreateForm()
            return redirect('core:resume_change')
    context = {
        'ed_form': ed_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/edu_change.html', context)

@login_required(login_url='/admin/')
def edu_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        edu = Education.objects.using('default').get(id=id)
        edu.delete()
    else:
        edu = Education.objects.using('demo_db').get(id=id)
        edu.delete()
    return redirect('core:resume_change')

@login_required(login_url='/admin/')
def wexp_create(request):
    if not request.user.is_superuser:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            wex_form = WorkExprerienceCreateForm(request.POST)
            if wex_form.is_valid():
                wex = wex_form.save(commit=False)
                wex.user = request.user
                wex.save(using='default')
                wex_form = WorkExprerienceCreateForm()
                return redirect('core:resume_change')
        else:
            wex_form = WorkExprerienceCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            wex_form = WorkExprerienceCreateForm(request.POST)
            if wex_form.is_valid():
                wex = wex_form.save(commit=False)
                wex.user = request.user
                wex.save(using='demo_db')
                wex_form = WorkExprerienceCreateForm()
                return redirect('core:resume_change')
        else:
            wex_form = WorkExprerienceCreateForm()
    context = {
        'wex_form': wex_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/wexp_change.html', context)

@login_required(login_url='/admin/')
def wexp_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        wex_query = WorkExprerience.objects.using('default')
        wex_obj = get_object_or_404(wex_query, id=id)
        wex_form = WorkExprerienceCreateForm(request.POST or None, instance=wex_obj)
        if wex_form.is_valid():
            wex = wex_form.save(commit=False)
            wex.user = request.user
            wex.save(using='default')
            wex_form = WorkExprerienceCreateForm()
            return redirect('core:resume_change')
    else:
        aboutme = About.objects.using('demo_db').last()
        wex_query = WorkExprerience.objects.using('demo_db')
        wex_obj = get_object_or_404(wex_query, id=id)
        wex_form = WorkExprerienceCreateForm(request.POST or None, instance=wex_obj)
        if wex_form.is_valid():
            wex = wex_form.save(commit=False)
            wex.user = request.user
            wex.save(using='demo_db')
            wex_form = WorkExprerienceCreateForm()
            return redirect('core:resume_change')
    context = {
        'wex_form': wex_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/change/wexp_change.html', context)

@login_required(login_url='/admin/')
def wexp_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        wex = WorkExprerience.objects.using('default').get(id=id)
        wex.delete()
    else:
        wex = WorkExprerience.objects.using('demo_db').get(id=id)
        wex.delete()
    return redirect('core:resume_change')

@login_required(login_url='/admin/')
def gen_change(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
    else:
        aboutme = About.objects.using('demo_db').last()
    contact = {
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/base_change.html', contact)

@login_required(login_url='/admin/')
def gen_create(request):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        if request.method == 'POST':
            about_form = AboutCreateForm(request.POST, request.FILES)
            if about_form.is_valid():
                about = about_form.save(commit=False)
                about.user = request.user
                about.save(using='default')
                return redirect('core:gen_change')
        else:
            about_form = AboutCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        if request.method == 'POST':
            about_form = AboutCreateForm(request.POST, request.FILES)
            if about_form.is_valid():
                about = about_form.save(commit=False)
                about.user = request.user
                about.save(using='demo_db')
                return redirect('core:gen_change')
        else:
            about_form = AboutCreateForm()
    context = {
        'about_form': about_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/general_change.html', context)

@login_required(login_url='/admin/')
def gen_edit(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        aboutme = About.objects.using('default').last()
        about_query = About.objects.using('default')
        obj_1 = get_object_or_404(about_query, id=id)
        about_form = AboutCreateForm(request.POST or None, request.FILES or None, instance=obj_1)
        if about_form.is_valid():
            about = about_form.save(commit=False)
            about.user = request.user
            about.save(using='default')
            return redirect('core:gen_change')
        else:
            about_form = AboutCreateForm()
    else:
        aboutme = About.objects.using('demo_db').last()
        about_query = About.objects.using('demo_db')
        obj_1 = get_object_or_404(about_query, id=id)
        about_form = AboutCreateForm(request.POST or None, request.FILES or None, instance=obj_1)
        if about_form.is_valid():
            about = about_form.save(commit=False)
            about.user = request.user
            about.save(using='demo_db')
            return redirect('core:gen_change')
        else:
            about_form = AboutCreateForm()
    context = {
        'about_form': about_form,
        'aboutme': aboutme,
    }
    return render(request, 'core/dash/general_change.html', context)

@login_required(login_url='/admin/')
def gen_delete(request, id):
    if request.user.is_superuser or not request.user.is_authenticated:
        gen = About.objects.using('default').get(id=id)
        gen.delete()
    else:
        gen = About.objects.using('demo_db').get(id=id)
        gen.delete()
    return redirect('core:gen_change')

from django.template import RequestContext
def handler404(request, exception):
    aboutme = About.objects.using('default').last()
    context = RequestContext(request)
    response = render('404.html', {'aboutme': aboutme}, context)
    response.status_code = 404
    return response


# def handler500(request):
#     aboutme = About.objects.using('default').last()
#     context = {
#         'aboutme': aboutme,
#     }
#     return render(request, '500.html', context)