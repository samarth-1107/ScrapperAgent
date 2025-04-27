from pydantic import BaseModel, Field
from typing import Optional,List

class Articles(BaseModel):
    title: str = Field(...,description="Title of the article")
    article_url: str = Field(..., description="URL of article")
    image_url: Optional[str] = Field(None, description="Image URL of article")
    excerpt : Optional [str] = Field(None, description="A short excerpt of the article")

class ArticleList(BaseModel):
    article:List[Articles] = Field(..., description="A list of articles")