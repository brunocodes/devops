##################################
#####         venv           #####

# Run Dev #
uvicorn main:app --reload

# Exclude from OpenAPI #
@app.get("/", include_in_schema=False)
async def root():
    return {
        "website": "MySite.com",
        "Docs 1": "api.MySite.com/docs",
        "Docs 2": "api.MySite.com/redoc"
    }


##################################
#####                        #####


##################################