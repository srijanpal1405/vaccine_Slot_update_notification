from cowin_api import CoWinAPI
from pprint import pprint
import pywhatkit
import time
from playsound import playsound



cowin = CoWinAPI()
states = cowin.get_states()
# print("All States List : ")
# for i in range(len(states['states'])):
#     print(states['states'][i])
#
# state_id = input("Enter State ID: ")
# districts = cowin.get_districts(state_id)
#
# print("Districts by State Id : ")
# pprint(districts)

pin_code = '713104'
date = '18-07-2022'
k = 0
playsound('txttosp1.mp3')
last = 3
while k != 1:
    print("Running...")
    available_centers = cowin.get_availability_by_pincode(pin_code, date)



    for i in range(len(available_centers['centers'])):
        if available_centers['centers'][i]['name'] == 'BMC LT3. 3':
            if available_centers['centers'][i]['sessions'][0]['available_capacity_dose2'] > last:

                print(available_centers['centers'][i]['sessions'][0]['available_capacity_dose2'])
                pywhatkit.sendwhatmsg("+917001869561", "check cowin", int(time.strftime("%H", time.localtime())),
                                      int(time.strftime("%M", time.localtime())) + 1, 7, False)
                while(1):
                    playsound('E:/python/vaccine_Tracker/txttosp.mp3')
                    k = 1

            else:
                last = available_centers['centers'][i]['sessions'][0]['available_capacity_dose2']
                print(last)