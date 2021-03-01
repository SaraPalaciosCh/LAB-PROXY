import requests
class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object = self.instance
        if object.language == "ita" or object.language == "jpn":
            print("Proxy actuando...")
            response = requests.get(f"https://restcountries.eu/rest/v2/lang/{object.language}")
            print(
                response.content
            )
            return True

        return False
