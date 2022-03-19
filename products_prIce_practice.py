products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    p = []
    p.append(name)
    p.append(price)
    # or 速寫 把上三行也可寫成 p = [name,price] 
    products.append(p)
print(products)

for p in products:
    print(p[0], '的價格', '是', p[1]) 