import smtplib
import re
import socket

class EmailValidator:
    def __init__(self, smtp_user : str, smtp_port : int, sender_password: str, sender:str) -> None:
        """
        Initializes the EmailValidator object with provided SMTP server details and logs in to the SMTP server.
        
        Args:
            smtp_user (str): SMTP server host address.
            smtp_port (int): SMTP server port.
            sender_password (str): Password for the sender's email account.
            sender (str): Email address of the sender.
        """
        try:
            self.__smtp_user = smtp_user
            self.__smtp_port = smtp_port
            self.__sender_password = sender_password
            self.__sender_email = sender
            self.__email_pattern =  re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            self.__smtp_client = smtplib.SMTP(host = self.__smtp_user, port = self.__smtp_port)
            self.__smtp_client.starttls()
            self.__smtp_client.login(user =self.__sender_email, password = self.__sender_password)
        
        except smtplib.SMTPConnectError as er:
            print(f"Error connecting to smtplib {er}")
        
        except smtplib.SMTPAuthenticationError as er:
            print(f"Error authenticating to smtplib {er}")
        
        except smtplib.SMTPException as er:
            print(f"SMPTP exception: {er}")
    
    def verify_with_regex(self, email : str) -> bool:
        """
        Validates an email address using a regular expression pattern.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if the email is valid; False otherwise.
        """
        return bool(self.__email_pattern.match(email))
    
    def syntax_validator(self,email : str) -> bool:
          """
          Validates the syntax of an email address based on its structure.
        
          Args:
            email (str): The email address to validate.
        
          Returns:
            bool: True if the email syntax is valid; False otherwise.
          """
          parts = email.split('@')
          if len(parts) != 2:
               return False
            
          receipent = parts[0]
          if len(receipent) > 64:
               return False
            
          domain_name = parts[1]
          if len(domain_name) > 253:
               return False
            
          if not '.'  in domain_name:
               return False
          else:
               return True

    def check_dns(self, email : str) -> bool:
         """
          Checks the DNS resolution for the domain of the provided email address.
        
          Args:
            email (str): The email address to check DNS for.
        
          Returns:
            bool: True if DNS resolution is valid; False otherwise.
         """
         try:
             domain = email.split('@')[1]
             ip_address = socket.gethostbyname_ex(domain)[2]
             if not ip_address:
                return False
             else:
                return True
          
         except socket.gaierror as e:
               print(e)
               return False

    
    def send_mail(self, email : str) -> bool:
         """
          Send a mail to the specified email address to  verify if it is valid or not.

          Args:
            email (str): The receiver email address.
          
            Returns:
              bool: True if the email is valid, False otherwise
         """
         try:
            message = """"
                    Dear user,
                    This email is sent for verification purposes. If you did not request this verification, you can ignore this message. There is no need to reply.
                    """
            self.__smtp_client.sendmail(from_addr = self.__sender_email, to_addrs = email, msg = message)
            self.__smtp_client.quit()
            return True
         except smtplib.SMTPServerDisconnected as e:
              print(e)
              return False
         
         except (
                smtplib.SMTPAuthenticationError,
                smtplib.SMTPConnectError, 
                smtplib.SMTPDataError,
                smtplib.SMTPNotSupportedError, 
                smtplib.SMTPSenderRefused , 
                smtplib.SMTPRecipientsRefused, 
                smtplib.SMTPResponseException,
                smtplib.SMTPException
                ) as e:
              print(e)
              return False

         except Exception as e:
            print(f"Unknown error occurred {e}")
            return False
     

    def validate(self, email: str) -> bool:
        """
        Validates an email address by combining all validation methods.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid; False otherwise.
        """
        is_valid_regex = self.verify_with_regex(email)
        if not is_valid_regex:
            return False

        is_valid_syntax = self.syntax_validator(email)
        if not is_valid_syntax:
            return False

        is_valid_dns = self.check_dns(email)
        if not is_valid_dns:
            return False

        return True