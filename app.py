from public_doors_rent_manage.app import create_app
from datetime import timedelta

app = create_app()

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
app.config['SECRET_KEY'] = 'zyk2019'

if __name__ == "__main__":
    app.run()
