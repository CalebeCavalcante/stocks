import requests
import json

class Curl:
    
    def get(self, url, headers, params):
        
        try:
          
            response = requests.get(url, headers=headers, params=params)
             
            if response.status_code > 308 : raise Exception("Falha ao buscar os dados. StatusCode: "+ response.status_code)

            return response
            
        except Exception as e:
            raise e
    
    def post(self, url, headers, params):

        try:
            # Exemplo: params = {'some': 'data'}
            response = requests.post(url, data=json.dumps(params), headers=headers)
            
            if response.status_code > 308 : raise Exception("Falha ao buscar os dados. StatusCode: "+ response.status_code)

            return response
            
        except Exception as e:
            raise e