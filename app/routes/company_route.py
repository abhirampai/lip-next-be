from fastapi import APIRouter,Depends
from ..servies import company_service
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal

router = APIRouter()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/allcompany", response_description="Get All Company Details")
def get_all_companies(start:int = 0,end:int = 5,db: Session = Depends(get_db)):
    return company_service.get_all_companies(db,start,end)

@router.get("/companybyid", response_description="Get Company Details by Internship Id")
def get_company_by_id(id:int,db: Session = Depends(get_db)):
    return company_service.get_company_by_id(db,id)

@router.get("/companysearch",response_description="Search Company by occupation and/or keyword")
def get_company_by_occupation_or_keyword(oid:int=0,kid:int=0,db: Session = Depends(get_db)):
    return company_service.get_company_by_occupation_or_keyword(db,oid,kid)

@router.get("/categories",response_description="Get All Category Ids")
def get_all_category_ids(db: Session = Depends(get_db)):
    return company_service.get_all_category_ids(db)