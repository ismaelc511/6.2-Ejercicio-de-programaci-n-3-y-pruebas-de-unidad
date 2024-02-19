import json
import os

class Hotel:
    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    @staticmethod
    def load_hotels(filename='hotels.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

    @staticmethod
    def save_hotels(data, filename='hotels.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_hotel(self):
        hotels = self.load_hotels()
        hotels.append(self.__dict__)
        self.save_hotels(hotels)

    @classmethod
    def delete_hotel(cls, hotel_id, filename='hotels.json'):
        hotels = cls.load_hotels(filename)
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        cls.save_hotels(hotels, filename)

    @classmethod
    def display_hotel_info(cls, hotel_id, filename='hotels.json'):
        hotels = cls.load_hotels(filename)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                print(json.dumps(hotel, indent=4))
                return
        print("Hotel not found.")

    @classmethod
    def modify_hotel_info(cls, hotel_id, updated_info, filename='hotels.json'):
        hotels = cls.load_hotels(filename)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(updated_info)
                cls.save_hotels(hotels, filename)
                return
        print("Hotel not found.")