import asyncio
from rest_framework.response import Response
from .services import StoreManager

# Create your views here.

async def get_book_info(request):
    tasks = []


