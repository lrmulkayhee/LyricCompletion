# Lyric Completion Project

This project uses speech recognition to capture a lyric and then completes the lyric using the Genius API.

## Setup

To set up the project, follow these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies by running the following command in the terminal:
   ```bash
   pip install -r requirements.txt
   ```

## Description

This repository contains a project that aims to complete lyrics using speech recognition and the Genius API.

## Installation

To install and set up the project, please follow these instructions:

1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/LyricCompletion.git
   cd LyricCompletion
   ```
2. Create a virtual environment and activate it.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the project dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application
   ```bash
   python3 main.py
   ```

## Usage

1. Run the application
   ```bash
   python3 main.py
   ```
2. Interact with the application
   * Speech Recognition: Speak into your microphone. The application will use the       speech_recognition library to convert your speech into text.
   * Lyric Completion: The application will process the recognized text and attempt to complete the lyrics using natural language processing techniques.
   * Popup Display: The completed lyrics will be displayed in a popup window for you to view.

## Contributing

Thank you for considering contributing to LyricCompletion! We welcome contributions from the community to help improve and enhance the project. Please follow these guidelines to ensure a smooth and effective collaboration.

1. Fork the Repository
   * Navigate to the repository on GitHub.
   * Click the "Fork" button to create a copy of the repository in your GitHub account.
2. Clone the Forked Repository to your local machine
   ```bash
   git clone https://github.com/yourusername/LyricCompletion.git
   cd LyricCompletion
   ```
3. Create a new branch for your feature or bug fix
   ```bash
   git checkout -b feature-or-bugfix-name
   ```
4. Install the necessary dependencies
5. Make changes
   * Implement your feature or bug fix.
   * Ensure your code follows the project's coding standards and conventions.
6. Test your changes by running the application and any tests to ensure your changes work as expected
7. Commit your changes
   ```bash
   git add .
   git commit -m "Description of the feature or bug fix"
   ```
8. Push your changes to your forked repository
   ```bash
   git push origin feature-or-bugfix-name
   ```
9. Create a pull request
   * Navigate to the original repository on GitHub.
   * Click the "New Pull Request" button.
   * Select your branch and create a pull request with a clear description of your changes.
10. Review Process
   * Your pull request will be reviewed by the repository maintainers.
   * Be responsive to feedback and make any necessary changes.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more information.
