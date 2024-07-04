# Multiple Language Code Generator

Welcome to the Multiple Language Code Generator repository. This project leverages Flask and OpenAI to create a web application where users can generate code in various programming languages by asking questions in natural language.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The Multiple Language Code Generator is a web-based application that allows users to generate code snippets in multiple programming languages. Users can ask questions or describe the functionality they need, and the application will provide the corresponding code.

This application uses Flask for the backend server and integrates with the OpenAI API to process user queries and generate code. The frontend is built with HTML and JavaScript to provide a user-friendly interface.

## Features

- Generate code snippets in multiple programming languages
- Easy-to-use web interface
- Real-time responses to user queries
- Supports a wide range of programming languages and use cases

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kausickk/Multiple_Language_Code_generator.git
    cd Multiple_Language_Code_generator
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up OpenAI API key**:
    Ensure you have your OpenAI API key ready. Replace the placeholder in the code with your actual API key.

## Usage

To run the application locally, follow these steps:

1. **Start the Flask server**:
    ```bash
    python app.py
    ```

2. **Open your browser** and navigate to `http://127.0.0.1:5000/` to access the application.

3. **Ask questions** related to code generation and receive the corresponding code snippets.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Make your changes**
4. **Commit your changes** (`git commit -m 'Add some feature'`)
5. **Push to the branch** (`git push origin feature-branch`)
6. **Open a pull request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
