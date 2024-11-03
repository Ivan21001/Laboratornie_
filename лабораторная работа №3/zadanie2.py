def find_common_participants(str_1, str_2, separator=","):
    comparison_str = set(str_1.split(separator))
    comparison = list(comparison_str.intersection(str_2.split(separator)))
    comparison.sort()
    return comparison


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
