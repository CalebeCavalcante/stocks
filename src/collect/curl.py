import requests

class Curl:
    
    def get(self, url, headers, params):
        
        try:
          
            response = requests.get(url, headers=headers, params=params)
             
            if response.status_code > 308 : raise Exception("Falha ao buscar os dados. StatusCode: "+ response.status_code)

            return response
            
        except Exception as e:
            raise e