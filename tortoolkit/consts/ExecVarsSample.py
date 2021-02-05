try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "efce4a04d1349fc6e007cafcefe640b0"
        API_ID = "2984400"
        BOT_TOKEN = "1456987498:AAGtiwtCm0nTNxr3JK4H9tWyHzx-aeNognE"
        BASE_URL_OF_BOT = "https://gautamleecherbot.herokuapp.com/"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [982055867,-1001169765253,-1001432689018]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 40

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1800000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = "postgresql://onlyaby:bayu123ok@postgresql/postgres"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/Bot Uploads/Leech Bot"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = True

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = True
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = "leech"

        # Max size of the videos in playlist allowed
        MAX_YTPLAYLIST_SIZE = 200
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 30

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





