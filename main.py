"""Este módulo contiene la lógica del sistema de reservaciones."""
from Hotel import Hotel
from Customer import Customer
from Reservation import Reservation


def main():
    """Ejecuta la lógica principal del programa."""

    # Crear e instanciar hoteles
    hotel1 = Hotel("H001", "Sunrise", "Down", {101: 'ava', 102: 'res'})
    hotel2 = Hotel("H002", "Ocean", "Bea", {201: 'ava', 202: 'ava'})

    # Crear hoteles en el archivo de almacenamiento
    print("Creando hoteles...")
    hotel1.create_hotel()
    hotel2.create_hotel()

    # Mostrar información de un hotel específico
    print("\nMostrando información del Hotel 1:")
    Hotel.display_hotel_info("H001")

    # Modificar la información de un hotel
    print("\nModificando información del Hotel 1...")
    Hotel.modify_hotel_info("H001", {"name": "Sunset", "location": "Up"})

    # Mostrar la información actualizada del hotel
    print("\nMostrando información actualizada del Hotel 1:")
    Hotel.display_hotel_info("H001")

    # Eliminar un hotel
    print("\nEliminando Hotel 2...")
    Hotel.delete_hotel("H002")

    # Intentar mostrar la información del hotel eliminado para confirmar
    print("\nIntentando mostrar información del Hotel 2 después de eliminar:")
    Hotel.display_hotel_info("H002")

    # Crear e instanciar clientes
    customer1 = Customer("C001", "Alice Johnson", "alice@example.com")
    customer2 = Customer("C002", "Bob Smith", "bob@example.com")

    # Crear clientes en el archivo de almacenamiento
    print("\nCreando clientes...")
    customer1.create_customer()
    customer2.create_customer()

    # Mostrar información de un cliente específico
    print("\nMostrando información del Cliente 1:")
    Customer.display_customer_info("C001")

    # Modificar la información de un cliente
    print("\nModificando información del Cliente 1...")
    Customer.modify_customer_info("C001", {"name": "A", "contact": "a@h.com"})

    # Mostrar la información actualizada del cliente
    print("\nMostrando información actualizada del Cliente 1:")
    Customer.display_customer_info("C001")

    # Eliminar un cliente
    print("\nEliminando Cliente 2...")
    Customer.delete_customer("C002")

    # Muestra la información del cliente eliminado para confirmar
    print("\nMuestra la información del Cliente 2 después de eliminar:")
    Customer.display_customer_info("C002")

    # Crear e instanciar reservaciones
    reservation1 = Reservation("R1", "C1", "H1", 101, "2024-03", "2024-03")
    reservation2 = Reservation("R2", "C1", "H1", 102, "2024-03", "2024-03")

    # Crear reservaciones en el archivo de almacenamiento
    print("\nCreando reservaciones...")
    reservation1.create_reservation()
    reservation2.create_reservation()

    # Mostrar información de una reservación específica
    print("\nMostrando información de la Reservación 1:")
    Reservation.display_reservation_info("R001")

    # Cancelar una reservación
    print("\nCancelando Reservación 2...")
    Reservation.cancel_reservation("R002")

    # Muestra la información de la reservación cancelada para confirmar
    print("\nMuestra información de la Reservación 2 después de cancelar:")
    Reservation.display_reservation_info("R002")


if __name__ == "__main__":
    main()
