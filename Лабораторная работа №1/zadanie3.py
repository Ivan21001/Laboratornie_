list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
kolichestvo_komand = 2
Kolichestvo_vsex_igrokov = len(list_players)
Kolichestvo_igrokov_v_dvux_komandax = int(Kolichestvo_vsex_igrokov/kolichestvo_komand)
Pervaya_komanda = list_players[0:Kolichestvo_igrokov_v_dvux_komandax]
Vtoraya_komanda = list_players[Kolichestvo_igrokov_v_dvux_komandax:]
print(Pervaya_komanda)
print(Vtoraya_komanda)
