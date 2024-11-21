import csv  # TODO импортировать необходимые молули
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(file: csv) -> None:
    with open(file, "r", encoding="utf-8") as f:
        content = csv.DictReader(f, delimiter=',', quotechar='\n')
        data: list = []
        for row_ in content:
            data.append(row_)
        with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
