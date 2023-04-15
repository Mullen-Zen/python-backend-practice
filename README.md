# Hello, Django!

This is nothing more than ongoing practice for me to teach myself the workings of a Django-based python backend for a web server, including some light (production/development-level) database stuff. It's based off the code found [here](https://code.visualstudio.com/docs/python/tutorial-django). I'm continuously adding to it as I screw with features. Figured I'd make it public so that people would be able to see what I'm working on :3

Other referenced tutorials:

- [Django Environment Variables](https://codinggear.blog/django-environment-variables/)
- [Generating Django Secret Keys](https://codinggear.blog/django-generate-secret-key/)

## Setup

### Installing Dependencies

- First you'll need to install the required libraries - do so by running the following command:

``` {.sh}
pip install -r requirements.txt
```

### Environment Variable Creation

You'll need to create a local environment file and generate a secret key as follows:

- Run the following command or mantually create a new file at the root of the project called ".env:"

```{.sh}
cat > .env
```

- Ensuring the required libraries are installed, run the following series of commands to generate a django secret key:

```{.sh}
python3 manage.py shell
# New terminal lines should now begin with >>> 
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
# Copy the generated key, then use exit() to exit
```

- Now enter the following line into the .env file:

```{.py}
SECRET_KEY=[paste the generated secret key]
```
