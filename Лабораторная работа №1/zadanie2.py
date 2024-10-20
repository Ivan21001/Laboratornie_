# Условие
V_Disketa_mb = 1.44
Chislo_stranits_v_knige = 100
Strok_na_stranitse = 50
Chislo_simvolov_v_stroke = 25
V_odnogo_simvola_byte = 4
odin_mb_raven_byte = 1024 ** 2
# Решение
V_Disketa_byte = V_Disketa_mb * odin_mb_raven_byte
V_odnoy_knigi_byte = Chislo_stranits_v_knige * Strok_na_stranitse * Chislo_simvolov_v_stroke * V_odnogo_simvola_byte
Chislo_knig_na_diskete = int(V_Disketa_byte/V_odnoy_knigi_byte)
print("Количество книг, помещающихся на дискету:", Chislo_knig_na_diskete)
