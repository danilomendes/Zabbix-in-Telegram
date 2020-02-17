# -*- coding: utf-8 -*-
import os

zbx_server = os.getenv("ZTG_SERVER", "http://127.0.0.1/zabbix/")
zbx_api_user = os.getenv("ZTG_API_USER", "api")
zbx_api_pass = os.getenv("ZTG_API_PASS", "api")

# True - do not ignore self signed certificates, False - ignore
zbx_api_verify = os.getenv("ZTG_API_VERIFY", True)

# for Zabbix 4.x version, default will be changed in the future with this
zbx_server_version = os.getenv("ZTG_SERVER_VERSION", 4)

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
