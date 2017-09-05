import requests
import json
import pprint
def get_doctor(longitude, latitude, diagnosis):
    url = 'https://api.betterdoctor.com/2016-03-01/'
    function = 'doctors'
    params = dict (
        user_location = str(latitude)+','+str(longitude),
        sort = 'distance-asc',
        query = diagnosis,
        skip = '0',
        limit = '10',
        user_key = 'd43951330ee8fdbf751b4abb864a9ed8'
    )
    url = url + function
#url = 'https://api.betterdoctor.com/2016-03-01/doctors?location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&gender=male&skip=0&limit=10&user_key=d43951330ee8fdbf751b4abb864a9ed8'
#r = requests.get('https://api.betterdoctor.com/2016-03-01/doctors?first_name=hahahaha&limit=10&location=37.773%2C-122.413%2C100&gender=male&user_key=d43951330ee8fdbf751b4abb864a9ed8&user_location=37.773%2C-122.413&skip=0')
#r = requests.get('https://api.betterdoctor.com/2016-03-01/doctors?first_name=hahahaha&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&gender=male&skip=0&limit=10&user_key=d43951330ee8fdbf751b4abb864a9ed8')

#r = requests.get(url)
#print r.text
#print data['meta']

#user_loc = input("Enter your location:")

    r = requests.get(url=url, params=params)
    data = json.loads(r.text)
#print(params['user_location'])
    #pp = pprint.PrettyPrinter(indent=4)
    doctor_list = []
    for i in range(5):
        full_name = data['data'][i]['profile']['first_name'] + " " + data['data'][i]['profile']['last_name']
        address = data['data'][i]['practices'][0]['visit_address']['street'] + " " + data['data'][i]['practices'][0]['visit_address']['city']
        address += data['data'][i]['practices'][0]['visit_address']['state'] + " " + str(data['data'][i]['practices'][0]['visit_address']['zip'])
        number = data['data'][i]['practices'][0]['phones'][0]['number']
        doctor_list.append((full_name, address, number))
    return doctor_list


if __name__ == '__main__':
    get_doctor(123,12321, 'headache')