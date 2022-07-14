import random
import string
import XLUtils

test_data_file_path = r'C:\Users\david.malkhasyan\Desktop\PythonTesting\Data\Sign_In.xlsx'


def negative_random_generator_email():
    for i in range(2, 31):
        string_length = random.randint(0, 20)
        email = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + '  ' + '@' + '@@' + '.com' + '.net' + '.ru') for i in range(string_length))
        XLUtils.write_data(test_data_file_path, "Negative", i, 1, email)



def password():
    for i in range(2, 31):
        string_length = random.randint(0, 20)
        password_value = ''.join(random.choice(string.ascii_letters + ' ' + string.digits + string.punctuation + '  ' + '@' + '@@' + '.com' + '.net' + '.ru') for i in range(string_length))
        XLUtils.write_data(test_data_file_path, "Negative", i, 2, password_value)



