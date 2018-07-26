# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/FULLYCHARGEDSHOW
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.fullycharged'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

pl_id_1 = "PL5E13DC4A5011B1E6"

# Entry point
def run():
    plugintools.log("fullycharged.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("fullycharged.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Augstein und Blome",
        url="plugin://plugin.video.youtube/playlist/%s/" % pl_id_1,
        thumbnail=icon,
        folder=True )

run()