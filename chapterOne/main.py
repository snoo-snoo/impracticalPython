""" CH-01 -Chapter One: Silly Name Generator """

import sys, random

print('Welcome to the Psych \'Sidekick Name Generator\'.\n')
print('A name just like Snoo would pick for Discostu.\n'')

first_names = (
    'Janeth', 'Scarlet', 'Regan', 'Lyn', 'Carina', 'Jolanda', 'Sima', 'Preston', 'Flo', 'Kasey', 'Jamaal', 'Jeanine',
    'Maura', 'Tyrell', 'Vickey', 'Elisha', 'Britta', 'Aimee', 'Ladawn', 'Adam', 'Octavia', 'Keena', 'Otto', 'Reinaldo',
    'Gwenn', 'Sunny', 'Latrisha', 'Vanesa', 'Emerson', 'Tiara', 'Jamila', 'Refugio', 'Tami', 'Aida', 'Angelic', 'Angle',
    'Pennie', 'Wilbur', 'Savannah', 'Phung', 'Rashad', 'Silvia', 'Lorene', 'Nelda', 'Paulene', 'Molly', 'Cherrie',
    'Ivana',
    'Jong', 'Reggie', 'Aero', 'Buddy', 'Bucky', 'Zorg', 'Dippy', 'Zee Zee', 'Kiddo', 'Reddy', 'Zip Zap', 'Zingo',
    'Zero',
    'Thunder', 'Beefy', 'Tramps', 'Waldo', 'Junior', 'Boop', 'Snips', 'Baby-Oil', 'Salte', 'Wheels', 'Pops')

surnames = (
    'Lightning-Leopard', 'Mega-Wraith', 'Blue Blockbuster', 'Golden Gastropod', 'Conquering Queen', 'Miltiversio',
    'Night Champion', 'Mighy Dynamo', 'Super-ARcher', 'Space Mermaid', 'Dinosaur Damsel', 'Laser-Eyes',
    'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Buttergaugh', 'Clovenhoff', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Hooperbag', 'Jenkins', 'Jefferson', 'Kingfish', 'Listenbee', 'McFadden',
    'Moonshine', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Winterkorn', 'Woolysocks'
)

while True:
    first_name = random.choice(first_names)
    surname = random.choice(surnames)

    print('\n\n')
    print('{} {}'.format(first_name, surname), file=sys.stderr)
    print('\n\n')

    try_again = input('\n\nTry again? (Press Enter else n to quit)\n ')
    if try_again.lower() == 'n':
        break

input('\nPress Enter to exit.')
