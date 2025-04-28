# tkinter-library-management

This project is a library management system built using Python's Tkinter library. It provides functionalities for managing books and members in a library.

## Project Structure

```
tkinter-library-management
├── main.py               # Main application logic for the library management system
├── login.py              # Login interface for the admin user
├── database              # Directory containing the SQLite database
│   └── bibliotheque.db   # Database file for storing information about books and members
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd tkinter-library-management
   ```

2. **Install required packages**:
   Ensure you have Python installed. You may need to install Tkinter if it's not included in your Python installation.

3. **Run the application**:
   Start the application by running the `login.py` file:
   ```
   python login.py
   ```

## Usage Guidelines

- Upon running `login.py`, you will be prompted to enter the admin username and password.
- Use the following credentials to log in:
  - Username: `louay`
  - Password: `louay123`
- After successful login, you will gain access to the main library management application.

## Features

- Add, delete, and manage books in the library.
- Add, delete, and manage library members.
- Switch between light and dark themes for better user experience.

## License

This project is licensed under the MIT License.