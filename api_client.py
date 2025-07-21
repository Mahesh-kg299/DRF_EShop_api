from requests import api
import json

class APIClient():
    def __init__(self, url, token=None):
        self.url = url
        self.token = token
    

    def get_url(self, page=None):
        if not page:
            return self.url
        else:
            return f'{self.url}?page={page}'

    def list(self, page=None):
        url = self.get_url(page)
        response = api.get(url)
        # pretty_json  = json.dumps(response.json(), indent=4)
        print(response.text)

    def detail(self, pk):
        new_url = f'{self.url}{pk}/'
        response = api.get(new_url)
        print(response.text)

    def post(self, data=None):
        if not data:
            response = api.post(self.url)
            print(response.text)
            return

        headers = {'Content-Type': 'application/json'}
        response = api.post(self.url, json=data, headers=headers)
        print(response.text)

    
    def post_form(self, data):
        response = api.post(self.url, data=data)
        print(response.text)

    def update(self, data):
        response = api.put(self.url, json=data)
        print(response.text)

    def post_auth(self, data=None):
        if not data:
            header = {'Authorization': f'Token {self.token}'}
            response = api.post(self.url, headers=header)
        header = {'Authorization': f'Token {self.token}'}
        response = api.post(self.url, json=data, headers=header)
        print(response.text)
    
    def delete(self, item_id):
        api.delete(f'{self.url}{item_id}/')

token = '1a3b68963ddaf778908ad1f917b089acbfb640a1'


productClient = APIClient('http://127.0.0.1:8000/api/products/')
brandClient = APIClient('http://127.0.0.1:8000/api/brands/')
categoryClient = APIClient('http://127.0.0.1:8000/api/categories/')
subCategoryClient = APIClient('http://127.0.0.1:8000/api/sub_categories/')
# productClient.post(
#     {
#         "product_id": "",
#         "name": "Galaxy S25",
#         "price": 70000,
#         "category": 1,
#         "sub_category": 2,
#         "brand": 1,
#         "release_year": "2025",
#         "in_stock": True
#     }
# )

# productClient.list()
# brandClient.list()
# brandClient.detail('samsung')
# brandClient.delete(1)
# items = ['car', 'truck', 'suv', 'bus', 'bike']
# for item in items:
#     subCategoryClient.post({
#         'name': item,
#         'category': 2
#     })