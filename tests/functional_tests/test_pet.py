import pytest
from services.petstore_service import PetStoreService


class PetClass:

    def test_get_pet(self):
        
        ### ARRANGE ###
        num_pets = 10

        ### ACT ###
        for id in range(num_pets):
            status_code, response = PetStoreService.get_pet(id)

        ### ASSERT ###
            assert response["sample_field"] == "sample_test_data"