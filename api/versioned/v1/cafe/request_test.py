import requests
import time



naver_url = "http://localhost:8080/api/v1/cafe/naver/"
local_url = "http://localhost:8001/api/v1/cafe/"

def process_data(json_list=None):
    for items in json_list:
        time.sleep(1)
        requests.post(local_url, json=items)

params = {
    "caller": "pcweb",
    "query": "연신내",
    "page": "1",
    "type": "all",
    "recommandation": "true",
    "latitude": "37.6943312",
    "longitude": "126.764245",
    "display_count": 50,
    "lang": "ko"
}

# 첫 번째 요청을 보냅니다.
response = requests.post(naver_url, params=params)
result = []
if response.ok:
    # 전체 페이지 수를 계산합니다.
    # for i in response.json()['result']:
    #     result.append(i['business_hours'])
    total_page = (response.json()["total_count"] // params["display_count"]) + 1

    # 모든 페이지에서 데이터를 추출합니다.
    for page in range(1, total_page + 1):
        params["page"] = page
        response = requests.post(naver_url, params=params)
        if response.ok:
            # for i in response.json()['result']:
            #     result.append(i['business_hours'])
            # 추출한 데이터를 처리합니다.
            process_data(json_list=response.json()["result"])
        # else:
            print(f"Request failed: {response.status_code}")
else:
    print(f"Request failed: {response.status_code}")


# print(result)
