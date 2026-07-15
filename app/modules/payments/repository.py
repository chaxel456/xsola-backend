from sqlalchemy.orm import Session

from app.modules.payments.model import Payment


class PaymentRepository:

    def create(self, db: Session, data: dict):

        payment = Payment(**data)

        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment

    def get_all(self, db: Session):

        return db.query(Payment).all()

    def get_by_id(
        self,
        db: Session,
        payment_id: int
    ):

        return (
            db.query(Payment)
            .filter(Payment.id == payment_id)
            .first()
        )

    def delete(
        self,
        db: Session,
        payment
    ):

        db.delete(payment)
        db.commit()