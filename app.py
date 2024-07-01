import requests
import json


#f_input = open('coordenadas.txt', 'r')
#line_in = f_input.readline()
#coor_in = line_in.split(' ')

ff = open('data2.txt','a')


with open('coordenadas2.txt', 'r') as f_input:
    line = f_input.readline()
    while line:
        # -- read line
        line_in = line.strip()

        # -- read coordenates
        coordenates = line_in.split()
        #print(coordenates)

        # -- replace coordinates in url
        #url = 'https://atlas.microsoft.com/route/directions/json?api-version=1.0&query={},{}:{},{}'.format(coordenates[0], coordenates[1], coordenates[2], coordenates[3])
        url = 'https://atlas.microsoft.com/route/directions/json?api-version=1.0&query={},{}:{},{}'.format(coordenates[1], coordenates[0], coordenates[3], coordenates[2])
        #print(url)
        key = ""
        url = url + '&report=effectiveSettings&traffic=true&travelMode=car&subscription-key=' + key

        # -- get query
        response = requests.get(url)
        #print(response.text)

        # -- parse json objec
        data = json.loads(response.text)

        # -- get variables
        #query_coodinates_no_stadarized = data['report']['effectiveSettings'][7]['value']
        lengthInMeters = data['routes'][0]['summary']['lengthInMeters']
        travelTimeInSeconds = data['routes'][0]['summary']['travelTimeInSeconds']
        trafficDelayInSeconds = data['routes'][0]['summary']['trafficDelayInSeconds']
        trafficLengthInMeters = data['routes'][0]['summary']['trafficLengthInMeters']
        #print("query_coodinates_no_stadarized: ",query_coodinates_no_stadarized)
        print("lengthInMeters: ", lengthInMeters)
        print("travelTimeInSeconds: ",travelTimeInSeconds)
        print("trafficDelayInSeconds: ",trafficDelayInSeconds)
        print("trafficLengthInMeters: ",trafficLengthInMeters)


        # -- get  positions of the first and second standarized coordinates
        first_coordinate_index = int(data['routes'][0]['sections'][0]['startPointIndex'])
        last_coordinate_index = int(data['routes'][0]['sections'][0]['endPointIndex'])

        # -- get coordinates
        first_coodinate_lat = data['routes'][0]['legs'][0]['points'][first_coordinate_index]['latitude']
        first_coodinate_lon = data['routes'][0]['legs'][0]['points'][first_coordinate_index]['longitude']

        last_coodinate_lat = data['routes'][0]['legs'][0]['points'][last_coordinate_index]['latitude']
        last_coodinate_lon = data['routes'][0]['legs'][0]['points'][last_coordinate_index]['longitude']

        # -- prints standarized coordinates
        print("primera coor: ",first_coodinate_lat, ":", first_coodinate_lon)
        print("segunda coor: ",last_coodinate_lat, ":", last_coodinate_lon)

        # -- make string for the output file
        line_v = "{}:{} {}:{} {} {} {} {}\n".format(first_coodinate_lat, first_coodinate_lon, last_coodinate_lat, last_coodinate_lon, lengthInMeters, travelTimeInSeconds, trafficDelayInSeconds, trafficLengthInMeters)

        # -- write in the output file
        ff.writelines(line_v)


        # -- read next line (in the while)
        line = f_input.readline()



ff.close()

