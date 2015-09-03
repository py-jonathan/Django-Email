# It's easy to send an email in Django
Just follow these steps to send an email using your Gmail account.

### Set Enviroment Variables
Substitute the values below with you Gmail username & password
```
export EMAIL_HOST_USER=youremail@gmail.com
export EMAIL_HOST_PASSWORD=yourpassword
```

### Send Email
Start a Django shell
```
python manage.py shell
```

And send your email
```python
from sendemail.views import *
send_email_with_uuid('whoever@whatever.com')
```

### Here's how it works
These fields have been added to `settings.py`
```python
# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
```

And here's the function that sends the email
```python
from django.core.mail import EmailMessage

import uuid

# Create your views here.
def send_email_with_uuid(email_address):
    key = uuid.uuid1()
    email = EmailMessage('Your Unique Key', "Here's your unique key:\n" + str(key), to=[email_address])
    return email.send()
```
