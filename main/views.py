
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API
  
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&APPID=26db2ff49e8a9ee59e2103c3db1fd63e').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        print("===============================================")
        print("===============================================")

        print(list_of_data)
         
        print("===============================================")
        print("===============================================")


        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "sea_level": str(list_of_data['main']['sea_level']),
            "name": str(list_of_data['name']),
        }
        print(data)
    else:
        data ={}
    return render(request, "main/index.html", data)