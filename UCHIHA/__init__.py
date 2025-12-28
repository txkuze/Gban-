from UCHIHA.core.bot import PARTH
from UCHIHA.core.dir import dirr
from UCHIHA.core.git import git
from UCHIHA.core.userbot import Userbot
from UCHIHA.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PARTH()
api = SafoneAPI()
userbot = Userbot()
