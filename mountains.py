mountains = [
    ("Mount Everest", "Nepal and China", 29032),
    ("K2", "Pakistan and China", 28251),
    ("Kangchenjunga", "Nepal and India", 28169),
    ("Lhotse", "Nepal and China", 27940),
    ("Makalu", "Nepal and China", 27838),
    ("Cho Oyu", "Nepal and China", 26864),
    ("Dhaulagiri I", "Nepal", 26795),
    ("Manaslu", "Nepal", 26781),
    ("Nanga Parbat", "Pakistan", 26660),
    ("Annapurna I", "Nepal", 26545),
]

print("10 Highest Mountains in the World")
for rank, (name, country, height_feet) in enumerate(mountains, start=1):
    print(f"{rank}. {name} - {country} - {height_feet:,} ft")