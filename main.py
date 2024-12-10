import redis

# Redis 서버에 연결
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Redis에 데이터 저장
r.set("greeting", "Hello, Redis!")

# Redis에서 데이터 가져오기
greeting = r.get("greeting")
print(f"Greeting from Redis: {greeting}")
