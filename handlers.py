from pysimplebase import SimpleBase
import json
from pathlib import Path

from ru.travelfood.simple_ui import SimpleUtilites as suClass
import time
import os


def init(hashMap,_files=None,_data=None):
    
    
    hashMap.put("StackAddMode","")
    

    return hashMap

def test(hashMap,_files=None,_data=None):
    

    hashMap.put("beep","10")
    
    db = SimpleBase("testdb3",path=suClass.get_simplebase_dir(),timeout=200)
    
    res = db['test_3'].insert({"nom":"миксер"}, upsert =True,no_index=True)
    hashMap.put("toast",str(res))

    set=[]
    for i in range(10):
        set.append({"nom":"Грабли -"+str(i)})

    inserted = db['test_3'].insert(set,upsert=True)
    hashMap.put("toast","вставили 3 грабли")

    res = db['test_3'].insert({"nom":"миксер-2"}, upsert =True)
    hashMap.put("toast","Вставили миксер")
    

    #db['test_d'].insert({"nom":"комбайн","_id":"d552a1b0-7ec0-48a5-9b39-3cf6d19d5c7f"}, upsert =True, fast=True)

    return hashMap        


def read_file(hashMap,imageBytes):
        from ru.travelfood.simple_ui import SimpleUtilites as suClass
        filename = suClass.get_temp_dir()+os.sep+"test_file.FILE"
        hashMap.put("toast",filename)
        hashMap.put("beep","")
        with open(filename, 'wb') as f: 
            f.write(imageBytes)

        suClass.download_file(filename)

        hashMap.put("filename",filename)

        return hashMap

def file_download(hashMap,_files=None,_data=None):
    
    filename = "/data/data/ru.travelfood.simple_ui/app_files/SimpleUI images/testdb/testdb2/test_2.db"
    hashMap.put("toast",filename)
    suClass.download_file(filename)

    return hashMap 

def run_nosql(hashMap,_files=None,_data=None):
    
    hashMap.put("RunSimpleBase",json.dumps([{"database":"dbnative","collection":"test_1","command":"insert","value":{"caption":"Hello world"}}]))

    return hashMap 

def set_visionsettings(hashMap,_files=None,_data=None):
    
    values_list = "123;532;345;111"

    hashMap.put("SetVisionSettings",json.dumps({"values_list":values_list,"min_length":3,"max_length":5,"ReplaceO":True,"ToUpcase":True}))

    hashMap.put("green_list",values_list)

    return hashMap 

def nosql_on_start(hashMap,_files=None,_data=None):
    

    
    dbpath = suClass.get_temp_dir()

    db = SimpleBase("dbnative",path=dbpath,timeout=200)
    
    res = db['test_1'].all()

    j = {
"type": "table",

"columns": [
  {
    "name": "id",
    "header": "id",
    "weight": "2"
  },
  {
    "name": "txt",
    "header": "txt",
    "weight": "2"
  },
  {
    "name": "qty",
    "header": "qty",
    "weight": "1"
  }
],
"rows": []
}

    for item in res:
        j['rows'].append({"id":item["_id"],"txt":item.get("txt"),"qty":item.get("count")})

    hashMap.put("table",json.dumps(j,ensure_ascii=False))

    return hashMap  


def open_dialog(hashMap,_files=None,_data=None):
    

    layout = {
            "Value": "",
            "Variable": "",
            "type": "LinearLayout",
            "weight": "0",
            "height": "match_parent",
            "width": "match_parent",
            "orientation": "vertical",
            "Elements": [
                {
                    "type": "TextView",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "Имя",
                    "Variable": ""
                },
                {
                    "type": "EditTextText",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "",
                    "Variable": "name"
                },
                {
                    "type": "TextView",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "Должность",
                    "Variable": ""
                },
                {
                    "type": "EditTextText",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "",
                    "Variable": "position"
                }
            ],
            "BackgroundColor": "",
            "StrokeWidth": "",
            "Padding": ""
        }
    

    hashMap.put("ShowDialogLayout",json.dumps(layout,ensure_ascii=False))
    hashMap.put("ShowDialog","")

    return hashMap

def long_handler(hashMap,_files=None,_data=None):
    
    import time
    time.sleep(5)

    hashMap.put("speak","Закончился обработчик")
    hashMap.put("toast","Закончился обработчик")
    hashMap.put("b","100")
    hashMap.put("RefreshScreen","")
    

    return hashMap


def run_timer(hashMap,_files=None,_data=None):
    
    timer_handlers = [{"action": "run","type": "python","method": "long_handler", "postExecute": ""}]

    hashMap.put("StartTimer",json.dumps({"handler":timer_handlers,"period":5000}))
    

    return hashMap

def vs_init(hashMap,_files=None,_data=None):
    
    

    hashMap.put("SetVisionSettings",json.dumps({"min_length":3,"max_length":5,"ReplaceO":True,"ToUpcase":True,"OnlyNumbers":True}))
    hashMap.put("UseVisionSettings","")

    hashMap.put("object_detector_mode",json.dumps([]))
    hashMap.put("CVDetectors","ocr")
    

    return hashMap 

def multiscanner_object(hashMap,_files=None,_data=None):

    if hashMap.containsKey("object_caption_list"):
        jobject_caption_list = json.loads(hashMap.get("object_caption_list"))
    else:
        jobject_caption_list = []  


    result = json.loads(hashMap.get("current_object"))
    
    if hashMap.containsKey("object_detector_mode"):
     detectors_mode=json.loads(hashMap.get("object_detector_mode"))
    else:   
     detectors_mode=[]

    if hashMap.containsKey("green_list"):
        green_list = str(hashMap.get("green_list")).split(";")
    else:
        green_list = []   

    

    modeitem = next((item for item in detectors_mode if item["object_id"] == result['object_id']), None)

    if modeitem!=None:
     if modeitem['mode']=='stop':   
      return hashMap
        
    detectors_mode.append({"object_id":result['object_id'],"mode":"stop"})
    

    green_list.append(str(result['object_id']))    

    hashMap.put("green_list",";".join(green_list))

  
    hashMap.put("object_detector_mode",json.dumps(detectors_mode))

    
    

    jobject_caption_list.append({"object":str(result['object_id']),"caption":" ID=<b>"+str(result['object_id'])+"</b> , <b> Цена: "+str(result["value"])+"</b>"} )
    hashMap.put("object_caption_list",json.dumps(jobject_caption_list,ensure_ascii=False))

    hashMap.put("beep","10")
    

    return hashMap 

def before_html(hashMap,_files=None,_data=None):
    
    html = """
<!DOCTYPE html>
<html>
 <head>
  <title>Все заголовки — schoolsw3.com</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
 </head>
 <body>
 
  <h1>HTML5 Все заголовки</h1>
  
  <h1>Заголовок 1</h1>
  <h2>Заголовок 2</h2>
  <h3>Заголовок 3</h3>
  <h4>Заголовок 4</h4>
  <h5>Заголовок 5</h5>
  <h6>Заголовок 6</h6>

 </body>
</html>
"""
    

    #hashMap.put("RunEvent",json.dumps([{"action": "runasync","type": "html2image","method": html, "postExecute": json.dumps([{"action": "run","type": "python","method": "html2image_after"}])  }]))

    hashMap.put("RunEvent",json.dumps([{"action": "runprogress","type": "html2image","method": html, "postExecute": json.dumps([{"action": "run","type": "python","method": "html2image_after"}])  }]))

    #Можно выводить в файл PNG
    #filename = suClass.get_temp_file("png")
    #hashMap.put("html2image_ToFile",filename)
    

    return hashMap 


def html2image_after(hashMap,_files=None,_data=None):
    hashMap.put("picture",hashMap.get("html2imageResult"))
    hashMap.put("RefreshScreen","")
    

    return hashMap 


def test_speak(hashMap,_files=None,_data=None):
    from ru.travelfood.simple_ui import MainActivity as MainActivity
    
    MainActivity.tts.speak("абырвалг", 1, None)

    return hashMap 
