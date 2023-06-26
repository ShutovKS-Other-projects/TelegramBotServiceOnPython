from bot.handlers.commands import info, openai, commands, commands_for_admin, statistics

sc = '/'
command_handlers = {
    f'{sc}helpAll': [info.help, openai.help, commands.help, commands_for_admin.help, statistics.help],

    # info
    f'{sc}help': [info.help],
    f'{sc}info': [info.info],

    # openai
    f'{sc}helpOpenai': [openai.help],
    f'{sc}request': [openai.request_in_openai],
    f'{sc}generate_image': [openai.generate_image],

    # commands
    f'{sc}helpCommands': [commands.help],
    f'{sc}pingAll': [commands.participant_notifications],
    '@all': [commands.participant_notifications],
    f'{sc}pingAdmins': [commands.administration_notifications],
    '@admins': [commands.administration_notifications],

    # commands for admin
    f'{sc}helpAdmin': [commands_for_admin.help],
    f'{sc}setNotify': [commands_for_admin.set_permission_to_notify_users],
    f'{sc}notifyChat': [commands_for_admin.send_chat_message],
    f'{sc}addUser': [commands_for_admin.add_user_in_user_table],
    f'{sc}deleteUser': [commands_for_admin.delete_user_in_user_table],

    # statistics
    f'{sc}helpStat': [statistics.help],
    f'{sc}stat': [statistics.get_stat],
    f'{sc}stat (id)': [statistics.get_stat_by_id],
    f'{sc}statAll': [statistics.get_stat_all], }
