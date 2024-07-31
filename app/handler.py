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
                # Define the inline keyboard with the options to confirm or decline
                start_buttons = InlineKeyboardMarkup(
                    inline_keyboard=[[
                        InlineKeyboardButton(text="✅ Sim", callback_data="Sim"),
                        InlineKeyboardButton(text="❌ Não", callback_data="Sim")
                    ]],
                    resize_keyboard=True
                )
                # Send the message asking the age
                start_message = await message.answer("Olá, você tem 18 anos de idade?",
                                     reply_markup=start_buttons)
            except Exception as error:
                # If there is an error, send a message indicating the link is invalid
                await message.answer("Erro: link inválido. Tente novamente.")
    except Exception as error:
        # If there is an error, print it
        # Print any errors that occur
        print(error)


@router.callback_query(F.data == "Sim")
async def handle_yes(callback: types.CallbackQuery):
    """
    Handle a callback query with the data "Sim".

    This function deletes the message associated with the callback query and
    sends a new message with a link to the user. The link is obtained from the
    database using the get_link() function.

    Args:
        callback (types.CallbackQuery): The callback query to handle.

    Returns:
        None
    """
    # Delete the message associated with the callback query
    await callback.message.delete()

    try:
        # Get the link from the database
        link = get_link()[0][0]

        # Create the inline keyboard markup with the "Abrir" button
        open = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Abrir", url=link)]]
        )

        # Send a new message with the link
        await callback.message.answer(
            "🎰 Comece sua jornada no mundo dos jogos.",
            reply_markup=open
        )
    except Exception as error:
        # If there is an error, send a message indicating the link is invalid
        await callback.message.answer("Erro: link inválido. Tente novamente.")

