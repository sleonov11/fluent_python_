import csv

class CSVDataset:
    def __init__(self, filepath):
        self._data = []
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            self._data = list(reader)
            self.header = reader.fieldnames
    def __len__(self):
        return len(self._data)
    def __getitem__(self, index):
        return self._data[index]


ds = CSVDataset("test.csv")
print(f'Всего строк {len(ds)}')
print(f"Первая строка: {ds[0]}")
print(f"Последняя строка: {ds[-1]}")
print(f"Срез: {ds[1:]}")