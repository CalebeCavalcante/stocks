from src.collect import Finance
from src.collect import Curl


def test_curl():

    try:
        
        curl = Curl()    
        response = curl.get('https://google.com', headers=None, params=None)
        assert response.status_code ==  200
        assert len(response.text) > 10
    
    except Exception as e:

        print(e.args[0])
        assert False


def test_finance():

    try:
        
        finance = Finance()

        for arrTest in [["GOLL4", 'GOLL4.SA'], ["vale3", 'VALE3.SA'], ["BoVv11", 'BOVV11.SA']]:            
            
            valores = finance.get_arr_symbol_actual_previous(arrTest[0])
            assert  len(valores) ==  3
            assert  valores[0] == arrTest[1]
            assert  isinstance(valores[1], float)
            assert  isinstance(valores[2], float)

    except Exception as e:

        print(e.args[0])
        assert False