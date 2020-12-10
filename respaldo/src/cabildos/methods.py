from quickchart import QuickChart

def crearpost(id_cabildo):
    #if not realizado:
    pass

def creargrafico():
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = { 
        "type": "bar",
        "data": {
            "labels": ["Hello world", "Test"],
            "datasets": [{
                "label": "Foo",
                "data": [1, 2]
            }]
        }
    }
    return qc.get_url()

img = creargrafico()
print(img)
