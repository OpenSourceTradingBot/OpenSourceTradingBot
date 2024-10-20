from sqlalchemy import Column, Integer, DateTime, DECIMAL, BigInteger, ForeignKey
from utils.database import Base

class Market(Base):
    __tablename__ = 'market'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbols.id'))
    price_change = Column(DECIMAL(30,10))
    price_change_percent = Column(DECIMAL(30,10))
    weighted_avg_price = Column(DECIMAL(30,10))
    prev_close_price = Column(DECIMAL(30,10))
    last_price = Column(DECIMAL(30,10))
    last_qty = Column(DECIMAL(30,10))
    bid_price = Column(DECIMAL(30,10))
    bid_qty = Column(DECIMAL(30,10))
    ask_price = Column(DECIMAL(30,10))
    ask_qty = Column(DECIMAL(30,10))
    open_price = Column(DECIMAL(30,10))
    high_price = Column(DECIMAL(30,10))
    low_price = Column(DECIMAL(30,10))
    volume = Column(DECIMAL(30,10))
    quote_volume = Column(DECIMAL(30,10))
    open_time = Column(BigInteger)
    close_time = Column(BigInteger)
    first_id = Column(BigInteger)
    last_id = Column(BigInteger)
    count = Column(BigInteger)
    created_at = Column(DateTime)


