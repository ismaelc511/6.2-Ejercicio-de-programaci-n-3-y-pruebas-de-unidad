import json
import os

class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id, room_number, start_date, end_date):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def load_reservations(filename='reservations.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

    @staticmethod
    def save_reservations(data, filename='reservations.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_reservation(self):
        reservations = self.load_reservations()
        reservations.append(self.__dict__)
        self.save_reservations(reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id, filename='reservations.json'):
        reservations = cls.load_reservations(filename)
        reservations = [reservation for reservation in reservations if reservation['reservation_id'] != reservation_id]
        cls.save_reservations(reservations, filename)

    @classmethod
    def display_reservation_info(cls, reservation_id, filename='reservations.json'):
        reservations = cls.load_reservations(filename)
        for reservation in reservations:
            if reservation['reservation_id'] == reservation_id:
                print(json.dumps(reservation, indent=4))
                return
        print("Reservation not found.")

