#print('Hell yeah')
#print('--------- Format string as an fake table----------')
"""
print('{0:>10}| {1:<20}| {2:^15}'.format('Id', 'Name', 'Qty'))
print('{0:>10}| {1:<20}| {2:^15.2f}'.format(
    '01', 'Frist Product', 5.9878989987979))
print('{0:>10}| {1:<20}| {2:^15}'.format('02', 'Second Product', '15'))
print('{0:>10}| {1:<20}| {2:^15}'.format('03', 'Third Product', '8'))
"""
# --------------Read the user's input--------------
"""
Here is the way to read user input 
then print it in terminal
"""
#magentoVersion = input('Currunt magento version that I use is: ')
#print('{} is the current magento version that you use'.format(magentoVersion))

# -----------Function defination--------------


def showProductName(productName='default product'):
    """ Document: this function will return the product name that customer pass to function otherwise it will return default product"""
    print('New Marimekko dress available in store, here is you product: {} '.format(
        productName))


showProductName('Bim pamper')
