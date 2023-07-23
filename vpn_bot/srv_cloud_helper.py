'''async function for requests to nginx'''
import aiohttp

SRV_CLOUD = 'http://nginx'

async def add_user(tg_id, first_name, last_name, username):
    '''Add user
       INPUT:
        id - id user in telegram messenger
        first_name - first name
        last_name - last name
        username - link user in telegram messenger
       OUTPUT:
        True - if this user not in BD
        False - if this user in BD
    '''
    data = {
        'tg_id': tg_id,
        'first_name': first_name,
        'last_name': last_name,
        'username': username
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{SRV_CLOUD}/api/v1/users/", data=data) as response:
            users = await response.json(content_type='application/json')
            if users.get('status') == 'ok':
                return True
    return False
