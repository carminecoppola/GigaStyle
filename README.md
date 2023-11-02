# GigaStyle

GigaStyle is a web application that allows users to book appointments with their favorite barbers and hairdressers in a smart and convenient way. Users can also browse through the price list and available services offered by various barbershops and hair salons. This README provides an overview of the project, instructions on how to set it up, and highlights some of its key features.

## System Requirements

To successfully run the GigaStyle project, you need the following requirements:

- Python 3.x installed on your system.
- Flask, the Python web framework, installed. You can install it using pip:

    ```
    pip install Flask
    ```

- MongoDB installed and running on your system. Make sure you have the MongoDB Python driver installed:

    ```
    pip install pymongo
    ```

## Installation

1. Clone the GigaStyle repository to your system:

    ```
    git clone https://github.com/carminecoppola/GigaStyle.git
    ```

2. Navigate to the project directory:

    ```
    cd GigaStyle
    ```

3. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

5. Install project dependencies:

    ```
    pip install -r requirements.txt
    ```

## Configuration

1. Configure the MongoDB database:
    - Ensure that the MongoDB server is running on your system.
    - Modify the database settings in the `config.py` file to reflect your preferences.

2. Set up environment variables:
    - Create a `.env` file in the project's root directory and define the following environment variables:

    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=YourSecretKey
    MONGO_URI=YourMongoDBDatabaseURL
    ```

3. Initialize the database (this will create the necessary collections in the specified database):

    ```
    flask init-db
    ```

## Running the Project

To start the GigaStyle web server, run the following command in the project's root directory:

    ```
    flask run
    ```


The application will be available at `http://localhost:5000` in your web browser.

## Project Structure

The project's structure is organized as follows:

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates.
- `static/`: Contains CSS, JavaScript, and other static assets.
- `models.py`: Defines the data models used by the application.
- `routes/`: Contains files defining routes and application functionality.
- `config.py`: Contains application configuration variables.

## Using the Application

1. Visit the GigaStyle website and register for an account.
2. Browse services, choose a barber or hairdresser, and book an appointment.
3. Explore your user profile to manage your information and appointments.
4. For salon owners, log in to the admin panel to manage services and appointments.

## Contributing

If you would like to contribute to this project, please follow the guidelines in the `CONTRIBUTING.md` file.

## License

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file.

## Acknowledgments

Thanks to the Flask community for providing a powerful web framework. This project was inspired by the need for a convenient barber and hairdresser booking system.

## Screenshot

![HomePage](https://github.com/carminecoppola/GigaStyle/assets/74236426/a50a6fc7-12d6-4033-acf0-adf38ee9c791)

## Questions or Assistance

If you have questions or need assistance, feel free to contact us at [carminecoppola917@gmail.com](mailto:your@email.com).

---

**Note:** Please make sure your virtual environment is activated when running commands like `flask run` and `flask init-db`.
