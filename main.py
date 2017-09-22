from Vehicle import vehicle

print "Welcome to Car-Maister. "
print "Did you buy a new car or did you crash the old one?"
print "We're here to help you keep track of your vehicles!"
print ""

veh1 = vehicle(brand = "BMW ", model = "540", km_driven = "12456 km ", servis = "25.6.2017")
veh2 = vehicle(brand = "BMW", model = "750", km_driven = "80687 km", servis = "25.6.2017")
veh3 = vehicle(brand = "Porsche", model = "Macan", km_driven = "46077 km", servis = "21.4.2017")
veh4 = vehicle(brand = "Porsche", model = "Cayenne", km_driven = "88754 km", servis = "21.4.2017")
veh5 = vehicle(brand = "Ford", model = "Transit", km_driven = "164987 km", servis = "15.3.2017")
veh6 = vehicle(brand = "Ford", model = "Transit", km_driven = "287512 km", servis = "15.3.2017")
veh7 = vehicle(brand = "Ford", model = "Transit", km_driven = "453242 km", servis = "8.2.2017")
veh8 = vehicle(brand = "Mercedes", model = "Sprinter", km_driven = "127553", servis = "16.8.2017")
veh9 = vehicle(brand = "Mercedes", model = "Sprinter", km_driven = "145653", servis = "16.8.2017")

vehicle_list = [veh1, veh2, veh3, veh4, veh5, veh6, veh7, veh8, veh9]

while True:
    print ""
    print "Choose on of these options:"
    print "(a) See all your vehicles"
    print "(b) Add vehicle"
    print "(c) Delete vehicle"
    print "(d) Edit vehicle"

    selector = raw_input("Enter a number before the description: ")

    if selector == "a":
        print print_full_list(vehicle_list)
    elif selector == "b":
        print ""

    #for p in vehicle_list:
       # print p.print_full_list()