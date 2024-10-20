from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from utils.database import Base
from sqlalchemy.orm import relationship

class Trades(Base):
    __tablename__ = 'trades'
    
    id = Column(Integer, primary_key=True)
    
    bot_id = Column(Integer, nullable=False)
    
    symbol_id = Column(Integer, ForeignKey('symbols.id'), nullable=False)
    
    market_id_buyin = Column(Integer, nullable=False)
    market_id_sellout = Column(Integer, nullable=True)
    
    value_buyin = Column(DECIMAL(30, 10), nullable=False)
    value_sellout = Column(DECIMAL(30, 10), nullable=True)
    
    datetime_buyin = Column(DateTime, nullable=False)
    datetime_sellout = Column(DateTime, nullable=True)
    
    percentage_difference = Column(DECIMAL(10, 10), nullable=True)
    total_percentage_change = Column(DECIMAL(10, 10), nullable=True)
    
    symbol_ref = relationship("Symbols", back_populates="trades")
