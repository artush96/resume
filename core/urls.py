from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('reset/', reset, name='reset'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('works/', works, name='works'),
    path('works/<category_slug>/', works, name='works_by_category'),
    path('resume/', resume, name='resume'),
    path('general/change/', gen_change, name='gen_change'),
    path('general/create/', gen_create, name='gen_create'),
    path('general/edit/<id>/', gen_edit, name='gen_edit'),
    path('general/delete/<id>/', gen_delete, name='gen_delete'),

    path('home/change/', home_change, name='home_change'),
    path('about/create/', about_me_create, name='about_me_create'),
    path('about/edit/<id>/', about_me_edit, name='about_me_edit'),
    path('about/delete/<id>/', about_me_delete, name='about_me_delete'),
    path('services/create/', my_services_create, name='my_services_create'),
    path('services/edit/<id>/', my_services_edit, name='my_services_edit'),
    path('services/delete/<id>/', my_services_delete, name='my_services_delete'),
    path('pricing/create/', pricing_create, name='pricing_create'),
    path('pricing/edit/<id>/', pricing_edit, name='pricing_edit'),
    path('pricing/delete/<id>/', pricing_delete, name='pricing_delete'),
    path('fact/create/', facts_create, name='facts_create'),
    path('fact/edit/<id>/', facts_edit, name='facts_edit'),
    path('fact/delete/<id>/', facts_delete, name='facts_delete'),
    path('client/create/', client_create, name='client_create'),
    path('client/edit/<id>/', client_edit, name='client_edit'),
    path('client/delete/<id>/', client_delete, name='client_delete'),

    path('contacts/change/', contact_change, name='contact_change'),
    path('contact/create/', contact_create, name='contact_create'),
    path('contact/edit/<id>/', contact_edit, name='contact_edit'),
    path('contact/delete/<id>/', contact_delete, name='contact_delete'),

    path('myworks/change/', works_change, name='works_change'),
    path('myworks/change/<category_slug>/', works_change, name='works_change_bycategory'),
    path('work/create/', work_create, name='work_create'),
    path('work/edit/<id>/', work_edit, name='work_edit'),
    path('work/delete/<id>/', work_delete, name='work_delete'),
    path('category/create/', cat_create, name='cat_create'),
    path('category/edit/<id>/', cat_edit, name='cat_edit'),
    path('category/delete/<id>/', cat_delete, name='cat_delete'),

    path('resume/change/', resume_change, name='resume_change'),
    path('experience/create/', exp_create, name='exp_create'),
    path('experience/edit/<id>/', exp_edit, name='exp_edit'),
    path('experience/delete/<id>/', exp_delete, name='exp_delete'),
    path('skill/create/', skill_create, name='skill_create'),
    path('skill/edit/<id>/', skill_edit, name='skill_edit'),
    path('skill/delete/<id>/', skill_delete, name='skill_delete'),
    path('edu/create/', edu_create, name='edu_create'),
    path('edu/edit/<id>/', edu_edit, name='edu_edit'),
    path('edu/delete/<id>/', edu_delete, name='edu_delete'),
    path('wexp/create/', wexp_create, name='wexp_create'),
    path('wexp/edit/<id>/', wexp_edit, name='wexp_edit'),
    path('wexp/delete/<id>/', wexp_delete, name='wexp_delete'),
]


























































