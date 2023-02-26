import json
with open('./usb.json','r') as f:
    ini_string = f.read()

final_dict = json.loads(ini_string)
keystroke = []
for i in final_dict:
    keystroke.append(''.join(i['_source']['layers']['usbhid.data'].split(":")))


with open('./keystroke.txt','w') as fw:
    for i in keystroke:
        fw.write(i + "\n")
