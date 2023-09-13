from fastapi import FastAPI

# creating fastapi instance
FastAPIExample = FastAPI()


# python decorator to create a http protocos
"""
- POST: to create data.
- GET: to read data.
- PUT: to update data.
- DELETE: to delete data.
"""
@FastAPIExample.get("/home")
async def root():
    return {"message": "This is first API Example Using FastAPI"}
  
  
# FASTAPI With path parameters
@FastAPIExample.get("/items/{itemId}")
async def return_items(itemId:int):
  return {"ITEM_ID": itemId}

# example
@FastAPIExample.get("/users/{userID}/{password}")
async def getUsers(userID:int, password:str):
  return {"USER_ID": userID, "Password": password}

# complex example
from enum import Enum
class brandName(str, Enum):
  Tata = "Nexon"
  Landrover = "Rangerover"
  Mahindra = "XUV700"


@FastAPIExample.get("/modelName/{brandName}")
async def getModel(brandName:brandName):
  if brandName == "Nexon":
    return {"Brand": brandName,"Message":f"{brandName.value} proud indian brand which is of Tata Group"}
  elif brandName.value == "Rangerover":
    return {"Brand": brandName,"Message":f"{brandName.value} also proud indian brand which is of Tata Group"}
  else:
    return {"Brand": brandName,"Message":f"{brandName.value} also proud indian brand which is of Mahindra and Mahindra Group"}
  
  
# fastapi with filepath
@FastAPIExample.get("/home/user/{fileName:path}")
async def getFilePath(fileName:str):
  return {"fileName":fileName}



# FASTAPI With query parameters

# finding the data existence
data = ["aaa","bbb","ccc","ddd","eee"]

@FastAPIExample.get("/finding/")

async def findingElement(ele:str):
  if ele in data:
    return {"Element":ele,"Message":f"{ele} is present in the database"}
  else:
    return {"Element":ele,"Message":f"{ele} not present in the database"}
    


# uvicorn main:FastAPIExample --reload