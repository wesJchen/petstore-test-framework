import requests

class PetStoreService:

    base_url = 'https://petstore.swagger.io'

    @staticmethod
    def get_pet(pet_id:int) -> tuple[str, dict]:
        """
        Send a get request to petstore.swagger.io/v2/pet + pet_id
        :param pet_id: integer of a pet ID
        :return: Status code and body of valid identifying fields for the pet ID requested
        """
        response = requests.get(f'{PetStoreService.base_url}/v2/pet/{pet_id}')
        status_code = response.status_code
        response_json = response.json() if response.content else {}
        return status_code, response_json
    
# if __name__ == "__main__":
    
#     status_code, response = PetStoreService.get_pet(2)
#     print(status_code)
#     print(response)
