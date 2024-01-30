import requests

class PetStoreService:

    base_url = 'https://petstore.swagger.io'

    @staticmethod
    def get_pet(pet_id:int) -> str:
        """
        Send a get request to petstore.swagger.io/v2/pet + pet_id
        :param pet_id: integer of a pet ID
        :return: Status code and body of valid identifying fields for the pet ID requested
        """
        status,response = requests.get(f'{PetStoreService.base_url}/v2/pet/{pet_id}')
        return status, response
    
# if __name__ == "__main__":
    
#     status, response = PetStoreService.get_pet(9)
#     print(status)