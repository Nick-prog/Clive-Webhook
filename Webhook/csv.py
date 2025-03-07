import os
import pandas as pd
from csv import DictWriter
from datetime import datetime

class CSV:

    def __init__(self, metadata: list, path: str):
        self.metadata = metadata
        self.path = path

    def create_csv(self, select: int) -> None:

        select_type = {
            1: 'Upload Document Portal',
            2: 'Fee Wavier Portal'
        }
        date = datetime.now()

        filepath = f'{self.path}/{date.strftime("%B %Y")}/{date.strftime("%m.%d.%Y")}/{select_type[select]}_{date.strftime("%Y-%m-%d")}.csv'

        if len(self.metadata) != 0:

            headers = [key for key, value in self.metadata[select-1][0].items()]

            with open(filepath, 'a', newline='') as outfile:
                writer = DictWriter(outfile, tuple(headers))
                if os.path.exists(filepath):
                    writer.writeheader()
                writer.writerows(self.metadata[select-1])
