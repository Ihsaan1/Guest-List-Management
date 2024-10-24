def startup():

    while True:
        print('Options:')
        print('A. Add a guest')
        print('R. Remove a guest')
        print('P. Print guest list')
        print('Q. Quit')

        user_choice = input('Enter your choice: ').strip().upper()

        if user_choice == 'A':
            add_guest()
        elif user_choice == 'R':
            remove_guest()
        elif user_choice == 'P':
            print_guest_list()
        elif user_choice == 'Q':
            break
        else:
            print('Invalid choice. Please choose a valid option (A, R, P, or Q)')

guest_list = []

def add_guest():
    while True:
        guest_name = input('Enter the name of the guest to add: ')
        guest_list.append(guest_name)
        print(f'Guest {guest_name} has been added')
        break

def remove_guest():
    while True:
        guest_remove = input('Enter the name of the guest to remove: ')

        if guest_remove in guest_list:
            guest_list.remove(guest_remove)
            print(f'{guest_remove} has been removed from the guest list')
            break
        else:
            print(f'{guest_remove} is not on the guest list')

def print_guest_list():
    print(sorted(guest_list))

startup()