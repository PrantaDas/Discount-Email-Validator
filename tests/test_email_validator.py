import unittest
from validator.email_validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.email_validator = EmailValidator(smtp_user='your_user', smtp_port='your_port', sender_password='your_password',sender='sender_email')
    
    def test_regex(self):
        self.assertTrue(self.email_validator.verify_with_regex('janedoe@gmail.com'))
        self.assertFalse(self.email_validator.verify_with_regex('abdfdf-@g'))
    

    def test_syntaxValidator(self):
        self.assertTrue(self.email_validator.syntax_validator('janedoe@gmail.com'))
        self.assertFalse(self.email_validator.syntax_validator('abdfdf-@g'))


    def test_dns_validator(self):
        self.assertTrue(self.email_validator.check_dns('janedoe@gmail.com'))
        self.assertFalse(self.email_validator.check_dns('abdfdf-@g'))
        
    def test_send_email(self):
        self.assertTrue(self.email_validator.send_mail('janedoe@gmail.com'))
        self.assertFalse(self.email_validator.send_mail('abdfdf-@g'))


if __name__ == '__main__':
    unittest.main()