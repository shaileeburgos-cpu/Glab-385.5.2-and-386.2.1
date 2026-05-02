# GLAB 385.5.2 - Event Management System
from datetime import datetime, date

# Temporary in‑memory database
events = {}

def add_event():
    event_name = input('Enter the event name: ')
    date_input = input('Enter the event date (YYYY-MM-DD): ')

    try:
        event_date = datetime.strptime(date_input, '%Y-%m-%d').date()
    except ValueError:
        print('❌ Invalid date format. Please use YYYY-MM-DD.')
        return

    events[event_name] = event_date
    print(f'🎉 Success! Added "{event_name}" to events.')

def get_event_date(tup):
    return tup[1]

def list_events():
    if len(events) == 0:
        print('🚨 No upcoming events 🚨')
        return

    print('\n🌟🌟 Upcoming Events 🌟🌟')
    sorted_events = sorted(events.items(), key=get_event_date)

    for e_name, e_date in sorted_events:
        today = date.today()
        days_remaining = (e_date - today).days
        print(f'🍾 {e_name} — {e_date} — {days_remaining} days remaining')

def delete_event():
    event_to_delete = input('Enter the name of the event to delete: ')

    if event_to_delete in events:
        del events[event_to_delete]
        print(f'✅ Successfully deleted "{event_to_delete}"')
    else:
        print('❌ Event not found. Check spelling.')

def main():
    while True:
        print('\n 📝 Event Management System 📝')
        print('1. Add Event')
        print('2. List Events')
        print('3. Delete Event')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print('🛑 Program closed. Goodbye!')
            break
        else:
            print('Invalid option. Try again.')

if __name__ == '__main__':
    main()
