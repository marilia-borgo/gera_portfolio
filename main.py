from typing import Union
import uvicorn
import service


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/projetos/{username}")
async def read_item(username: str):
    projects = await service.get_projects_user(username)
    return {"item_id": projects}