import json
import requests


if __name__ == '__main__':
    response = requests.post('https://api.zhuangxiang.com/connect/token', data={ # URL
        'client_id': 'your app id', # 填写app-id、app-secret、账号及密码
        'client_secret': 'your app secret',
        'grant_type': 'password',
        'username': 'your account name(admin)',
        'password': 'your account password'
    }, cookies={
        'Abp.TenantId': 'your tenant id' # 设置Cookie，使用租户id
    })
    access_token = json.loads(response.text)['access_token'] # 从响应中获取access_token
    taskdata = { # 构造要计算的数据
        'type': 0,
        'packingCargoes': [{ # 货物数据
            'name': 'cargo1',
            'length': 1.1,
            'width': 0.8,
            'height': 0.6,
            'weight': 0.5,
            'quantity': 99
        }],
        'packingContainers': [{ # 容器数据
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
    r = requests.post('https://openapiv2.zhuangxiang.com/OptimizeLoadingTask', data=json.dumps({'taskData': taskdata}), headers={
        'Authorization': 'bearer ' + access_token,
        'content-type': 'application/json'
    }) # 发送请求，使用access_token进行认证，Body为要计算的数据
    print(r.text)
