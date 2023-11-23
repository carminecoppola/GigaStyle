# GigaStyle

GigaStyle is a web application that allows users to book appointments with their favorite barbers and hairdressers in a smart and convenient way. Users can also browse through the price list and available services offered by various barbershops and hair salons. This README provides an overview of the project, instructions on how to set it up, and highlights some of its key features.

## How to Run

Follow these steps to set up and run the GigaStyle project:

1. Clone the GigaStyle repository to your system:

    ```bash
    git clone https://github.com/carminecoppola/GigaStyle.git
    ```

2. Navigate to the project directory:

    ```bash
    cd GigaStyle
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Configure the MongoDB database:
    - Ensure that the MongoDB server is running on your system.
    - Modify the database settings in the `config.py` file to reflect your preferences.

6. Set up environment variables:
    - Create a `.env` file in the project's root directory and define the following environment variables:

    ```bash
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=YourSecretKey
    MONGO_URI=YourMongoDBDatabaseURL
    ```

7. Initialize the database (this will create the necessary collections in the specified database):

    ```bash
    flask init-db
    ```

8. To start the GigaStyle web server, run the following command in the project's root directory:

    ```bash
    flask run
    ```

The application will be available at `http://localhost:5000` in your web browser.

9. (Optional) To run the GigaStyle application via remote access:

    ```
    flask run --host=0.0.0.0 --port=8000
    ```

    Starts the Flask server by making the GigaStyle application accessible on all IP addresses on the local machine and network.

   - **_host=0.0.0.0:_** Specifies that the Flask server must be available on all IP addresses on the local machine and network. In this way, the application will be accessible from other devices on the same network.
   - **_port=8000:_** Specifies the port on which the Flask server will be listening. In your case, the application will be accessible at the IP address of the machine followed by port 8000 (for example, http://192.168.1.2:8000).

## Project Structure

The project's structure is organized as follows:

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates and JavaScript functions.
- `static/`: Contains CSS and other static assets.
- `routes/`: Contains files defining routes and application functionality.
- `config.py`: Contains application configuration variables.

## Using the Application

1. Visit the GigaStyle website and register for an account.
2. Browse services, choose a barber or hairdresser, and book an appointment.
3. Explore your user profile to manage your information and appointments.
4. For salon owners, log in to the admin panel to manage services and appointments.

## Contributing

If you would like to contribute to this project, please follow the guidelines in the `CONTRIBUTING.md` file.

## Preview

Is it possible to see a short presentation of **GigaStyle** with the features explained:

https://github.com/carminecoppola/GigaStyle/assets/74236426/24c2cb93-18ad-4531-b9aa-b6a9c2a52ec0

## Presentations

Here you can see the GigaStyle proposal and the final presentation:

- [Proposal-GigaStyle.pdf](https://github.com/carminecoppola/GigaStyle/files/13412028/Proposal-GigaStyle.pdf)

- [FinalPresentation.pdf](https://github.com/carminecoppola/GigaStyle/files/13437910/FinalPresentation.pdf)

## License

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file.

## Acknowledgments

Thanks to the Flask community for providing a powerful web framework. This project was inspired by the need for a convenient barber and hairdresser booking system.


## Questions or Assistance

If you have questions or need assistance, feel free to contact us at: [carminecoppola917@gmail.com](mailto:your@email.com)
    
---

**Note:** Please make sure your virtual environment is activated when running commands like `flask run` and `flask init-db`.
