import bot.handlers.handlers_additional.commands as commands
import bot.handlers.handlers_additional.commands_for_admin as commands_for_admin
import bot.handlers.handlers_additional.info as info
import bot.handlers.handlers_additional.openai as openai

sc = '/'

command_handlers = {
    f'{sc}helpAll': [info.help, openai.help, commands.help, commands_for_admin.help],
    f'{sc}hall': [info.help, openai.help, commands.help, commands_for_admin.help],

    # info
    f'{sc}help': [info.help],
    f'{sc}h': [info.help],

    f'{sc}info': [info.info],
    f'{sc}i': [info.info],

    # openai
    f'{sc}helpOpenai': [openai.help],
    f'{sc}ho': [openai.help],

    f'{sc}request': [openai.request_in_openai],
    f'{sc}r': [openai.request_in_openai],

    f'{sc}generate_image': [openai.generate_image],
    f'{sc}gi': [openai.generate_image],

    # commands
    f'{sc}helpCommands': [commands.help],
    f'{sc}hc': [commands.help],

    f'{sc}pingAll': [commands.participant_notifications],
    f'{sc}pal': [commands.participant_notifications],
    '@all': [commands.participant_notifications],

    f'{sc}pingAdmins': [commands.administration_notifications],
    f'{sc}paa': [commands.administration_notifications],
    '@admins': [commands.administration_notifications],

    # commands for admin
    f'{sc}helpAdmin': [commands_for_admin.help],
    f'{sc}ha': [commands_for_admin.help],

    f'{sc}setNotify': [commands_for_admin.set_permission_to_notify_users],
    f'{sc}sn': [commands_for_admin.set_permission_to_notify_users],

    f'{sc}notifyChat': [commands_for_admin.send_chat_message],
    f'{sc}nc': [commands_for_admin.send_chat_message]
}
