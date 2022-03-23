import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder



class PetFriends:
    def __init__(self):
        # URL
        self.base_url = "https://petfriends1.herokuapp.com/"


    def get_api_key (self, email, password):
        # получаем ключ пользователя
        headers ={
            'email': email,
            'password': password}

        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try :
            result = res.json()
        except:
            result = res.text
        return status, result



    def get_api_pet (self, auth_key: json, filter):
        # получаем id питомца
        header = {'auth_key': auth_key['key']}
        filter = {'filter' : filter}

        res = requests.get(self.base_url+'api/pets',headers=header, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def post_api_pets_without_photo(self, auth_key: json, name: str, animal_type: str,
                    age: str):
        # добавление питомца без фотографии
        header = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}

        res = requests.post(self.base_url+'api/create_pet_simple', headers=header, data = data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def delete_api_pets(self, auth_key: json, pet_id):
        #удаление питомца
        header = {'auth_key': auth_key['key']}


        res = requests.delete(self.base_url+'api/pets/'+pet_id, headers=header)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def put_api_pets(self,  auth_key: json, pet_id, name: str, animal_type: str, age: str):
        #добавление информации о питомце
        header = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=header, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        #добавляем питомца с фото

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
