import json
import requests


if __name__ == '__main__':
    response = requests.post('https://api.zhuangxiang.com/connect/token', data={
        'client_id': 'your app id',
        'client_secret': 'your app secret',
        'grant_type': 'password',
        'username': 'your account name(admin)',
        'password': 'your account password'
    }, cookies={
        'Abp.TenantId': 'your tenant id'
    })
    access_token = json.loads(response.text)['access_token']
    taskdata = {
        'type': 0,
        'packingCargoes': [{
            'name': 'cargo1',
            'length': 1.1,
            'width': 0.8,
            'height': 0.6,
            'weight': 0.5,
            'quantity': 99
        }],
        'packingContainers': [{
            'name': "20ft",
            'InnerX': 2.35,
            'InnerY': 2.38,
            'InnerZ': 5.89,
            'Maxload': 21000
        }],
        'interimContainers': [],
        'loadingOptions': {},
        'interimOptions': {},
        'predefinedModels': [],
        'pointedContainers': [],
        'skuCargoes': []
    }
    r = requests.post('https://openapi.zhuangxiang.com/OptimizeLoadingTask', data=json.dumps({'taskData': taskdata}), headers={
        'Authorization': 'bearer ' + access_token,
        'content-type': 'application/json'
    })
    print(r.text)
