import pytest
from services.petstore_service import PetStoreService


class PetClass:

    def test_pets_get_and_retrieve(self):
        
        ### ARRANGE ###
        number_of_pets = 10

        ### ACT ###
        for id in range(number_of_pets):
            status_code, response = PetStoreService.get_pet(id)

        ### ASSERT ###
            assert status_code == 200
            
            # Validate pet id matches value passed in
            assert response['id'] == id