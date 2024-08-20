from pydantic import BaseModel
from typing import Optional

# Pydantic model for Account
class Account(BaseModel):
    username: str
    password: str

# Pydantic model for Account update (optional fields)
class AccountUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[int] = None