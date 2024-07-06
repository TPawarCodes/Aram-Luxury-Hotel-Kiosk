# Aram-Luxury-Hotel-Kiosk

# ARAM Luxury Hotel Management System

## Overview
The ARAM Luxury Hotel Management System is a comprehensive tool designed to streamline hotel operations, including room booking, stay modifications, room service, customer details management, and bill payment. This system is built using Python and MySQL, ensuring robust data handling and ease of use.

## Features
1. **Book New Room**: Facilitates new room bookings by collecting customer details and providing room options with respective pricing.
2. **Make Changes to Current Stay**: Allows changes to the customer's stay, such as extending the checkout date or changing the room type.
3. **Room Service**: Manages room service orders, updates bills, and prints detailed receipts.
4. **Check Customer Details**: Retrieves and displays detailed customer information.
5. **Bill Payment**: Displays payment details and processes bill payments.
6. **Staff Portal**: Enables staff to add new employees, update customer details manually, and update the restaurant menu.

## Getting Started

### Prerequisites
- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/aram-hotel-management.git
   cd aram-hotel-management
   ```

2. **Install Required Python Packages**
   ```bash
   pip install mysql-connector-python
   pip install tabulate
   ```

3. **Set Up the MySQL Database**
   - Create a new MySQL database named `ARAM_HOTEL`.
   - Execute the SQL script `setup.sql` provided in the repository to create the necessary tables and insert initial data.

### Configuration

Update the MySQL connection parameters in the `main.py` file to match your MySQL server configuration:
```python
mydb = mysql.connector.connect(
    user="root",
    password="yourpassword",
    host="localhost",
    database="ARAM_HOTEL"
)
```

### Running the Application

Execute the `main.py` file to start the application:
```bash
python main.py
```

## Usage

### Main Menu

Upon running the application, you will be greeted with a main menu where you can select from the following options:

1. **Book New Room**: Follow the prompts to enter customer details and book a room.
2. **Make Changes to Current Stay**: Modify existing bookings.
3. **Room Service**: Add room service orders to the customer's bill.
4. **Check Customer Details**: View detailed information about customers.
5. **Bill Payment**: Process bill payments and generate receipts.
6. **Staff Portal**: Access staff functionalities such as adding employees and updating customer details.

### Staff Portal

The staff portal requires an employee ID and password for access. Once logged in, staff members can:
- Add new employees
- Check and update customer details manually
- Update the restaurant menu

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

**Note:** This is a basic implementation. You can extend its functionality by adding more features, improving the user interface, and enhancing security measures.

---
