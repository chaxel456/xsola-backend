import csv
from pathlib import Path


class FileService:

    def export_csv(
        self,
        filename: str,
        rows: list
    ):

        filepath = Path(filename)

        with open(
            filepath,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            for row in rows:
                writer.writerow(row)

        return str(filepath)