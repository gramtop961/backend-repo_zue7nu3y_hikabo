"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Portfolio-specific schemas

class Feedback(BaseModel):
    """
    Feedback left by visitors or clients
    Collection name: "feedback"
    """
    name: str = Field(..., description="Name of the person leaving feedback")
    message: str = Field(..., min_length=3, max_length=2000, description="Feedback message")
    rating: Optional[int] = Field(None, ge=1, le=5, description="Optional rating from 1 to 5")
    instagram: Optional[str] = Field(None, description="Instagram handle or URL of the person (optional)")
    approved: bool = Field(True, description="Whether feedback is approved to show on site")

class Photo(BaseModel):
    """
    Portfolio/gallery photo entries
    Collection name: "photo"
    """
    title: str = Field(..., description="Short title for the photo")
    image_url: str = Field(..., description="Public image URL")
    category: Optional[str] = Field(None, description="Category or tag")
    featured: bool = Field(False, description="Mark as featured for hero/gallery highlights")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
