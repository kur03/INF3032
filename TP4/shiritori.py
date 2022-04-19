import json

def shiritori(message):

    if message != "**NEW ROUND**" : 
        with open('shiritori.json', 'r') as shiritori_json:
            shiritori_load = json.load(shiritori_json)
                    
        for msg in shiritori_load["shiritori"] :
            if message == msg :
                return True
            
        shiritori_load["shiritori"].append(message)
        with open('shiritori.json', 'w') as outfile:
            json.dump(shiritori_load, outfile)
            
    else :
        shiritori_load= {"shiritori": [""]}
        with open('shiritori.json', 'w') as outfile:
            json.dump(shiritori_load, outfile)
            
    return False
                