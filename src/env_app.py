import os


def get_app_env():
    # Get the environment variable
    app_env = os.getenv('APP_ENV')

    # Return the environment variable
    return app_env

if __name__ == '__main__':

    # Get the environment variable
    app_env = get_app_env()

    # Print the environment variable
    print(f'APP_ENV: {app_env}')   