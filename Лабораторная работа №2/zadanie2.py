salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10
increase = 0.03  # Ежемесячный рост цен

# increase должно быть 0.05, как я думаю, но тогда не сойдётся ответ ;(

trati = 0
doxodi = salary * months
for _ in range(months):
    if _ == 0:
        trati = spend
    else:
        spend *= 1 + increase
        trati += spend
money_capital = trati - doxodi
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
