from utils.database import get_session
from models.symbols import Symbols
from sqlalchemy import select
from utils.logging import ExceptionLogger
from sqlalchemy.orm.exc import NoResultFound

def get_all() -> list:
    """Retrieves all symbols from the database.

    Returns:
        List[Symbols]: A list of Symbols objects.

    Raises:
        Exception: If an error occurs during the database query.
    """

    try:
        result = get_session().execute(select(Symbols))
        return result.fetchall()
    except Exception as e:
        ExceptionLogger().log_exception(e)

def get_symbol_by_id(symbol_id: int) -> Symbols:
    """
    Retrieves a symbol from the database by its ID.

    This function queries the database to find a symbol with the specified ID.
    If no symbol is found, an exception is logged, and None is returned.

    Args:
        symbol_id (int): The ID of the symbol to be retrieved.

    Returns:
        Symbols: The Symbols object corresponding to the given ID if found.

    Raises:
        NoResultFound: If no symbol is found for the provided ID.
    """
    try:
        symbol = get_session().query(Symbols).filter(Symbols.id == symbol_id).one()
        return symbol
    
    except NoResultFound as e:
        ExceptionLogger().log_exception(f"Symbol with ID {symbol_id} not found: {e}")
        raise ValueError(f"Symbol with ID {symbol_id} not found")  # Raise a specific exception
    except Exception as e:
        ExceptionLogger().log_exception(f"Error retrieving symbol with ID {symbol_id}: {e}")
        raise



