from fastapi import APIRouter

router = APIRouter


@router.get("/")
def get_terms():
    return 'Hello World!'
