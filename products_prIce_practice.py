# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品, 價格' in line:
            continue #繼續 跳到下一迴的意思 跟break一樣只能寫在迴圈裡
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)



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

with open ('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')