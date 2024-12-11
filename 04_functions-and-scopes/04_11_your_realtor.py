# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def realtor_advert(**kwargs):
    print("Real estate advertisement:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

realtor_advert(sale_price=100000, location="Downtown", square_footage=2000, year_built=1990)
print(f"realtor_advert)")