from sqlalchemy.orm import Session

from app.modules.customers.model import Customer


class CustomerRepository:

    def create(self, db: Session, customer_data: dict):
        customer = Customer(**customer_data)

        db.add(customer)
        db.commit()
        db.refresh(customer)

        return customer

    def get_all(self, db: Session):
        return db.query(Customer).all()

    def get_by_id(self, db: Session, customer_id: int):
        return (
            db.query(Customer)
            .filter(Customer.id == customer_id)

            .first()  
            .first()

        )

    def delete(self, db: Session, customer: Customer):
        db.delete(customer)
        db.commit()