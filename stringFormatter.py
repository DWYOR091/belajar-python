# f-string
txt = "hello world"
print(txt)

# placeholder and modifier
price = 50
txt2 = f"harga buah mangga 1kg Rp.{price:.3f}"
print(txt2)

#operation in f string
txt3 = f"hasil perkalian: {2*2}"
print(txt3)

#execute function
name = "rifqi"
txt4 = f"hello {name.upper()}"
print(txt4)

price2 = 20000
txt5 = "harga pulpen {}"
print(txt5.format(price2))