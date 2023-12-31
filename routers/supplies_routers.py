from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from db import database
from schemas.users_schemas import CreateUser
from utils.auth import get_current_user
from utils.db_operations import get_in_db, get_with_branch
from utils.role_checker import *
from functions.supplies_func import all_supplies_r,create_supplies_r, delete_supplies_r,update_supplies_r
from schemas.supplies_schemas import CreateSupplies,UpdateSupplies
from models.supplies import Supplies

supplies_router = APIRouter(
    prefix="/supplies",
    tags=["Supplies Operations"]
)

@supplies_router.get("/get_supplies")
def all_supplies(search: str = None, limit: int = 25, page: int = 0,db: Session = Depends(database),
                  current_user:CreateUser = Depends(get_current_user),id: int = 0,branch_id: int = 0):
    role_verification(user=current_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    if id > 0:
        return get_in_db(db, Supplies, id)
    # if branch_id > 0:
    #     return get_with_branch(db,Supplies,branch_id)
    return all_supplies_r(search,limit,page,db,branch_id)
@supplies_router.post("/create_supplies")
def create_supplies(new_supplie: CreateSupplies,db: Session = Depends(database),current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    create_supplies_r(new_supplie,db,current_user)
    
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

@supplies_router.put("/update_supplies")
def update_suppplies(this_supplies: UpdateSupplies,db: Session = Depends(database),current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    update_supplies_r(this_supplies,db,current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

@supplies_router.delete("/delete_supplies")
def delete_supplies(id: int, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    delete_supplies_r(id, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
