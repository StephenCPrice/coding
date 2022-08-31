series = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
id = 1
def find_the_number_plate(customer_id):
    customer_plate = ()
    customer_plate_series = ''
    for i in range(26):
        for x in range(26):
            for y in range(26):
                customer_plate_series = series[y] + series[x] + series[i]
                for p in range(1, 1000):
                    customer_plate = customer_plate + eval(str(customer_plate_series + str(p).rjust(3, '0')))
        return customer_plate[customer_id]
print(find_the_number_plate(id))
