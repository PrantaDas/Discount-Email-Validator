# Email Validator

## Introduction

The Email Validator is a Python script that allows you to validate email addresses using various methods, including regular expression matching, syntax checking, and DNS resolution.

## Installation

To use the Email Validator, you'll need to have Python installed. Additionally, make sure to install additional libraries.

## Usage
### Initialization
To get started, create an EmailValidator object by providing the necessary SMTP server details:
```python
from email_validator import EmailValidator

# Replace the placeholders with your SMTP server details
validator = EmailValidator(smtp_user="your_smtp_host", smtp_port="your_smtp_port", sender_password="your_password", sender="your_email@example.com")
```
### Validation methods:
The Email Validator provides three methods to validate email addresses:
1. Regular Expression matching
    ```python
    is_valid_regex = validator.verify_with_regex("example@example.com")
    ```
2. Syntax Validation
    ```python
    is_valid_syntax = validator.syntax_validator("example@example.com")
    ```
3. DNS Resolution Check
    ```python
    is_valid_dns = validator.check_dns("example@example.com")
    ```
4. Combined Validation
    ```python
    is_valid_email = validator.validate("exmaple@example.com")
    ```

## Error Handling
The script includes error handling for common exceptions, such as SMTP connection errors, authentication errors, and DNS resolution issues. If an error occurs, the script will print an error message to the console.

## Contributing
Feel free to contribute to the development of this Email Validator by submitting issues or pull requests.

### Note for myself:
 As I am still learning Python and this is my first time working with test cases, there might be suboptimal approaches or areas for improvement in the code. I welcome feedback and suggestions from the community to enhance my understanding and coding skills. Feel free to point out any mistakes or provide insights that can help me grow as a Python developer. Thank you for your understanding and support!
