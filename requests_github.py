import httpx


async def get_repositorios_user(username):
     async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'https://api.github.com/users/{username}/repos')
            return response.json()
        except:
            return 'ja eras'