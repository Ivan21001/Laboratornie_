money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mnogitel_poviheniya_tsen = 1 + increase
kol_mesyatsev_bez_dolgov = 0
while money_capital > 0:
    if kol_mesyatsev_bez_dolgov >= 1:
        money_capital = money_capital + salary - spend
        spend = spend * mnogitel_poviheniya_tsen
        if money_capital > 0:
            kol_mesyatsev_bez_dolgov += 1
    else:
        money_capital = money_capital + salary - spend
        spend = spend * mnogitel_poviheniya_tsen
        kol_mesyatsev_bez_dolgov += 1

print("Количество месяцев, которое можно протянуть без долгов:", kol_mesyatsev_bez_dolgov)
