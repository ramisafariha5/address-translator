from googletrans import Translator
import time
from city import city
import csv
from dhaka import dhaka

level_0_bn = ""
level_1_bn = ""
level_2_bn = ""

def translate_to_bn(text):
    translator = Translator(service_urls=[
      'translate.google.co.kr',
    ])

    translated = translator.translate(text, src='en', dest='bn').text
    
    # print(translated)
    return translated

def dumpcsv():
    with open('Dhakabn.csv', 'a') as csvfile: 
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
        
        rows= ["level_0","level_0_bn","level_1","level_1_bn","level_2","level_2_bn","level_3","level_3_bn","level_4","level_4_bn","level_5","level_5_bn"]
    # writing the data rows 
        csvwriter.writerow(rows)
def dump(data):
    with open('Dhakabn.csv','a') as csvfile:
         csvwriter = csv.writer(csvfile)

         rows = [data['level_0'],data['level_0_bn'],data['level_1'],data['level_1_bn'],data['level_2'],data['level_2_bn'],data['level_3'],data['level_3_bn'],data['level_4'],data['level_4_bn'],data['level_5'],data['level_5_bn']]
         print(rows) 
         csvwriter.writerow(rows)  
def execute():
    dumpcsv()
    level_0_bn = translate_to_bn(dhaka[0]['level_0'])
    level_1_bn = "ঢাকা"
    level_2_bn = "ঢাকা"
    for i in range(0,10):
        level_3_bn = translate_to_bn(dhaka[i]['level_3'])
        level_4_bn = translate_to_bn(dhaka[i]['level_4'])
        level_5_bn = translate_to_bn(dhaka[i]['level_5'])
        dhaka[i]['level_0_bn'] = level_0_bn
        dhaka[i]['level_1_bn'] = level_1_bn
        dhaka[i]['level_2_bn'] = level_2_bn
        dhaka[i]['level_3_bn'] = level_3_bn
        dhaka[i]['level_4_bn'] = level_4_bn
        dhaka[i]['level_5_bn'] = level_5_bn
        print(dhaka[i])
        data = dhaka[i]
        dump(data)
        

    
execute()

#print(translate_to_bn(dhaka[0]['level_1']))