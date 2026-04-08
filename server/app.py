import uvicorn
from api.server import app

def main(host: str = "0.0.0.0", port: int = 7860):
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()
