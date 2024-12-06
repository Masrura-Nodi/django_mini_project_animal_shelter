from django.shortcuts import render
from .models import Animals

# Create your views here.


def index(request):
    pet1 = Animals()
    pet1.name = "Golu"
    pet1.desc = "The cat that bites me"
    pet1.img = "destination_1.jpg"
    pet1.price = 700
    pet1.offer = True

    pet2 = Animals()
    pet2.name = "Zack"
    pet2.desc = "The Goat that bites me"
    pet2.img = "destination_2.jpg"
    pet2.price = 750
    pet2.offer = False

    pet3 = Animals()
    pet3.name = "Snuggie"
    pet3.desc = "The Panther that bites me"
    pet3.img = "destination_3.jpg"
    pet3.price = 600
    pet3.offer = not True


    pet4 = Animals()
    pet4.name = "Golu2"
    pet4.desc = "The cat that bites me"
    pet4.img = "destination_4.jpg"
    pet4.price = 700
    pet4.offer = not True

    pet5 = Animals()
    pet5.name = "Zack2"
    pet5.desc = "The Goat that bites me"
    pet5.img = "destination_5.jpg"
    pet5.price = 750
    pet5.offer = not True

    pet6 = Animals()
    pet6.name = "Snuggie2"
    pet6.desc = "The Panther that bites me"
    pet6.img = "destination_6.jpg"
    pet6.price = 600
    pet6.offer = not True
    

    pets = [pet1, pet2, pet3, pet4, pet5, pet6]
    
    return render(request, "index.html", {"pets" : pets})