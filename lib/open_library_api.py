import requests
import json


class Search:

    def get_search_results(self):
        # Specify the search term (the lord of the rings)
        search_term = "the lord of the rings"
        # Replaces every space in the search term with + signs to make suitable for inclusions in the URL
        search_term_formatted = search_term.replace(" ", "+")
        # Specifies the field to be included in the search results
        fields = ["title","author_name"]
        # formats the list into a comma separated string.
        # output: "title, author_name"
        # Convert the fileds into comma separated sting.
        fields_formatted = ",".join(fields)
        # Specifies the maximum amount of serach results to return, 1 in this case.
        limit = 1
        # The url endpoint assigned to the variable URL
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        # Create a response object. Send the request to the url using the get method defined in the requests library.
        response = requests.get(URL)
        # return the content of the response
        return response.content

    def get_search_results_json(self):
        # Specifies the search term (the lord of the rings).
        search_term = "the lord of the rings"
        # Replace every space in the search term with a + sign to make suitable for inclusions in the URL
        search_term_formatted= search_term.replace(" ", "+")
        # Specifies the field to be included in the search results
        fields = ["title", "author_name"]
        # Convert the fileds into comma separated sting.
        fields_formatted = ",".join(fields)
        # Specifies the maximum amount of serach results to return, 1 in this case.
        limit = 1
        # The url endpoint assigned to the variable URL
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        # Print the URL for debugging purposes.
        print(URL)
        # Create a response object. Send the request to the url using the get method defined in the requests library.
        response = requests.get(URL)
        # Converts the response content from JSON format to python dictionary 
        return response.json()
    
# Create an instance of the Search class and call the method get_search_results_json on it.
results_json = Search().get_search_results_json()
# This function from the json module converts Python objects into JSON format.
# This indent parameter specifies the number of spaces to use for indentation in the JSON output, making it more human-readable.
print(json.dumps(results_json, indent=4))
# results = Search().get_search_results()
# print(results)
