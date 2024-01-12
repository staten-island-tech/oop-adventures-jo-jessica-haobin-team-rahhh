import json


weapons = {{


}
{


}
{

    
}}



json_object = json.dumps(weapons, indent=4)

with open("data.json", "w") as f:
    f.write(json_object)