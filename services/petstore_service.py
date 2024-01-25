import requests

class PetStoreService:

    base_url = 'https://petstore.swagger.io/oauth/authorize'

    def get_pet(self, pet_id):
        """
        Send a get request to petstore
        :param pet_id: integer of a pet ID
        :return: Status code and body of valid identifying fields for the pet ID requested
        """
        response = requests.get(PetStoreService.base_url, pet_id)
        return response