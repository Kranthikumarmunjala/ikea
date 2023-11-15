from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Furniture,Details

# Create your views here.

@api_view(['GET'])
def furnitures(request):
    all_furnitures=Furniture.objects.all()
    output=[

    ]
    for temp_furniture in all_furnitures:
        temp_dict={
            'furniture_id':temp_furniture.id,
            'furniture_name':temp_furniture.name,
            'furniture_price':temp_furniture.price,
            'furnitur_color':temp_furniture.color,
            'furniture_brand':temp_furniture.brand,
            'furniture_quantity':temp_furniture.quantity
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def furniture(request):
    furniture_id=request.GET.get('furniture_id',None)
    if furniture_id is None:
        return Response({'message':'invalid furniture id'})
    else:
        try:
            furniture_info=Furniture.objects.get(id=furniture_id)
            furniture_dict={
                'furniture_id':furniture_info.id,
                'furniture_name':furniture_info.name,
                'furniture_price':furniture_info.price,
                'furniture_brand':furniture_info.brand,
                'furniture_color':furniture_info.color,
                'furniture_quantity':furniture_info.quantity
            }
            return Response(furniture_dict)
        except Furniture.DoesNotExist:
            return Response({'message':'invalid furniture_id'})

@api_view(['POST'])
def add_details(request):
    name=request.POST.get('name',None)
    discription=request.POST.get('discription',None)
    if name is None or discription is None:
        return Response({'message':'send name and discription'})
    else:
        new_details=Details.objects.create(
            name=name,
            description=description
        )
        new_details.save()
        return Response({'name':name,'description':description})


