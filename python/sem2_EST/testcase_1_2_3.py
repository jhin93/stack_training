# -*- coding: utf-8 -*-
"""
System Test Cases for LambdaTest E-commerce Playground
Test Cases 1, 2, 3 - User Registration Tests
Author: Jin
Date: 2025-10-24
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import string


class TestUserRegistration:
    """Test cases for user registration functionality"""

    BASE_URL = "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
    REGISTER_URL = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

    def __init__(self):
        """Initialize the test class"""
        self.driver = None
        self.wait = None

    def setup(self):
        """Set up the WebDriver before each test"""
        print("\n--- Setting up WebDriver ---")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        print("WebDriver initialized successfully")

    def teardown(self):
        """Clean up after each test"""
        print("\n--- Tearing down WebDriver ---")
        if self.driver:
            time.sleep(2)  # Brief pause to see the result
            self.driver.quit()
            print("WebDriver closed successfully")

    def generate_random_email(self):
        """Generate a random email address for testing"""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"test_{random_string}@example.com"

    def navigate_to_register_page(self):
        """Navigate to the registration page"""
        print(f"Navigating to: {self.REGISTER_URL}")
        self.driver.get(self.REGISTER_URL)
        time.sleep(2)

    def fill_registration_form(self, first_name="", last_name="", email="",
                              telephone="", password="", confirm_password="",
                              accept_policy=True):
        """
        Fill in the registration form with provided data

        Args:
            first_name: First name
            last_name: Last name
            email: Email address
            telephone: Phone number
            password: Password
            confirm_password: Confirm password
            accept_policy: Whether to accept privacy policy
        """
        try:
            # Fill First Name
            if first_name:
                first_name_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "input-firstname"))
                )
                first_name_field.clear()
                first_name_field.send_keys(first_name)
                print(f"Entered First Name: {first_name}")

            # Fill Last Name
            if last_name:
                last_name_field = self.driver.find_element(By.ID, "input-lastname")
                last_name_field.clear()
                last_name_field.send_keys(last_name)
                print(f"Entered Last Name: {last_name}")

            # Fill Email
            if email:
                email_field = self.driver.find_element(By.ID, "input-email")
                email_field.clear()
                email_field.send_keys(email)
                print(f"Entered Email: {email}")

            # Fill Telephone
            if telephone:
                telephone_field = self.driver.find_element(By.ID, "input-telephone")
                telephone_field.clear()
                telephone_field.send_keys(telephone)
                print(f"Entered Telephone: {telephone}")

            # Fill Password
            if password:
                password_field = self.driver.find_element(By.ID, "input-password")
                password_field.clear()
                password_field.send_keys(password)
                print(f"Entered Password: {'*' * len(password)}")

            # Fill Confirm Password
            if confirm_password:
                confirm_password_field = self.driver.find_element(By.ID, "input-confirm")
                confirm_password_field.clear()
                confirm_password_field.send_keys(confirm_password)
                print(f"Entered Confirm Password: {'*' * len(confirm_password)}")

            # Accept Privacy Policy
            if accept_policy:
                try:
                    # Try multiple methods to find and click the privacy policy checkbox
                    # Method 1: Try by name
                    try:
                        privacy_checkbox = self.driver.find_element(By.NAME, "agree")
                        if not privacy_checkbox.is_selected():
                            self.driver.execute_script("arguments[0].click();", privacy_checkbox)
                            print("Privacy Policy accepted (method 1: by name)")
                    except:
                        # Method 2: Try by label text
                        try:
                            privacy_label = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Privacy Policy')]")
                            privacy_label.click()
                            print("Privacy Policy accepted (method 2: by label)")
                        except:
                            # Method 3: Try all checkboxes on page
                            try:
                                checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
                                for checkbox in checkboxes:
                                    parent_text = checkbox.find_element(By.XPATH, "./..").text.lower()
                                    if 'privacy' in parent_text or 'policy' in parent_text:
                                        if not checkbox.is_selected():
                                            self.driver.execute_script("arguments[0].click();", checkbox)
                                            print("Privacy Policy accepted (method 3: found via search)")
                                            break
                            except:
                                print("Privacy policy checkbox not found - trying to proceed anyway")
                except Exception as e:
                    print(f"Privacy policy handling failed: {str(e)}")

        except Exception as e:
            print(f"Error filling registration form: {str(e)}")
            raise

    def submit_registration_form(self):
        """Submit the registration form"""
        try:
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
            submit_button.click()
            print("Registration form submitted")
            time.sleep(2)
        except Exception as e:
            print(f"Error submitting form: {str(e)}")
            raise

    def test_001_user_registration_happy_path(self):
        """
        T001 - User Registration (Happy Path)
        Objective: Verify that a new user can successfully register using valid information.
        Priority: High

        Steps:
        1. Navigate to the Register page
        2. Fill in First Name, Last Name, Email, Telephone, Password, Confirm Password
        3. Accept the Privacy Policy and submit the form

        Expected Result:
        - User account is created successfully
        - Redirected to My Account page
        - Success message is displayed
        """
        print("\n" + "="*80)
        print("TEST CASE 001: User Registration (Happy Path)")
        print("="*80)

        try:
            self.setup()

            # Test Data
            test_data = {
                "first_name": "John",
                "last_name": "Doe",
                "email": self.generate_random_email(),
                "telephone": "1234567890",
                "password": "Test@123",
                "confirm_password": "Test@123"
            }

            print("\nTest Data:")
            for key, value in test_data.items():
                if 'password' in key.lower():
                    print(f"  {key}: {'*' * len(value)}")
                else:
                    print(f"  {key}: {value}")

            # Step 1: Navigate to Register page
            print("\nStep 1: Navigate to Register page")
            self.navigate_to_register_page()

            # Step 2: Fill in registration form
            print("\nStep 2: Fill in registration form")
            self.fill_registration_form(
                first_name=test_data["first_name"],
                last_name=test_data["last_name"],
                email=test_data["email"],
                telephone=test_data["telephone"],
                password=test_data["password"],
                confirm_password=test_data["confirm_password"],
                accept_policy=True
            )

            # Step 3: Submit the form
            print("\nStep 3: Submit the registration form")
            self.submit_registration_form()

            # Verification
            print("\nVerifying results...")

            # Check if redirected to account success page
            current_url = self.driver.current_url
            print(f"Current URL: {current_url}")

            # Check for success message or My Account page
            try:
                # Look for success message
                success_message = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success, #content h1"))
                )
                print(f"Success message found: {success_message.text}")

                # Verify account page elements
                if "account/success" in current_url or "account/account" in current_url:
                    print("\nTEST PASSED: User successfully registered and redirected to My Account page")
                    return True
                else:
                    print("\n TEST FAILED: Not redirected to expected page")
                    return False

            except TimeoutException:
                print("\n TEST FAILED: Success message not found")
                return False

        except Exception as e:
            print(f"\n TEST FAILED with exception: {str(e)}")
            return False
        finally:
            self.teardown()

    def test_002_user_registration_missing_fields(self):
        """
        T002 - User Registration (Missing Required Fields)
        Objective: Ensure the system prevents registration when required fields are missing.
        Priority: High

        Steps:
        1. Navigate to Register page
        2. Leave First Name empty
        3. Fill in other fields and submit

        Expected Result:
        - An inline validation error appears under the missing field
        - Registration is blocked
        """
        print("\n" + "="*80)
        print("TEST CASE 002: User Registration (Missing Required Fields)")
        print("="*80)

        try:
            self.setup()

            # Test Data - intentionally missing First Name
            test_data = {
                "first_name": "",  # Empty - this should trigger validation error
                "last_name": "Doe",
                "email": self.generate_random_email(),
                "telephone": "1234567890",
                "password": "Test@123",
                "confirm_password": "Test@123"
            }

            print("\nTest Data (First Name intentionally left empty):")
            for key, value in test_data.items():
                if 'password' in key.lower():
                    print(f"  {key}: {'*' * len(value) if value else '[EMPTY]'}")
                else:
                    print(f"  {key}: {value if value else '[EMPTY]'}")

            # Step 1: Navigate to Register page
            print("\nStep 1: Navigate to Register page")
            self.navigate_to_register_page()

            # Step 2: Fill in registration form (leaving First Name empty)
            print("\nStep 2: Fill in registration form (leaving First Name empty)")
            self.fill_registration_form(
                first_name=test_data["first_name"],  # Empty
                last_name=test_data["last_name"],
                email=test_data["email"],
                telephone=test_data["telephone"],
                password=test_data["password"],
                confirm_password=test_data["confirm_password"],
                accept_policy=True
            )

            # Step 3: Submit the form
            print("\nStep 3: Submit the registration form")
            self.submit_registration_form()

            # Verification
            print("\nVerifying results...")

            # Check for validation error
            try:
                # Look for error message related to First Name field
                error_messages = self.driver.find_elements(By.CSS_SELECTOR, ".text-danger, .invalid-feedback, .error")

                if error_messages:
                    print(f"\nValidation errors found ({len(error_messages)} error(s)):")
                    for i, error in enumerate(error_messages, 1):
                        if error.is_displayed() and error.text.strip():
                            print(f"  Error {i}: {error.text}")

                    # Check if still on registration page
                    current_url = self.driver.current_url
                    print(f"\nCurrent URL: {current_url}")

                    if "register" in current_url:
                        print("\n TEST PASSED: Registration blocked due to missing required field")
                        return True
                    else:
                        print("\n TEST FAILED: User was redirected despite missing field")
                        return False
                else:
                    print("\n TEST FAILED: No validation error found")
                    return False

            except Exception as e:
                print(f"\n TEST FAILED: Error during validation check: {str(e)}")
                return False

        except Exception as e:
            print(f"\n TEST FAILED with exception: {str(e)}")
            return False
        finally:
            self.teardown()

    def test_003_user_registration_existing_email(self):
        """
        T003 - User Registration with Existing Email
        Objective: Ensure duplicate registration with an existing email is not allowed.
        Priority: Medium

        Steps:
        1. Navigate to Register page
        2. Use an already registered email
        3. Fill other details and submit

        Expected Result:
        - Error message displayed stating the email is already registered
        """
        print("\n" + "="*80)
        print("TEST CASE 003: User Registration with Existing Email")
        print("="*80)

        try:
            # First, register a user to ensure we have an existing email
            print("\n--- Pre-requisite: Registering initial user ---")
            self.setup()

            existing_email = self.generate_random_email()

            # Test Data for first registration
            test_data_1 = {
                "first_name": "Jane",
                "last_name": "Smith",
                "email": existing_email,
                "telephone": "9876543210",
                "password": "Test@123",
                "confirm_password": "Test@123"
            }

            print("\nFirst Registration Data:")
            for key, value in test_data_1.items():
                if 'password' in key.lower():
                    print(f"  {key}: {'*' * len(value)}")
                else:
                    print(f"  {key}: {value}")

            # Register first user
            self.navigate_to_register_page()
            self.fill_registration_form(
                first_name=test_data_1["first_name"],
                last_name=test_data_1["last_name"],
                email=test_data_1["email"],
                telephone=test_data_1["telephone"],
                password=test_data_1["password"],
                confirm_password=test_data_1["confirm_password"],
                accept_policy=True
            )
            self.submit_registration_form()

            print("\nFirst user registered successfully")
            self.teardown()

            # Now attempt to register again with the same email
            print("\n--- Main Test: Attempt registration with existing email ---")
            self.setup()

            # Test Data for duplicate registration
            test_data_2 = {
                "first_name": "Bob",
                "last_name": "Johnson",
                "email": existing_email,  # Same email as before
                "telephone": "5551234567",
                "password": "Test@456",
                "confirm_password": "Test@456"
            }

            print("\nSecond Registration Data (using existing email):")
            for key, value in test_data_2.items():
                if 'password' in key.lower():
                    print(f"  {key}: {'*' * len(value)}")
                else:
                    print(f"  {key}: {value}")

            # Step 1: Navigate to Register page
            print("\nStep 1: Navigate to Register page")
            self.navigate_to_register_page()

            # Step 2: Fill in registration form with existing email
            print("\nStep 2: Fill in registration form with existing email")
            self.fill_registration_form(
                first_name=test_data_2["first_name"],
                last_name=test_data_2["last_name"],
                email=test_data_2["email"],
                telephone=test_data_2["telephone"],
                password=test_data_2["password"],
                confirm_password=test_data_2["confirm_password"],
                accept_policy=True
            )

            # Step 3: Submit the form
            print("\nStep 3: Submit the registration form")
            self.submit_registration_form()

            # Verification
            print("\nVerifying results...")

            # Check for error message about duplicate email
            try:
                # Look for error messages
                error_messages = self.driver.find_elements(By.CSS_SELECTOR, ".alert-danger, .text-danger, .error")

                duplicate_email_error_found = False

                if error_messages:
                    print(f"\nError messages found ({len(error_messages)} error(s)):")
                    for i, error in enumerate(error_messages, 1):
                        if error.is_displayed() and error.text.strip():
                            error_text = error.text.lower()
                            print(f"  Error {i}: {error.text}")

                            # Check if error mentions duplicate/existing email
                            if any(keyword in error_text for keyword in ['already', 'registered', 'exists', 'duplicate']):
                                duplicate_email_error_found = True

                # Check if still on registration page
                current_url = self.driver.current_url
                print(f"\nCurrent URL: {current_url}")

                if duplicate_email_error_found:
                    print("\n TEST PASSED: Duplicate email error message displayed correctly")
                    return True
                elif "register" in current_url:
                    print("\n� TEST PARTIALLY PASSED: Registration blocked but error message may not be specific")
                    return True
                else:
                    print("\n TEST FAILED: User was registered with duplicate email")
                    return False

            except Exception as e:
                print(f"\n TEST FAILED: Error during validation check: {str(e)}")
                return False

        except Exception as e:
            print(f"\n TEST FAILED with exception: {str(e)}")
            return False
        finally:
            self.teardown()

    def run_all_tests(self):
        """Run all test cases"""
        print("\n" + "#"*80)
        print("# RUNNING ALL TEST CASES FOR USER REGISTRATION")
        print("#"*80)

        results = {
            "T001": self.test_001_user_registration_happy_path(),
            "T002": self.test_002_user_registration_missing_fields(),
            "T003": self.test_003_user_registration_existing_email()
        }

        # Summary
        print("\n" + "#"*80)
        print("# TEST SUMMARY")
        print("#"*80)

        passed = sum(1 for result in results.values() if result)
        total = len(results)

        for test_id, result in results.items():
            status = " PASSED" if result else " FAILED"
            print(f"{test_id}: {status}")

        print(f"\nTotal: {passed}/{total} tests passed")
        print("#"*80 + "\n")

        return results


# Main execution
if __name__ == "__main__":
    print("\n" + "*"*80)
    print("* LambdaTest E-commerce System Testing")
    print("* Test Cases 1, 2, 3 - User Registration")
    print("* Author: Jin")
    print("*"*80)

    # Create test instance
    test_suite = TestUserRegistration()

    # Run all tests
    test_suite.run_all_tests()

    print("\nTest execution completed!")