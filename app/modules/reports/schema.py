from pydantic import BaseModel


class DashboardReport(BaseModel):
    total_users: int
    total_customers: int
    total_devices: int
    total_subscriptions: int

    total_payments: int
    

