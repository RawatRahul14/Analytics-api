from fastapi import APIRouter
from .schema import EventSchema

router = APIRouter()

@router.get("/")
def read_events():
    # Bunch of items in  a table
    return {
        "items": [1, 2, 3]
    }

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # A single row
    return {"id": event_id}