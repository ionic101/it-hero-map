from fastapi import APIRouter
from typing import List
from it_hero_map.routers.places import place_router


routers: List[APIRouter] = [
    place_router
]

__all__ = [
    'routers'
]
