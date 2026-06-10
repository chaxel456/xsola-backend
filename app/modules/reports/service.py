from datetime import datetime


class ReportService:

    def generate_report(self, report_name: str):
        return {
            "report_name": report_name,
            "generated_at": datetime.utcnow()
        }