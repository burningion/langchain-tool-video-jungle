from langchain_core.tools import tool
from typing import Annotated, List

from videojungle import ApiClient
import os

VJ_API_KEY = os.environ.get("VJ_API_KEY") 

if VJ_API_KEY is None:
    raise ValueError("VJ_API_KEY environment variable is not set")

vj = ApiClient(VJ_API_KEY)

@tool
def search_videos(query: str) -> List[Annotated[dict, "video"]]:
    return vj.video_files.search(query)
