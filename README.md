# social media backened


# Social Media API

This is a RESTful API for a social media application built with Flask-Restx. It allows users to interact with the system by performing CRUD operations on users, friendships, and follows.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kipkirui63/social-media-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd social-media-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the environment:

    - Rename `.env.example` to `.env`.
    - Update the configuration variables in the `.env` file as needed.

5. Run the application:

    ```bash
    python app.py
    ```

## Usage

### Endpoints

- **/users**: Perform CRUD operations on users.
- **/friendships**: Perform CRUD operations on friendships.
- **/follows**: Perform CRUD operations on follows.

For detailed information on each endpoint and the expected request/response formats, please refer to the API documentation.

### API Documentation

The API documentation is generated dynamically using Swagger UI. Once the application is running, you can access the API documentation at `http://localhost:5555/api/doc`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

