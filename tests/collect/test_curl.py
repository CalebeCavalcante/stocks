from stocks.src.collect import curl

def test_curl():

    try:

        for arrTest in [["GOLL4", 'GOLL4.SA'], ["vale3", 'VALE3.SA'], ["BoVv11", 'BOVV11.SA']]:            
            
            valores = curl.extracao(arrTest[0])
            assert  len(valores) ==  3
            assert  valores[0] == arrTest[1]
            assert  isinstance(valores[1], float)
            assert  isinstance(valores[2], float)

    except Exception as e:

        print(e.args[0])
        assert False