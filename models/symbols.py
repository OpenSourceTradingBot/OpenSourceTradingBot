from sqlalchemy import Column, Integer, String, DateTime
from utils.database import Base
from sqlalchemy.orm import relationship

class Symbols(Base):
    __tablename__ = 'symbols'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    trades = relationship("Trades", back_populates="symbol_ref")



