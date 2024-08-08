# Garment Store Management System

## Overview

The Garment Store Management System is a console-based Python application that allows store owners to manage their inventory, customer information, and orders, while also enabling customers to create accounts, log in, view products, and place orders. This system uses CSV files for data storage and management.

## Features

### For Customers:
1. **Account Creation**: New users can create an account by providing their name, phone number, address, and email. A unique username is generated for them.
2. **Login**: Existing customers can log in using their username and password.
3. **View Products**: Customers can browse available products and see the details of products they have viewed.
4. **Product Recommendations**: Based on the products viewed, the system can recommend additional products.
5. **Place Orders**: Customers can place orders for the products they are interested in.
6. **Request Products**: Customers can request products that are not currently in stock.
7. **Logout**: Customers can log out, with their login and logout times recorded.

### For Store Owners:
1. **Product Management**: Owners can add new products to the inventory, including the product name and company name.
2. **Customer Management**: Owners can view the total number of customers and detailed information about each customer.
3. **Order Management**: Owners can view orders placed by customers.
4. **Product Demand Management**: Owners can see which products are in demand based on customer requests.

## File Structure

The application uses the following CSV files for data storage:

- **`formality`**: Stores usernames and passwords for login authentication.
- **`user_info`**: Stores customer information such as username, name, phone number, address, and email.
- **`stockinfo`**: Stores product information including product name and company name.
- **`items_checked`**: Tracks products that customers have viewed.
- **`orders_info`**: Stores information about products that customers have ordered.
- **`request_info`**: Stores customer requests for products not currently in stock.

## How to Run the Program

1. **Ensure Python is Installed**: Make sure Python is installed on your system. This program is written in Python 3.

2. **Download or Clone the Project**: Obtain the source code for the project and place it in a directory on your computer.

3. **Run the Program**: Open a terminal, navigate to the directory containing the source code, and run the script using the command:
    ```
    python <script_name>.py
    ```
    Replace `<script_name>` with the name of the Python file.

4. **Follow On-Screen Instructions**: The program is interactive and will guide you through various options such as creating an account, logging in, managing products, etc.

## Program Flow

### For Customers:
1. **Main Menu**: Choose between creating a new account or logging in.
2. **After Login**: View and interact with available products, receive recommendations, place orders, request products, and log out.

### For Store Owners:
1. **Login as Owner**: Enter the owner key to access the management section.
2. **Management Section**: Add new products, view customer details, check orders, and see product requests.

## Notes and Limitations
- **Data Persistence**: The system uses CSV files to store all data. Make sure these files are in the same directory as the script and are not manually modified to prevent data corruption.
- **Security**: Passwords are stored in plain text. For a production system, consider implementing secure password storage and more robust authentication.
- **User Interface**: The system is console-based, with text input and output. Enhancing the user interface with a graphical or web-based frontend could improve usability.

## Future Enhancements
- Implement secure password hashing and storage.
- Add more detailed product information, including pricing and availability.
- Develop a graphical user interface (GUI) or a web-based interface for better user experience.
- Implement search functionality for products and customers.
- Enhance the recommendation system with more sophisticated algorithms.

## Contact
For any questions or suggestions, please contact the developer at [adityaforgames03@gmail.com].
