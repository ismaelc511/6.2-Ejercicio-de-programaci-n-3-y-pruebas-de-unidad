import json
import os

class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info

    @staticmethod
    def load_customers(filename='customers.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

    @staticmethod
    def save_customers(data, filename='customers.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_customer(self):
        customers = self.load_customers()
        customers.append(self.__dict__)
        self.save_customers(customers)

    @classmethod
    def delete_customer(cls, customer_id, filename='customers.json'):
        customers = cls.load_customers(filename)
        customers = [customer for customer in customers if customer['customer_id'] != customer_id]
        cls.save_customers(customers, filename)

    @classmethod
    def display_customer_info(cls, customer_id, filename='customers.json'):
        customers = cls.load_customers(filename)
        for customer in customers:
            if customer['customer_id'] == customer_id:
                print(json.dumps(customer, indent=4))
                return
        print("Customer not found.")

    @classmethod
    def modify_customer_info(cls, customer_id, updated_info, filename='customers.json'):
        customers = cls.load_customers(filename)
        for customer in customers:
            if customer['customer_id'] == customer_id:
                customer.update(updated_info)
                cls.save_customers(customers, filename)
                return
        print("Customer not found.")
