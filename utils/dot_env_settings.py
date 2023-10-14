from dotenv import dotenv_values

def get_env_settings():
    settings =  dotenv_values(".env")
    api_key = settings.get("OPENAI_API_KEY", None)
    org_id = settings.get("OPENAI_ORG_ID", None)

    assert api_key, "OpenAI API key not found in .env file"

    return api_key, org_id