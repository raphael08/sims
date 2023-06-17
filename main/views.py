from django.shortcuts import render
from django.views.decorators.csrf import *
# Create your views here.
from django.http import JsonResponse
from .models import *

def sensordata_table(request):
 try:
    last_data = Sensordata.objects.last()
    
    #converting each last_data attribute into integer so that it works in our math comparison in our template

    humidity = float(last_data.humidity_val)
    moisture = float(last_data.moisture_val)
    Temp = float(last_data.temperature_val)
    waterLevel = float(last_data.waterLevel_val)

    context = {'last_data': last_data, 'humidity': humidity, 'moisture': moisture, 'temperature': Temp, 'waterLevel': waterLevel}
    return render(request, 'sensordata_table.html', context)
 except:
     return render(request, 'sensordata_table.html')
    

@csrf_exempt  
def postData(request,moisture,level,temperature,humidity):
    
    try:
   
    #  datas = Sensordata.objects.create(humidity_val=humidity,temperature_val=temperature,moisture_val=moisture,waterLevel_val=level)
    #  if datas:
     status = 'true'

     return JsonResponse({'status':humidity})
    except:
      return JsonResponse({'status':'false'})  