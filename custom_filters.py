from pyrogram import filters

def button_filter(data):
    async def func(flt, client, update):
        if update.callback_query:
            return update.callback_query.data == flt.data
        return False
    return filters.create(func, data=data)