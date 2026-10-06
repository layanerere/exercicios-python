anos_exp = float(input(" anos de experiencia na area:"))

if anos_exp >= 5:
    print("categoria: desenvolvedor senior")
elif anos_exp >= 2:
    print("categoria: desenvolver pleno")
else:
    print("categoria: desenvolver junior")