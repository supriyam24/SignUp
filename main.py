from fastapi import FastAPI
from pydantic import BaseModel
# from dotenv import load_dotenv
import json
import os

# load_dotenv() # take environment variables from .env.
# pwd = os.getenv("PWD")
class User(BaseModel):
    email : str
    password : str
    age : int | None = None

app = FastAPI()

@app.get('/')
async def index():
    return "hey, welcome!"

# @app.get('/blog/{id}/comments')
# async def comments(id: int):  # path parameter with Type --> int
#     return {'data' : {'1','2'}}

@app.post('/signup')
async def create_User(req:User):
    # print(type(req))
    f = open("users.json","r+") #open the file
    data = json.load(f) # Conversion from JSON to Python OBJ
    # modReq = json.loads(req)
    data["users"].append(req)
    f.seek(0)
    d = json.dump(data,f,default=vars,indent=4) # when default=vars not specified --> TypeError: Object of type Person is not JSON serializable   
                                                # Dump a Python dict to Valid JSON   
    # f.truncate()
    # f.write(d)
    f.close()

    return {f"user of type {type(req)} created"}
    

