import urllib
import urllib2
import json
import infermedica_api 
from api import get_diagnosis
from betterdoctor import get_doctor


def get_location():
    """
    gets users longitude and latitude based on their IP address
    """

    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    return location['latitude'], location['longitude']



# step 1: get user input (personal details, symptoms)
print "Welcome, thank you for using Dr AI. Please be patient with us as we"
print "try to diagnose you, we are still in our beta."
name = raw_input("What do I address you by?\n")
sex = raw_input("Hi "+name+", what is your gender?\n")
age = raw_input("Hi "+name+", how old are you?\n")

# step 2: use symptoms to find diagnosis
diagnosis, probability = get_diagnosis(age, sex)

# step 3: use diagnosis & % to decide on doctor/pharmacy
print('There is a ' + str(probability*100) + '% ' +'chance that you have chance that you have ' + diagnosis +'.\n')

# step 4: run doctor or pharmacy if necessary
if probability < 0.5:
    latitude, longitude = get_location()
    doctors = get_doctor(longitude = longitude, latitude = latitude, diagnosis = diagnosis)
    print ("From our initial analysis, we recommend the following doctors")
    try:    
        for doctor in doctors:
            print "You can visit "+doctor[0]+" at "+doctor[1]
            print "You can reach him/her at "+doctor[2]
    except:
        print "There are no doctors in this area for your illness. Please call the CDC."

# step 5: print diagnosis report

