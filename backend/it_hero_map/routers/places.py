from fastapi import APIRouter


place_router: APIRouter = APIRouter(prefix='/place')


@place_router.get('/')
async def get_places():
    return 'places'


@place_router.post('/')
async def create_place():
    return 'places'


@place_router.delete('/')
async def delete_place():
    return 'places'


@place_router.put('/')
async def update_place():
    return 'places'
