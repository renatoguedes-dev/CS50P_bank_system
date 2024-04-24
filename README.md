# Bank Account Management System
    #### Video Demo:  https://youtu.be/GqQeKEhQot4

#### Description:

Welcome to the Bank Account Management System! This project aims to provide a simple yet effective system for managing bank accounts for individual clients. Developed using Python, this system allows clients to deposit and withdraw funds, view their account statements, open new accounts, list their existing accounts, and register new clients.

## Project Structure

The project consists of three main classes:

1. **Client**: This class represents a client of the bank. It contains methods for listing clients and filtering clients based on their SSN (Social Security Number). Additionally, it includes a method for registering new clients.

2. **Individual**: Inherits from the Client class, representing individual clients specifically. It includes methods for registering new clients, checking if an SSN already exists, and properties for retrieving client information.

3. **Account**: This class handles the bank accounts associated with clients. It includes methods for opening new accounts, depositing and withdrawing funds, updating account statements, displaying account statements, and listing accounts.

## Design Choices

### Object-Oriented Approach

The project follows an object-oriented approach to modeling clients and accounts, which allows for easier management and scalability. By utilizing classes and inheritance, the code becomes more organized and modular. Object-oriented programming (OOP) enables encapsulation, inheritance, and polymorphism, making the codebase easier to understand, maintain, and extend.

### Static Methods and Class Methods

Static and class methods are used where appropriate to encapsulate functionality that is not specific to instances of the class. For example, the `filter_client()` method in the Client class is a static method used to filter clients based on their SSN. Static methods do not require access to instance attributes and can be called directly on the class itself. Class methods, on the other hand, have access to the class itself via the `cls` parameter, allowing them to modify class-level attributes or call other class methods.

### Validation and Error Handling

The project includes comprehensive validation checks for user input, such as validating dates and numerical values. Error handling is implemented to gracefully handle invalid inputs and prevent runtime errors. For instance, the `validate_date()` function ensures that the date format is correct before proceeding with further operations. Similarly, the `is_number()` function validates whether a given input is a valid numerical value, preventing errors during deposit or withdrawal operations.

### User Interface

A simple text-based menu system is provided for interacting with the bank account management system. Users can choose options from the menu to perform various actions, making the system easy to use and navigate. The menu-driven interface enhances user experience by providing clear options and prompts, guiding users through different functionalities of the system. Additionally, informative messages are displayed to provide feedback to users regarding their actions, ensuring a smooth and intuitive interaction with the system.

## Future Improvements

While the current implementation provides basic functionality for managing bank accounts, there are several areas for potential improvement:

- Enhanced Error Handling: Implement more robust error handling to handle edge cases and unexpected inputs. This could involve incorporating try-except blocks to catch specific exceptions and provide meaningful error messages to users.
- Security Features: Introduce authentication and authorization mechanisms to ensure the security of client accounts. Implementing user authentication via username/password and access control based on user roles can enhance the security of the system and protect sensitive client information.
- Data Persistence: Implement data storage and retrieval mechanisms to persist client and account information between sessions. This could involve integrating a database backend to store client data securely and enable features such as transaction history and account statements.
- User Interface Enhancements: Improve the user interface by adding more informative prompts and feedback messages. Enhancing the graphical user interface (GUI) or providing additional features such as transaction summaries and account analytics can further enhance the user experience and usability of the system.

## Conclusion

The Bank Account Management System project provides a foundation for managing individual bank accounts in a simple and efficient manner. With its object-oriented design, comprehensive validation checks, and user-friendly interface, it offers a convenient solution for both clients and bank administrators. By incorporating future improvements such as enhanced error handling, security features, data persistence, and user interface enhancements, the system can be further refined to meet the evolving needs of banking operations and provide a seamless banking experience to users.
