
import os
import platform
from mediaApp.mm_app import create_app
from mediaApp.mm_app.config import ProductionConfig, DevelopmentConfig, TestingConfig

env = os.environ.get('FLASK_DEBUG', 'development')


if platform.system() == 'Windows':
    # For Windows, you may keep your certificate in C:\\Path\\To\\Certs
    ssl_context = (
        os.environ.get('WIN_PUBLIC_CERT', r"C:\Programming\Development\Certs\public.pem"),
        os.environ.get('WIN_PRIVATE_CERT', r"C:\Programming\Development\Certs\private.pem")
    )
else:
    # For Linux, you may keep your certificate in ~/path/to/certs
    ssl_context = (
        os.environ.get('LIN_PUBLIC_CERT', os.path.expanduser('~/public.pem')),
        os.environ.get('LIN_PRIVATE_CERT', os.path.expanduser('~/private.pem'))
    )


def home_test_certs():
    if os.path.exists(ssl_context[0]) and os.path.exists(ssl_context[1]):
        print("Both files exist!")
    else:
        print(f"Public cert exists: {os.path.exists(ssl_context[0])}, Private key exists: {os.path.exists(ssl_context[1])}")


# test_certs()





app = create_app(ProductionConfig)
app_test = create_app(TestingConfig)


with app.app_context():
    if __name__ == "__main__":
        if env == 'production':
            app.run(host="0.0.0.0", port=80)
            # When the app is running with Nginx and Gunicorn.
        else:
            app.run(debug=True, host="0.0.0.0", port=50511, ssl_context=ssl_context)
            # I use port 50511 because ports lower than 1024 require root privileges to use.
