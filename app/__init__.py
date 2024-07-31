from aiogram import Dispatcher
from app.handler import router as handler_router


def setup_routers(dp: Dispatcher):
    """
    Set up the routers for the Dispatcher.

    Args:
        dp (aiogram.Dispatcher): The Dispatcher to set up the routers for.
    """
    # Include the handler router in the Dispatcher
    # This allows the handlers defined in app.handler to be used
    dp.include_router(handler_router)
