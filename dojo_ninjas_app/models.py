from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField(default = 'old dojo')
class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, on_delete = models.CASCADE, related_name = 'ninjas')
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length =255)


def display_dojos():
    return Dojo.objects.all()

def add_dojo(request):
    dojo = Dojo.objects.create(name = request.POST['dojo_name'], city = request.POST['city'], state = request.POST['state'])

def display_ninjas():
    return Ninja.objects.all()

def add_ninja(request):
    ninja = Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo_id = request.POST['ninja_dojo'])

def remove_dojo(post_data):
    Dojo.objects.get(id = post_data['remove_dojo']).delete()
    

