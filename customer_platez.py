<<<<<<< HEAD
# https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/python
# I solved the Kata, but my code is too slow. More to learn!
series = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
id = 1
=======
series = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>>>>>> 952d572 (yeah)
def find_the_number_plate(customer_id):
    customer_plate = []
    customer_plate_series = []
    for i in range(26):
        for x in range(26):
            for y in range(26):
                customer_plate_series = series[y] + series[x] + series[i]
                for y in range(1, 1000):
                    customer_plate.append(customer_plate_series + str(y).rjust(3, '0'))
        return str(customer_plate[customer_id])
id = 675323
print(find_the_number_plate(id))
