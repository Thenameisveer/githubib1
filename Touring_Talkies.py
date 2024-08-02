print ("Hi, Welcome to Touring Talkies: Your Ultimate designation for tickets and showtimes!\n")
print ("Secure your seats : Book your movie tickets Now!\n")

def main():
    cities = {
        "Chennai": {
            "theaters": ["PVR Velachery", "AGS T-nagar", "Rohini Koyambaedu"],
            "movies": ["Raayan", "Indian 2", "Deadpool & Wolverine", "Kalki 2898 AD"]
        },
        "Madurai": {
            "theaters": ["Guru Cinemas", "Cini Priya", "Gopuram"],
            "movies": ["Raayan", "Indian 2", "Deadpool & Wolverine", "Kalki 2898 AD"]
        },
        "Trichy": {
            "theaters": ["Mariyam Cinemas", "LA Cinemas", "Shanthi Cinemas"],
            "movies": ["Raayan", "Indian 2", "Deadpool & Wolverine", "Kalki 2898 AD"]
        }
    }

    show_timings = ["10:30 AM", "2:30 PM", "6:00 PM", "9:30 PM"]
    
    show_dates = ["01-Aug-24", "02-Aug-24", "03-Aug-24", "04-Aug-24"]

    print("Select a city:")
    city = select_option(list(cities.keys()))
    
    print("\nSelect a movie:")
    movie = select_option(cities[city]["movies"])

    print("\nSelect a theater:")
    theater = select_option(cities[city]["theaters"])

    print("\nSelect a show dates:")
    show_time = select_option(show_dates)
    
    print("\nSelect a show timing:")
    show_time = select_option(show_timings)

    print("\nEnter number of seats:")
    num_seats = int(input())
    
    seats = select_seats(num_seats)
    
    print("\nBooking Review:\n")
    print(f"City: {city}")
    print(f"Movie: {movie}")
    print(f"Theater: {theater}")
    print(f"Show Time: {show_time}")
    print(f"Seats: {', '.join(seats)}\n")
    
    
    confirm = input ('Press "(y/n)" to confirm booking : \n') 
    if confirm == 'y':
        print("\nTICKET(S) BOOKED SUCCESSFULLY, ENJOY YOUR MOVIE!\n")
    else:
        print("\nBack to Main Page\n")
        print("\nSelect a movie:\n")
        return select_option(cities[city]["movies"])
            
        
    
    
    

def select_option(options):
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    while True:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= choice <= len(options):
            return options[choice - 1]
        else:
            print("Invalid choice. Try again.")

def select_seats(num_seats):
    seats = []
    for i in range(num_seats):
        while True:
            seat = input(f"Select seat {i + 1}: ")
            if seat not in seats:
                seats.append(seat)
                break
            else:
                print("Seat already taken. Choose another seat.")
    return seats


main()



