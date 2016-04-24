from random import randint

from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Count

from .models import Tag, Restaurant, Menu

# Create your views here.

class FoodTagView(APIView):

	def get(self, request):
		if request.GET.get('random'):
			selected_tags = request.GET.get('selected_tags')
			selected_tags = selected_tags.split(',')
			while True:
				restaurants = Restaurant.objects.filter(tags__id=selected_tags[0])
				all_style_tags = Tag.objects.filter(tag_type='style')
				random_style = all_style_tags[randint(0,len(all_style_tags)-1)]
				restaurants = restaurants.filter(tags=random_style)
				print random_style
				if restaurants:
					randomed_restaurant = restaurants[randint(0,len(restaurants)-1)]
					menus = Menu.objects.filter(restaurant=randomed_restaurant)
					randomed_menu = menus[randint(0,len(menus)-1)]
					data = {
						'text': randomed_menu.name,
						'price': randomed_menu.price
					}
					break

		else:
			step = request.GET.get('step')
			if step == '1':
				tags = Tag.objects.filter(tag_type='location')
				data = []
				for tag in tags:
					data.append({
						'id': tag.id,
						'text': tag.name
					})
			elif step == '2':
				tags = Tag.objects.filter(tag_type='style')
				data = []
				for tag in tags:
					data.append({
						'id': tag.id,
						'text': tag.name
					})
			elif step == '3':
				selected_tags = request.GET.get('selected_tags')
				selected_tags = selected_tags.split(',')
				restaurants = Restaurant.objects.filter(tags__id=selected_tags[0])
				restaurants = restaurants.filter(tags__id=selected_tags[1])
				randomed_restaurant = restaurants[randint(0,len(restaurants)-1)]
				menus = Menu.objects.filter(restaurant=randomed_restaurant)
				randomed_menu = menus[randint(0,len(menus)-1)]
				data = {
					'text': randomed_menu.name,
					'price': randomed_menu.price
				}
		
		return Response(data)