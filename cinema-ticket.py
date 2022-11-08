from os import system
# DATA
m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titanic Zombie"


m_1_ticket_cost_a = 100.00
m_1_ticket_cost_b = 120.00

# HW1: use variables for HOURS / time
system("clear")
# MOVIE BOARD
print(
f"""
1. {m_title_1}
    a. 18:00
    b. 20:00
2. {m_title_2}
    a. 16:00
    b. 23:00
3. {m_title_3}
    a. 18:00
"""    
)


movie_number = input('Choose a movie: ') # '1'

if movie_number == '1':
    print(f"You've chosen '{m_title_1}'" )
    time = input('Choose time: ')

    if time == 'a':
        print(f'time: 18:00, ticket cost {m_1_ticket_cost_a}')
        cost = m_1_ticket_cost_a

    if time == 'b':
        print(f'time: 20:00, ticket cost {m_1_ticket_cost_b}')
        cost = m_1_ticket_cost_b

    amount = int(input('How many tickets: '))
    total = amount * cost
    print(f'{amount} x {cost} = {total}')


# HW2: finish the other 2 movies



if movie_number == '2':
    print(f"You've chosen '{m_title_2}'" )

if movie_number == '3':
    print(f"You've chosen '{m_title_3}'" )
