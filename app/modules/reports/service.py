from sqlalchemy.orm import Session

from app.modules.users.model import User
from app.modules.customers.model import Customer
from app.modules.devices.model import Device
from app.modules.subscriptions.model import Subscription
from app.modules.payments.model import Payment


class ReportService:

    def get_dashboard(self, db: Session):

        total_users = db.query(User).count()

        total_customers = db.query(Customer).count()

        total_devices = db.query(Device).count()

        total_subscriptions = db.query(
            Subscription
        ).count()

        total_payments = db.query(
            Payment
        ).count()

        return {
            "total_users": total_users,
            "total_customers": total_customers,
            "total_devices": total_devices,
            "total_subscriptions": total_subscriptions,
            "total_payments": total_payments
        }