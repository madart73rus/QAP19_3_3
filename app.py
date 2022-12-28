import requests
import json

base_url = f"https://petstore.swagger.io/v2"

# pet Everything about your Pets

# POST /pet Add a new pet to the store

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
          "id": 111,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "maddoggie1",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
data = json.dumps(data, ensure_ascii=False)
res = requests.post(base_url + '/pet', headers=headers, data=data)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())
pet_id = res.json()['id']



# PUT /pet Update an existing pet

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
          "id": 111,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "MadDog",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
data = json.dumps(data, ensure_ascii=False)
res = requests.put(base_url + '/pet', headers=headers, data=data)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# GET  /pet/findByStatus Finds Pets by status

status = 'available'
params = {'status': status}
headers = {'accept': 'application/json'}
res = requests.get(base_url + '/pet/findByStatus', headers=headers, params=params)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# GET /pet/{petId} Find pet by ID

id =str(pet_id)
res = requests.get(base_url + '/pet/' + id, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# POST /pet/{petId} Updates a pet in the store with form data


headers={'accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}
data = {
          "id": 111,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "MadDogy",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
data = json.dumps(data, ensure_ascii=False)
res  = requests.post(base_url + '/pet/' + id , headers=headers, data=data)
print('POST /pet/{petId} Updates a pet in the store with form data')
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())


# DELETE /pet/{petId} Deletes a pet

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
id =str(id)
res = requests.delete(base_url +'/pet/'+ id, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())


# store Access to Petstore orders

# POST /store/order Place an order for a pet
data = {
          "id": 0,
          "petId": 0,
          "quantity": 0,
          "shipDate": "2022-12-21T10:10:42.697Z",
          "status": "placed",
          "complete": True
        }
data = json.dumps(data, ensure_ascii=False)

res = requests.post(base_url + '/store/order', headers=headers, data=data)
orderid = res.json()['id']
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# GET /store/order/{orderId} Find purchase order by ID

id =str(orderid)
res = requests.get(base_url + '/store/order/' + id, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())


# GET /store/inventory Returns pet inventories by status

res = requests.get(base_url + '/store/inventory', headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# DELETE /store/order/{orderId} Delete purchase order by ID

id =str(orderid)
res = requests.delete(base_url + '/store/order/' + id, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# user  Operations about user

# POST  /user/createWithArray  Creates list of users with given input array

data = [
          {
            "id": 998,
            "username": "Art",
            "firstName": "Artem",
            "lastName": "",
            "email": "string@mail.ru",
            "password": "12345",
            "phone": "66-11-11",
            "userStatus": 0
          }
        ]
data = json.dumps(data, ensure_ascii=False)

res = requests.post(base_url + '/user/createWithArray', headers=headers, data=data)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# POST  /user/createWithList Creates list of users with given input array

data = [
          {
            "id": 999,
            "username": "Art1",
            "firstName": "Artem1",
            "lastName": "",
            "email": "string1@mail.ru",
            "password": "123451",
            "phone": "66-11-111",
            "userStatus": 0
          }
        ]
data = json.dumps(data, ensure_ascii=False)

res = requests.post(base_url + '/user/createWithList', headers=headers, data=data)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())


# GET /user/{username} Get user by user name
username = 'Art'
res = requests.get(base_url + '/user/' + username, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# PUT /user/{username} Updated user
data = {
            "id": 999,
            "username": "Art1",
            "firstName": "Artem1",
            "lastName": "",
            "email": "string1@mail.ru",
            "password": "123451",
            "phone": "66-11-111",
            "userStatus": 0
          }

data = json.dumps(data, ensure_ascii=False)
username = 'Art1'
res = requests.put(base_url + '/user/' + 'Art1', headers=headers, data=data)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# DELETE /user/{username} Delete user

username = 'Art'
res = requests.delete(base_url + '/user/' + username, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())



# GET /user/login Logs user into the system

username = 'ArtGS'
password = '12345'
res = requests.get(base_url + '/user/login?username=' + username + '&password=' + password, headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())


# GET /user/logout Logs out current logged in user session

res = requests.get(base_url + '/user/logout', headers=headers)
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())

# POST /user Create user

data = {
            "id": 999,
            "username": "Art1",
            "firstName": "Artem1",
            "lastName": "",
            "email": "string1@mail.ru",
            "password": "123451",
            "phone": "66-11-111",
            "userStatus": 0
          }

data = json.dumps(data, ensure_ascii=False)

res = requests.post(base_url + '/user', headers=headers, data=data)
print(base_url + '/user')
print('Статус запроса :', res.status_code)
print('Ответ сервера :', res.json())







