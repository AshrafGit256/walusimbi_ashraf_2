from multipledispatch import dispatch

@dispatch(int, int, int)

def product_price(sugar, rice, soap):
    products = sugar+rice+soap
    print('Total products purchased:', products)
    
@dispatch(float, float, float)

def product_price(sugar, rice, soap):
    products = sugar+rice+soap
    print('Total amount paid: shs.',products)
    
product_price(4,2,3)
product_price(2400.5, 3600.5, 8100.5)