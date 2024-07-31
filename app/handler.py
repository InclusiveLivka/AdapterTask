from aiogram import Router, types, F
from app.database.engine import add_link, get_link
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from __init__ import owned

router = Router()


@router.message()
async def handle_link(message: types.Message):
    """
    Handle a message and add a link if the user has the correct permissions.

    Args:
        message (types.Message): The message to handle.

    Returns:
        None
    """
    # Check if the user has the correct permissions and if the message is a link
    try:
        # Check if the user has the correct permissions
        if str(message.from_user.id) == str(owned) and message.text.startswith("/link"):
            # Add the link to the database
            link = message.text.replace("/link ", "")
            add_link(link)
            await message.answer("Link adicionado com sucesso!")
        else:
            # If the user does not have the correct permissions, send a message asking the age
            # Create the inline keyboard markup
            try:
                start_buttons = InlineKeyboardMarkup(
                    inline_keyboard=[[
                        InlineKeyboardButton(
                            text="Sim", url=str(get_link()[0][0])),
                        InlineKeyboardButton(text="Não", callback_data="Não")
                    ]],
                    resize_keyboard=True
                )
                # Send the message asking the age
                await message.answer("Olá, você tem 18 anos de idade?",
                                     reply_markup=start_buttons)
            except Exception as error:
                await message.answer("Erro: link inválido. Tente novamente.")
    except Exception as error:
        # Print any errors that occur
        print(error)
