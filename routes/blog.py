from fastapi import APIRouter, HTTPException
from typing import List, Dict, Optional, Annotated

from model import  models
from config.database import accounts_collection


blogRouter = APIRouter()