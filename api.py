from __future__ import print_function
import infermedica_api 

infermedica_api.configure(app_id='eb4835a9', app_key='679dd699e25f6bee7fe14cc3dc4d2b99')

api = infermedica_api.get_api()

def get_diagnosis(age, sex):
    '''
    this function gets the symptoms from the user and adds them to search in infermedica
    '''
    request = infermedica_api.Diagnosis(sex=sex, age=age)
    flag = True
    print ('Please enter the various symptoms you have line by line.')
    print ('Press enter once more when you are done entering all of your symptoms.')
    print ('The more symptoms you enter the more accurate our diagnosis would be.')
    while (flag):
        symptom=raw_input('')
        if(symptom==""):
            flag = False
            break
        dic = api.search(symptom)
        try: 
            SID = dic[0]['id'] 
            request.add_symptom(SID, 'present')
        except: 
            print("")
    request = api.diagnosis(request)
    return request.conditions[0]['name'], request.conditions[0]['probability']


        


# print('Welcome to the interactive nurse!')
# age = raw_input('What is your age?\n')
# sex = raw_input('What is your sex?\n')
# request = infermedica_api.Diagnosis(sex=sex, age=age)
# symptom='A'
# while(symptom!=""):
#     symptom=raw_input('What kind of symptoms are you having?\n')
#     #print (symptom)
#     if(symptom==""):
#         #print ('lol'+symptom)
#         break
#     #print (symptom)
#     dic = api.search(symptom)
#     SID = dic[0]['id'] 
#     request.add_symptom(SID, 'present')
# request = api.diagnosis(request)
# #print(request)
# print('There is a ' + str(request.conditions[0]['probability']*100) + '% ' +'chance that you have chance that you have ' + request.conditions[0]['name'] +'.\n')
