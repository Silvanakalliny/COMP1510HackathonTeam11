import requests


def main():
    pass


def definition_and_example(word: str) -> tuple or str:
    # ID and KEY are needed for authentication
    my_id = "67421323"
    my_key = "427d2d5a8f8aab43d83284acf09cfa3f"
    # try making requests to the API
    try:
        response = requests.get(f"https://od-api.oxforddictionaries.com/api/v2/entrie" +
                                f"s/en-us/{word}", headers={'app_id': my_id, 'app_key': my_key})
        response.raise_for_status()
        # Get access to the word's definition and example
        access_word_information = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]
        # Get access to the definition
        definition = access_word_information['definitions'][0]
        # Get access to the example
        an_example = access_word_information['examples'][0]['text']
        # Return the definition and the example
        return definition, an_example
    # Catch the Error if the word dose not exist and return a helping message
    except requests.exceptions.HTTPError:
        help_message = "!!! There is no such a word"
        return help_message
