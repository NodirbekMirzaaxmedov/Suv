from fastapi import APIRouter,FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from models.transfers import Transfers
from schemas.transfers_schemas import CreateTransfer,UpdateTransfer
from utils.auth import get_current_user
from db import database
from functions.transfers_func import all_transfers,create_transfers_y, delete_transfers_r,update_transfers_y
from schemas.users_schemas import CreateUser
from utils.role_checker import *
from utils.db_operations import get_in_db
transfers_router = APIRouter(
    prefix="/transfers",
    tags=["Transfers Opeations"]
)

@transfers_router.get("/get_transfers")
def get_transfers(search:str = None,page:int = 0,limit: int = 25, db:Session = Depends(database),
                  current_user:CreateUser = Depends(get_current_user),id:int=0,branch_id: int = 0):
    role_verification(user=current_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    if id > 0:
        return get_in_db(db, Transfers, id)
    return all_transfers(search, page, limit, db)
@transfers_router.post("/create_transfers")
def create_transfers(new_transfer: CreateTransfer,db: Session = Depends(database), current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    create_transfers_y(new_transfer,db,current_user)
    raise HTTPException(status_code=200,detail="Amaliyot muvaffaqiyatli yakunlandi")

@transfers_router.put("/update_transfers")
def update_transfers(this_transfer: UpdateTransfer,db: Session = Depends(database),current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    update_transfers_y(this_transfer,db,current_user)
    raise HTTPException(status_code=200,detail="Amaliyot muvaffaqiyatli yakunlandi")

@transfers_router.delete("/delete_transfers")
def delete_transfers(id: int, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    delete_transfers_r(id, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
