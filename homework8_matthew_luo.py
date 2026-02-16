def sandwich_ingredient(*items):
    print(f'\n Making a sandwich with the following ingredients:')
    for item in items:
        print(f'- {item}')

sandwich_ingredient('lettuce', 'tomato', 'onion', 'avocado')
sandwich_ingredient('meat','more meat')