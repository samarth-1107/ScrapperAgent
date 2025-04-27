import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from schemas.article_schema import ArticleList

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def process_with_llm(html, instructions, truncate=False):
    if not html:
        return None
    max_len=15000
    content_to_send=html[:max_len] if truncate and len(html) > max_len else html

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role":"system",
                    "content":f"""
                    You are an expert web scraping agent and below are the steps to extract : 
                    1. title
                    2. articleUrl (absolute URL)
                    3. imageURL
                    4. excerpt
                    from this page's HTML.

                    Instructions
                    {instructions}

                    Return ONLY a JSON object matching the expected schema.
                    """
                },
                {"role":"user","content":content_to_send}
            ],
            temperature=0.1,
            response_format={"type":"json_object"}
        )

        response_content = completion.choices[0].message.content
        return ArticleList.model_validate_json(response_content)
    
    except Exception as e:
        print(f"Error in LLM processing : {e}")
        return None