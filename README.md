# Inventory & Stock Management System (ISMS)

A web-based Inventory and Stock Management System designed to manage users, products, inventory transactions, and stock-related operations through a centralized application.

## Project Overview

The Inventory & Stock Management System (ISMS) provides a structured platform for managing inventory operations. It aims to simplify product management, monitor stock movement, and maintain transaction records.

This repository is being maintained and further developed to understand the existing application architecture, improve functionality, and explore practical implementation of inventory workflows.

## Key Features

- **User Authentication:** Login and session-based user access.
- **Role-Based Access Control:** Restricts application features based on user roles.
- **Product Management:** Manage product information and inventory records.
- **Transaction Management:** Maintain records of inventory-related transactions.
- **Database Integration:** Store and manage application data using SQLite and SQLAlchemy.
- **Web Interface:** Browser-based interface for interacting with the system.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | Flask-Login |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git and GitHub |

## Project Architecture

The application follows a modular structure that separates its primary responsibilities:

- **Frontend:** Handles the user interface and user interactions.
- **Backend:** Processes requests, executes application logic, and manages workflows.
- **Database:** Stores user, product, and transaction information.
- **Authentication & Authorization:** Manages user sessions and role-based access.

## Getting Started

### Prerequisites

- Python 3.x
- Git
- A code editor such as Visual Studio Code

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gh-rohit07/ISMS.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ISMS
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```cmd
   venv\Scripts\activate
   ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application using the project's configured entry point.

   Refer to the application source code for the exact startup command.

## Database Models

The existing application includes the following core entities:

- **User:** Stores user account information.
- **Product:** Represents products maintained in the inventory.
- **Transaction:** Records inventory-related operations.

## Development Objectives

The current development focus includes:

- Understanding the existing MVC-style architecture and application flow.
- Studying backend routes, database models, and authentication.
- Understanding how inventory transactions affect stock records.
- Identifying bugs and improving existing functionality.
- Exploring additional features based on practical inventory management requirements.

## Repository Information

- **Repository Maintainer:** Sovan Kumar Mohapatra
- **Repository:** [ISMS](https://github.com/gh-rohit07/ISMS)
- **Original Project:**