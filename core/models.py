import sys

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
from unidecode import unidecode


def gen_slug(s):
    new_slug = slugify(unidecode(s))
    return new_slug


class About(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    img = models.ImageField(upload_to='profile/', blank=True, verbose_name='Profile Picture')
    name = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Full Name')
    speciality = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Speciality')
    cv = models.FileField(upload_to='pdf', blank=True, verbose_name='CV File')
    fb = models.CharField(max_length=60, blank=True, db_index=True, verbose_name='Facebook')
    lin = models.CharField(max_length=60, blank=True, db_index=True, verbose_name='LinkedIn')
    gt = models.CharField(max_length=60, blank=True, db_index=True, verbose_name='GitHub')
    tm = models.CharField(max_length=60, blank=True, db_index=True, verbose_name='Telegram')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        image = Image.open(self.img)
        output = BytesIO()
        image.save(output, optimize=True, format='JPEG', quality=55)
        output.seek(0)
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)
        super(About, self).save(*args, **kwargs)


class AboutMe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    age = models.CharField(max_length=4, db_index=True, verbose_name='Age')
    location = models.CharField(max_length=30, db_index=True, verbose_name='Location')
    specialty = models.CharField(max_length=30, db_index=True, verbose_name='Specialty')
    body = models.TextField(max_length=3000, blank=True, verbose_name='Body')

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'Abaut Me'

    def __str__(self):
        return self.location


class Services(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    title_1 = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Service Name')
    body_1 = models.TextField(max_length=2000, blank=True, verbose_name='Service Characteristics')
    title_2 = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Service Name')
    body_2 = models.TextField(max_length=2000, blank=True, verbose_name='Service Characteristics')
    title_3 = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Service Name')
    body_3 = models.TextField(max_length=2000, blank=True, verbose_name='Service Characteristics')
    title_4 = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Service Name')
    body_4 = models.TextField(max_length=2000, blank=True, verbose_name='Service Characteristics')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title_1


class Pricing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    title_l = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Pricing Plain')
    price_l = models.CharField(max_length=15, blank=True, db_index=True, verbose_name='Price')
    option_l_1 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_l_2 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_l_3 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_l_4 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')

    title_c = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Pricing Plain')
    price_c = models.CharField(max_length=15, blank=True, db_index=True, verbose_name='Price')
    option_c_1 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_c_2 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_c_3 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_c_4 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')

    title_r = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Pricing Plain')
    price_r = models.CharField(max_length=15, blank=True, db_index=True, verbose_name='Price')
    option_r_1 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_r_2 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_r_3 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')
    option_r_4 = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Option')

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'

    def __str__(self):
        return self.title_l


class Facts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    count_1 = models.CharField(max_length=6, blank=True, db_index=True, verbose_name='Fact Cunt')
    fact_1 = models.CharField(max_length=20, blank=True, db_index=True, verbose_name='Fact')
    count_2 = models.CharField(max_length=6, blank=True, db_index=True, verbose_name='Fact Cunt')
    fact_2 = models.CharField(max_length=20, blank=True, db_index=True, verbose_name='Fact')
    count_3 = models.CharField(max_length=6, blank=True, db_index=True, verbose_name='Fact Cunt')
    fact_3 = models.CharField(max_length=20, blank=True, db_index=True, verbose_name='Fact')
    count_4 = models.CharField(max_length=6, blank=True, db_index=True, verbose_name='Fact Cunt')
    fact_4 = models.CharField(max_length=20, blank=True, db_index=True, verbose_name='Fact')

    class Meta:
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'

    def __str__(self):
        return self.fact_1


class Clients(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    client_logo = models.ImageField(upload_to='client_logo/', default='', verbose_name='Client Logo')
    client_url = models.CharField(max_length=30, db_index=True, verbose_name='Client Url')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.client_url

    def save(self, *args, **kwargs):
        image = Image.open(self.client_logo)
        output = BytesIO()
        image.save(output, optimize=True, format='JPEG', quality=55)
        output.seek(0)
        self.client_logo = InMemoryUploadedFile(output, 'ImageField',
                                                "%s.jpg" % self.client_logo.name.split('.')[0], 'image/jpeg',
                                                sys.getsizeof(output), None)
        super(Clients, self).save(*args, **kwargs)


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    introduction = models.TextField(max_length=2000, blank=True, verbose_name='Introduction')
    location = models.CharField(max_length=20, blank=True, db_index=True, verbose_name='Location')
    phone = models.CharField(max_length=15, db_index=True, verbose_name='Phone')
    mail = models.CharField(max_length=30, db_index=True, verbose_name='Mail')
    telegram = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Telegram')
    telegram_name = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Telegram Name')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.location


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='blog', blank=True, verbose_name='Image')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Title')
    body = models.TextField(max_length=5000, verbose_name='Body')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        imageoutput = Image.open(self.image)
        output = BytesIO()
        imageoutput.save(output, optimize=True, format='JPEG', quality=55)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField',
                                          "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Blog, self).save(*args, **kwargs)


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=20, db_index=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=25, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:works_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super(Category, self).save(*args, **kwargs)


class Works(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='works/', verbose_name='Work Image')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Work Name')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')
    work_url = models.CharField(max_length=100, db_index=True, verbose_name='Work Url')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        imageoutput = Image.open(self.image)
        output = BytesIO()
        imageoutput.save(output, optimize=True, format='JPEG', quality=55)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField',
                                          "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Works, self).save(*args, **kwargs)


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    option_1 = models.CharField(max_length=30, db_index=True, verbose_name='')
    option_2 = models.CharField(max_length=30, db_index=True, verbose_name='')
    option_3 = models.CharField(max_length=30, db_index=True, verbose_name='')
    body = models.TextField(max_length=3000, verbose_name='Experience Body')

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self):
        return self.option_1


class Skills(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    skills = models.CharField(max_length=60, db_index=True, verbose_name='Skills')
    skill_level = models.CharField(max_length=3, db_index=True, verbose_name='Level')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skills

    # def get_absolute_url(self):
    #     return reverse('skills', args=[str(self.id)])


class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    year = models.CharField(max_length=16, db_index=True, verbose_name='Education Year')
    schooll = models.CharField(max_length=50, db_index=True, verbose_name='School/University')
    location = models.CharField(max_length=30, db_index=True, verbose_name='Education Location')
    body = models.TextField(max_length=1000, verbose_name='Specialty')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.year


class WorkExprerience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    year = models.CharField(max_length=25, db_index=True, verbose_name='Exprerience Year')
    specialty = models.CharField(max_length=50, db_index=True, verbose_name='Specialty')
    location = models.CharField(max_length=50, db_index=True, verbose_name='Exprerience Location')
    body = models.TextField(max_length=1000, verbose_name='Job Description')

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experience'

    def __str__(self):
        return self.specialty

