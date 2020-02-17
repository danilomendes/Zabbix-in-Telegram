# -*- coding: utf-8 -*-
import os

tg_key = os.getenv(ZTG_TG_KEY, "XYZ")  # telegram bot api key

zbx_tg_prefix = os.getenv(ZTG_ZBX_TG_PREFIX, "zbxtg")  # variable for separating text from script info
zbx_tg_tmp_dir = os.getenv(ZTG_ZBX_TG_TMP_DIR, "/var/tmp/" + zbx_tg_prefix)  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = os.getenv(ZTG_ZBX_TG_SIGNATURE, False)

zbx_tg_update_messages = os.getenv(ZTG_ZBX_TG_UPDATE_MESSAGES, True)
zbx_tg_matches = os.getenv(ZTG_ZBX_TG_MATCHES, {)
    "problem": "PROBLEM: ",
    "ok": "OK: "
}

zbx_server = os.getenv(ZTG_ZBX_SERVER, "http://127.0.0.1/zabbix/")  # zabbix server full url
zbx_api_user = os.getenv(ZTG_ZBX_API_USER, "api")
zbx_api_pass = os.getenv(ZTG_ZBX_API_PASS, "api")
zbx_api_verify = os.getenv(ZTG_ZBX_API_VERIFY, True)  # True - do not ignore self signed certificates, False - ignore

zbx_server_version = os.getenv(ZTG_ZBX_SERVER_VERSION, 4)  # for Zabbix 4.x version

zbx_basic_auth = os.getenv(ZTG_ZBX_BASIC_AUTH, False)
zbx_basic_auth_user = os.getenv(ZTG_ZBX_BASIC_AUTH_USER, "zabbix")
zbx_basic_auth_pass = os.getenv(ZTG_ZBX_BASIC_AUTH_PASS, "zabbix")

proxy_to_zbx = os.getenv(ZTG_PROXY_TO_ZBX, None)
proxy_to_tg = os.getenv(ZTG_PROXY_TO_TG, None)

# proxy_to_zbx = os.getenv(ZTG_PROXY_TO_ZBX, "http://proxy.local:3128")
# proxy_to_tg = os.getenv(ZTG_PROXY_TO_TG, "https://proxy.local:3128")

# proxy_to_tg = os.getenv(ZTG_PROXY_TO_TG, "socks5://user1:password2@hostname:port") # socks5 with username and password
# proxy_to_tg = os.getenv(ZTG_PROXY_TO_TG, "socks5://hostname:port") # socks5 without username and password
# proxy_to_tg = os.getenv(ZTG_PROXY_TO_TG, "socks5h://hostname:port") # hostname resolution on SOCKS proxy.
                                          # This helps when internet provider alter DNS queries.
                                          # Found here: https://stackoverflow.com/a/43266186/957508

google_maps_api_key = os.getenv(ZTG_GOOGLE_MAPS_API_KEY, None)  # get your key, see https://developers.google.com/maps/documentation/geocoding/intro

zbx_tg_daemon_enabled = os.getenv(ZTG_ZBX_TG_DAEMON_ENABLED, False)
zbx_tg_daemon_enabled_ids = os.getenv(ZTG_ZBX_TG_DAEMON_ENABLED_IDS, [6931850, ])
zbx_tg_daemon_enabled_users = os.getenv(ZTG_ZBX_TG_DAEMON_ENABLED_USERS, ["ableev", ])
zbx_tg_daemon_enabled_chats = os.getenv(ZTG_ZBX_TG_DAEMON_ENABLED_CHATS, ["Zabbix in Telegram Script", ])

zbx_db_host = os.getenv(ZTG_ZBX_DB_HOST, "localhost")
zbx_db_database = os.getenv(ZTG_ZBX_DB_DATABASE, "zabbix")
zbx_db_user = os.getenv(ZTG_ZBX_DB_USER, "zbxtg")
zbx_db_password = os.getenv(ZTG_ZBX_DB_PASSWORD, "zbxtg")

emoji_map = {
    "OK": "✅",
    "PROBLEM": "❗",
    "info": "ℹ️",
    "WARNING": "⚠️",
    "DISASTER": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
