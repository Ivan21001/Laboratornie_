# TODO решите задачу
import json


def task(file: json) -> float:
    with open(file, "r", encoding="utf-8") as f:
        content: list = json.load(f)
        counter_: float = 0
        for dicts_ in content:
            multiplication: float = float(dicts_["score"] * dicts_["weight"])
            counter_ += multiplication
    return counter_


print(round(task("input.json"), 3))
