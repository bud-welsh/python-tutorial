player_name = "Babe Ruth"
games = 2503
at_bats = 8398
plate_apperances = 10616
singles = 1517
doubles = 506
triples = 136
homeruns = 714
runs = 2174
runs_batted_in = 2217
walks = 2062
strikeouts = 1330
hit_by_pitch = 43
sacrifice_hit = 113
stolen_bases = 123
caught_stealing = 117

hits = singles + doubles + triples + homeruns
total_bases = (singles + (doubles * 2) + (triples * 3) + (homeruns * 4))
batting_average = hits / at_bats

print(hits)
print(batting_average)
print (total_bases)
