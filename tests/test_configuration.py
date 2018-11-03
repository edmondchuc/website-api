import re
import configuration as conf
import subprocess


def test_email_sender_is_string():
    assert isinstance(conf.EMAIL_SENDER, str), f"Expected EMAIL_SENDER to be of type str, instead it is {type(conf.EMAIL_SENDER)}"


def test_email_has_value():
    assert len(conf.EMAIL_SENDER) > 0, "EMAIL_SENDER has not been assigned yet."


def test_email_is_valid(email=None):
    email = conf.EMAIL_SENDER if email is None else email
    pattern = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    result = re.search(pattern, email)
    assert result is not None, f'Email: {email} is not a valid email.'
    assert len(result.group()) == len(email), f'Email: {email} is not a valid email. Regex matched only a portion of the email.'


def test_email_list_is_set():
    assert len(conf.EMAIL_RECEIVERS) > 0, 'EMAIL_RECEIVERS list require at least one valid email.'


def test_email_list_has_valid_emails():
    for email in conf.EMAIL_RECEIVERS:
        test_email_is_valid(email)


def run():
    result = None
    try:
        result = subprocess.call('pytest tests/test_configuration.py')
    except:
        pass

    if not result:
        return True # passed
    else:
        return False # failed


if __name__ == '__main__':
    run()

