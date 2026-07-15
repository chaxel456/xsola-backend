from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.customers.repository import CustomerRepository


class CustomerService:

    def __init__(self):
        self.repo = CustomerRepository()

    def create_customer(self, db: Session, payload):
        return self.repo.create(
            db,
            payload.model_dump()
        )

    def get_customers(self, db: Session):
        return self.repo.get_all(db)

    def get_customer(self, db: Session, customer_id: int):
        customer = self.repo.get_by_id(
            db,
            customer_id
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return customer

    def delete_customer(
        self,
        db: Session,
        customer_id: int
    ):
        customer = self.repo.get_by_id(
            db,
            customer_id
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        self.repo.delete(db, customer)

        return {"message": "Customer deleted"}