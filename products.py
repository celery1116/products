products = []

while True:
	name = input('請輸入商品名稱')
	if name == 'q' :
		break
	price = input('請輸入商品價格')
	products.append([name,price])

for p in products:
	print(p[0],'的價格是',p[1])

file = 'products.csv'
with open (file,'w') as f:
	f.write('品項'+ ',' + '價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')