# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def is_coffee(drink):
    return 'coffee' in drink

def is_strawberry_milkshake(drink):
    return 'stawberry milkshake' in drink

def make_drink(drink, addons):
    if is_coffee(drink):
        mix = []
        mix = add(mix, 'coffee')
        mix = add(mix, addons)
    if is_strawberry_milkshake(drink):
        mix = []
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')
        mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
