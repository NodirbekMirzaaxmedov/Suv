from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.products import Products
from utils.auth import get_current_user
from schemas.users_schemas import CreateUser
from utils.db_operations import get_in_db
from db import database
from utils.role_checker import *
from functions.user_products_func import all_user_products,create_user_products_y, delete_user_products_r,update_user_products_y
from models.user_products import User_products
from schemas.user_products_schemas import UpdateUserProduct,CreateUserProduct

user_products_router = APIRouter(
    prefix="/user_products",
    tags=["User Products operation"]
)


@user_products_router.get("/get_user_products")
def get_products(search: str = None, id: int = 0, page: int = 0, limit: int = 25,db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_user),branch_id: int = 0):
    role_verification(user=current_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    if id > 0:
        return get_in_db(db, User_products, id)
    return all_user_products(search, page, limit, db,branch_id)



@user_products_router.post("/create_user_products")
def create_products(new_user_products: CreateUserProduct, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    create_user_products_y(new_user_products, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@user_products_router.put("/update_user_products")
def update_products(this_user_products: UpdateUserProduct, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    update_user_products_y(this_user_products, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

@user_products_router.delete("/delete_user_products")
def delete_user_products(id: int, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    role_verification(user=current_user)
    delete_user_products_r(id, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

