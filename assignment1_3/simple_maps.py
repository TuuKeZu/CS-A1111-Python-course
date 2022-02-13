#GLOBAL muuttujat

walking_speed = 5.5 #km/h
cycling_speed = 18 #km/h
waiting_time_for_lights = 30 #s

def CalcDistance(route_lenght, speed_limit, traffic_count, vehicle):
        #t = s/v, jossa aika t on tuntematon, metka (s) muuttuja, ja nopus (v) vakio.
        

        traffic_delay = traffic_count * 0.5 #mins
        time = 0 #mins

        if(vehicle == "WALKING"):
            #t = s/v
            time = (route_lenght/walking_speed) * 60 + traffic_delay

        if(vehicle == "BICYCLE"):
            time = (route_lenght/cycling_speed) * 60 + traffic_delay

        if(vehicle == "CAR"):
            time = (route_lenght/speed_limit) * 60 + traffic_delay

        return(time)

print("How long is the route (km)?")
ans1 = input();
print("Enter the speed limit (km/h):")
ans2 = input();
print("How many traffic lights are there on the road?")
ans3 = input();

print("Your traveling time will be:")
print(str(CalcDistance(float(ans1), int(ans2), int(ans3), "CAR")) + " minutes by car,")
print(str(CalcDistance(float(ans1), int(ans2), int(ans3), "BICYCLE")) + " minutes by bike,")
print(str(CalcDistance(float(ans1), int(ans2), int(ans3), "WALKING")) + " minutes on foot.")

    
