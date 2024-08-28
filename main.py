from fastapi import FastAPI, Request

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

@app.get("/")
async def read_root():
    """
    루트 엔드포인트: 기본적인 환영 메시지를 반환합니다.
    """
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/process/")
async def process_message(request: Request):
    """
    /process/ 엔드포인트: 클라이언트가 보낸 user_input을 처리하고 응답을 반환합니다.
    """
    # JSON 데이터 추출
    data = await request.json()
    user_input = data.get("user_input", "")

    # 입력된 데이터를 처리하고 응답 생성
    response_text = f"Received input: {user_input}"
    
    # JSON 형식으로 응답 반환
    return {"response": response_text}

@app.get("/items")
async def get_items():
    """
    /items 엔드포인트: 간단한 아이템 리스트를 반환합니다.
    """
    items = ["item1", "item2", "item3"]
    return {"items": items}

if __name__ == "__main__":
    import uvicorn
    # FastAPI 서버 실행
    uvicorn.run(app, host="0.0.0.0", port=8000)
