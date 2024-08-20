from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException


from config.database import accounts_collection
from model.hashing import Hash

class AccountModel(BaseModel):
    # username: str
    # password: str
    def getAccounts():
        try:
            accounts = list(accounts_collection.find({}))
            for account in accounts:
                account['_id'] = str(account['_id'])
            return accounts
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database query failed: {e}")
    def getAccountByUsername(username):
        try:
            account = accounts_collection.find_one({"username": username})
            print(account.username)
            if account:
                account['_id'] = str(account['_id'])
                return account
            else:
                raise HTTPException(status_code=404, detail="Account {username} not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Account {username} not found")
    def createAccount(account):
        try:
            # Check if the account already exists
            existing_account = accounts_collection.find_one({"username": account.username})
            if existing_account:
                print("Exist")
                raise HTTPException(status_code=400, detail="Account already exists")
            
            # Insert the new account
            hashedPass = Hash.get_password_hash(account.password)
            print("Hashed: " + hashedPass)
            result = accounts_collection.insert_one({
                "username": account.username,
                "password": hashedPass
            })
            if result.inserted_id:
                return account
            else:
                raise HTTPException(status_code=500, detail="Account creation failed")
        except Exception as e:
            print(f"Exception caught: {e}")
            raise 
    
    def deleteAccount(username):
        try:
            result = accounts_collection.delete_one({"username": username})
            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail= f"Account {username} not found")
            return {"detail": "Account deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database operation failed: {e}")
        
    def updateAccount(username, account_update):
        try:
            update_data = {k: v for k, v in account_update.dict().items() if v is not None}
            result = accounts_collection.update_one({"username": username}, {"$set": update_data})
            
            if result.matched_count == 0:
                raise HTTPException(status_code=404, detail="Account not found")
            
            # Fetch the updated account
            updated_account = accounts_collection.find_one({"username": username})
            updated_account['_id'] = str(updated_account['_id'])
            return updated_account
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database operation failed: {e}")
