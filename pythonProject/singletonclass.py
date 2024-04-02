import json

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.config = cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        with open("config.json", "r") as file:
            return json.load(file)

    def get_config(self):
        return self.config

# Example usage
if __name__ == "__main__":
    # Create two instances of Singleton
    singleton1 = Singleton()
    singleton2 = Singleton()

    # They are the same instance
    print(singleton1 is singleton2)  # Output: True

    # Accessing configuration
    print(singleton1.get_config())  # Output: Contents of config.json
