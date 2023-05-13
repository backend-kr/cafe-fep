# cafe_info_kafka_producer_example.py
from confluent_kafka import Producer
import json

conf_producer = {
    'bootstrap.servers': '127.0.0.1:29092',
}

producer = Producer(conf_producer)
topic = 'cafe-info'

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce_cafe_infos(topic, cafe_infos):
    for cafe_info in cafe_infos:
        producer.produce(topic, json.dumps(cafe_info), callback=delivery_report)
    producer.flush()

if __name__ == '__main__':
    cafe_infos = [
        {
            "cafe_id": "상암동",
            "menu_info": "그릴드 슈림프 웜볼 14,500 | 클램차우더 6,000 | 토마토비프스튜 14,500 | 비프플레이트 16,500 | 치킨 플레이트 14,500 | 연어포케 16,500 | 착즙주스(케일/당근/비트) 7,000",
            "tel": "02-333-1281",
            "thumUrls": [
                "https://ldb-phinf.pstatic.net/20200427_62/1587954805108eXAsz_JPEG/Ml3aW1u2mr2wDFxPh0nG9TfQ.JPG.jpg",
                "https://ldb-phinf.pstatic.net/20200427_35/1587954751192jEUu7_JPEG/1mt1XEpWwprO051fIF0CwSBM.JPG.jpg",
                "https://ldb-phinf.pstatic.net/20200427_35/1587954750568VWiid_JPEG/fVYC-P3Zzwi3LsyOBOfUy4Hg.JPG.jpg"
            ],
            "title": "크리스피프레시 합정점",
            "address": "서울특별시 마포구 상암동 473 딜라이트스퀘어 2차 지하1층",
            "road_address": "서울특별시 마포구 월드컵로3길 14 딜라이트스퀘어 2차 지하1층",
            "business_hours": "202304291100~202304292100",
            "latitude": "37.5509348",
            "longitude": "126.9119694",
            "home_page": ""
        },
        # 다른 카페 정보를 여기에 추가하세요.
    ]
    produce_cafe_infos(topic, cafe_infos)
