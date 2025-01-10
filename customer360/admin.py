from django.contrib import admin
from .models import Customer, Interaction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'social_media')  
    search_fields = ('name', 'email', 'phone') 
    list_filter = ('social_media',)  

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'channel', 'direction', 'interaction_date', 'summary') 
    search_fields = ('customer__name', 'summary') 
    list_filter = ('channel', 'direction', 'interaction_date') 
