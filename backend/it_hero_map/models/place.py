from it_hero_map.models import BaseModel
from sqlalchemy import Column, UUID, VARCHAR, TIMESTAMP, func
import uuid


class PlacesModel(BaseModel):
    __tablename__ = "places"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(128), unique=False, nullable=False)
    description = Column(VARCHAR(2048), unique=False, nullable=False)
    image_path = Column(VARCHAR(128), unique=False, nullable=False)
    coords = Column()
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), server_onupdate=func.current_timestamp(), nullable=False)
