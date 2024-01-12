#The most generic product register ever. It can be used for store inventary or industry stock, etc
#I will try tuplas first

t = [ ]

def insert_product( ):

    product = []
    product.append ( input("insert product name: ") )
    product.append ( input("insert product weight: ") )
    product.append ( input("insert product price: ") )
    t.append( product )
    print ( "product register successfully: \n" )
    print( product )
    print('\n')
    main( )
    
def all_products( ) :

    print ("Product | Weight | Price ")

    for i in range( len ( t ) ) :
        print ( t [ i ] )
        
    main()

def main():
    
    option = input ("register product 1, list all registered products, 2. exit 3 \n ")

    if option == '1':
        insert_product( )
    
    elif option == '2':
        all_products( )

    elif option == '3':
        exit( )

    else:
        print ("invalid option")

if __name__ == "__main__" :
    main( )
