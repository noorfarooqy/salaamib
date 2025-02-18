from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.account import Account
from app.core.security import get_password_hash

class UserCRUD:
    def get_by_cif(self, db: Session, cif_number: str) -> Optional[User]:
        return db.query(User).filter(User.cif_number == cif_number).first()
        
    def create(self, db: Session, *, obj_in) -> User:
        db_obj = User(
            cif_number=obj_in.cif_number,
            hashed_password=get_password_hash(obj_in.password),
            phone_number=obj_in.phone_number,
            email=obj_in.email,
            # Optional fields from CBS validation
            first_name=getattr(obj_in, 'first_name', None),
            last_name=getattr(obj_in, 'last_name', None),
            gender=getattr(obj_in, 'gender', None),
            title=getattr(obj_in, 'title', None),
            short_name=getattr(obj_in, 'short_name', None),
            address_line1=getattr(obj_in, 'address_line1', None),
            address_line2=getattr(obj_in, 'address_line2', None),
            address_line3=getattr(obj_in, 'address_line3', None),
            address_line4=getattr(obj_in, 'address_line4', None),
            address_country=getattr(obj_in, 'address_country', None),
            nationality=getattr(obj_in, 'nationality', None),
            unique_id_name=getattr(obj_in, 'unique_id_name', None),
            unique_id_value=getattr(obj_in, 'unique_id_value', None),
            customer_type=getattr(obj_in, 'customer_type', None),
            category=getattr(obj_in, 'category', None)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

class AccountCRUD:
    def create(self, db: Session, *, obj_in) -> Account:
        db_obj = Account(
            user_id=obj_in.user_id,
            account_number=obj_in.account_number,
            account_type=obj_in.account_type,
            currency=obj_in.currency,
            status=obj_in.status,
            balance=0  # Initial balance
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user = UserCRUD()
account = AccountCRUD() 