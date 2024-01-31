import requests_github

async def get_projects_user(username):
    repositorio = await requests_github.get_repositorios_user(username)
    return repositorio
    