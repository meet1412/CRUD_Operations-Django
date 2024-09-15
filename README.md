# Django CRUD Application

## Project Overview

This Django CRUD (Create, Read, Update, Delete) application is designed to manage a list of user records with basic operations. It allows users to create new records, view a list of existing records, update specific records, and delete records. The application leverages Django’s robust framework for handling web-based CRUD operations with a simple and intuitive user interface.

## Key Features

- **Create Records**: Users can submit a form to create new records with first and last names. The form data is stored in the database and can be viewed or edited later.
- **View Records**: The application provides a view that lists all the records in a tabular format. Each record can be updated or deleted from this view.
- **Update Records**: Users can modify existing records by accessing an update form pre-filled with the current details of the record. Changes are saved to the database upon submission.
- **Delete Records**: Before deleting a record, users are presented with a confirmation form displaying the record's details. This ensures that records are only deleted intentionally.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites.
- **HTML/CSS**: Standard markup and styling languages for structuring and designing web pages.

## Application Structure

- **Templates**: Includes HTML templates for creating, viewing, updating, and deleting records. Each template extends a base layout and utilizes Bootstrap for styling.
- **Views**: Handles the logic for rendering templates and processing form submissions.
- **Models**: Defines the structure of the records stored in the database.
- **URLs**: Configures the routing for different views and actions in the application.
