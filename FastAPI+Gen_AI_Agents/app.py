from workflow import chain
from fastapi import FastAPI,Path,HTTPException,Query


app=FastAPI(title="Deep Research AI",
    description="Multi-Agent Deep Research Platform")


@app.get("/")
def home():
    return {"message":"welcome to our deep searching platform"}

@app.get("/search")
def search(message: str = Query(..., description="Enter your research topic")):
    try:
        result = chain.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            },
            config={"recursion_limit": 50}
        )
        return {
            "query": message,
            "result": result["messages"][-1].content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)