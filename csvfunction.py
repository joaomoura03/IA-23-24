import csv
import random


class csvfunction:

    def print_delivery():
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                print(row)


    def print_ranking():
        with open('csv/ranking.csv', 'r') as ranking_csv:
            reader_csv = csv.reader(ranking_csv)
            for row in reader_csv:
                print(row[:-1])


    def search_start(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[4]
                    return line_row


    def search_end(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[5]
                    return line_row


    def time_of_travel(line, distance):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    if row[2] == 'Bicicleta':
                        final_time = (distance/(10 - 0.6 * float(row[3])))*60
                        return final_time

                    if row[2] == 'Mota':
                        final_time = (distance/(35 - 0.5 * float(row[3])))*60
                        return final_time

                    if row[2] == 'Carro':
                        final_time = (distance/(50 - 0.1 * float(row[3])))*60
                        return final_time


    def create_courier():
        name = input("Introduza nome do estafeta: ")
        row_to_write = [name, '0', '0', '0']

        with open("csv/ranking.csv", 'a', newline='\n') as ranking_csv:
            csv_writer = csv.writer(ranking_csv)
            csv_writer.writerow(row_to_write)

                    
    def create_order():
        weight = int(input("Introduza o peso da sua encomenda: "))
        start = input("Introduza local de recolha: ")
        end = input("Introduza local de entrega: ")
        time = int(input("Introduza tempo limite de entrega em minutos: "))

        list_of_couriers = []
        with open('csv/ranking.csv', 'r') as ranking_csv:
            reader_csv = csv.reader(ranking_csv)
            for row in reader_csv:
                if row:
                    list_of_couriers.append(row[0])
        list_of_couriers.pop(0)

        with open("csv/delivery.csv", 'r') as delivery_csv:
            csv_reader = csv.reader(delivery_csv)
            lines = list(csv_reader)
            if lines:
                first_element_last_line = lines[-1][0]

        if weight <= 5:
            row_to_write = [int(first_element_last_line) + 1, random.choice(list_of_couriers), 
                            'Bicicleta', weight, start, end, time]

        elif 5 < weight <= 20:
            row_to_write = [int(first_element_last_line) + 1, random.choice(list_of_couriers), 
                            'Mota', weight,  start, end, time]

        elif 20 < weight <= 100:
            row_to_write = [int(first_element_last_line) + 1, random.choice(list_of_couriers), 
                            'Carro', weight,  start, end, time]

        with open("csv/delivery.csv", 'a', newline='\n') as delivery_csv:
            csv_writer = csv.writer(delivery_csv)
            csv_writer.writerow(row_to_write)

    
    def rank_courier(line, rank_deduction):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row in reader_delivery_csv:
                if row[0] == line:
                    courier = row[1]

        with open("csv/ranking.csv", 'r') as ranking_csv:
            reader_ranking_csv = csv.reader(ranking_csv)
            data = list(reader_ranking_csv)
            i = 0
            for row in data:
                if row[0] == courier:
                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    new_numero = float(row[3]) + stars - rank_deduction
                    new_total = float(row[2]) + 1.0
                    new_classificaçao = new_numero/new_total
                    row = [courier, new_classificaçao, new_total, new_numero]
                    data[i] = row
                i += 1

        with open("csv/ranking.csv", 'w') as ranking_csv:
            writer_csv = csv.writer(ranking_csv)
            writer_csv.writerows(data)
        
        return new_classificaçao

    
    def check_time(line, time):
        with open("csv/delivery.csv", 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row in reader_delivery_csv:
                if row[0] == line:
                    if int(row[6]) >= time:
                        print("\nO estafeta fez a entrega a tempo")
                        return True
                    else:
                        print("\nO estafeta não fez a entrega a tempo")
                        print("O estafeta terá uma dedução automática no seu ranking")
                        return False
                    
    
    def deliver(line, time, rank):
        line_delivered = []
        with open("csv/delivery.csv", 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row_delivery in reader_delivery_csv:
                if row_delivery[0] == line:
                    line_delivered = row_delivery

        line_delivered.append(time)
        line_delivered.append(rank)

        with open("csv/delivered.csv", 'a', newline='\n') as delivered_csv:
            writer_delivered_csv = csv.writer(delivered_csv)
            writer_delivered_csv.writerow(line_delivered)

    
    def print_delivered():
        with open("csv/delivered.csv", 'r') as deliver_csv:
            reader_deliver_csv = csv.reader(deliver_csv)
            for row in reader_deliver_csv:
                print(row)


    def remove_delivery(line):
        with open ("csv/delivery.csv", 'r', newline='') as delivery_csv:
            data = list(csv.reader(delivery_csv))

        del data[int(line)]

        with open("csv/delivery.csv", 'w', newline='') as delivery_csv:
            csv.writer(delivery_csv).writerows(data)