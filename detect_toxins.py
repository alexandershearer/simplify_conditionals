# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')


ingredients = ['sodium benzoate', 'sodium nitrate', 'sodium oxide']

def is_toxic(ingredients):
    return 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients\
    or 'sodium oxide' in ingredients:

def check_toxic():
    if is_toxic(ingredients):
        print('!!!')
        print('there is a toxin in the food!')    
        print('!!!')
        make_alert_sound()
    else:
        print('***')
        print('Toxin Free')
        print('***')
        make_accept_sound()
