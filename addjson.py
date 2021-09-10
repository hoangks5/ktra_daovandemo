import json
import readfile

information = readfile.__readfile__('Commodore.txt')
__add__ = {
    "intents": [
        {
            "title": "Commodore",
            "text": [
                information
            ]
        }
    ]



}


with open('main.json','w',encoding='utf-8') as fp: # Thêm dữ liệu vào tệp JSON
    json.dump(__add__, fp, indent=2,)