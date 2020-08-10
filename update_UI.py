# coding:utf-8
import os
import pprint
import glob
import re


# defaultRoot = "Z:\\"


def getAssetRoot(drive, project):
    return os.path.join(drive, project, "assets")


def get_assets(asset_root, charType):
    path = os.path.join(asset_root, charType)
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        return []


def get_asset_type(asset_name):
    asset_re = r"([a-zA-Z])\d+[a-zA-Z]+"
    matched = re.match(asset_re, asset_name)
    mapping = {
        "s": "set",
        "c": "char",
        "p": "prop",
        "e": "elem",

    }
    if matched:
        asset_type_char = matched.group(1)
        asset_type = mapping.get(asset_type_char, "null")
    else:
        asset_type = "null"
    return asset_type


def get_varient(asset_root, asset_type, asset, varient_type):
    asset_path = os.path.join(asset_root, asset_type, asset, )
    if varient_type == "geo":
        path = os.path.join(asset_path, "mod\\geo")
    if varient_type == "look":
        path = os.path.join(asset_path, "surface\\look")

    filePaths = glob.glob(path + "\\*")
    basenames = [os.path.basename(n) for n in filePaths if os.path.isdir(n)]
    return basenames


def asset_id_update(eventType, eventId, param, node):
    print eventType, eventType
    # monitor asset id
    if node.getType() != "Group":
        return
    typeParm = node.getParameter("user.type")
    if typeParm:
        # print("type")
        typeValue = typeParm.getValue(0)
        if typeValue == "AssetLoader":
            # print("AssetLoader")
            drive = node.getParameter("user.root").getValue(0)
            project = node.getParameter("user.project").getValue(0)
            if param.getFullName().endswith("user.ID") or param.getFullName().endswith("user.project"):
                if param.getFullName().endswith("user.ID"):
                    asset = node.getParameter("user.ID").getValue(0)
                    # rename node
                    node.setName(asset)
                    # change asset type
                    asset_type_name = get_asset_type(asset)
                    node.getParameter("user.assetType").setValue(asset_type_name, 0)

                asset_root = getAssetRoot(drive, project)
                asset_type = node.getParameter("user.assetType").getValue(0)
                asset = node.getParameter("user.ID").getValue(0)
                geo_varient = get_varient(asset_root, asset_type, asset, "geo")
                look_varient = get_varient(asset_root, asset_type, asset, "look")
                hint = {'widget': 'popup', 'options': geo_varient}
                node.getParameter("user.geo_varient").setHintString(pprint.pformat(hint))
                hint = {'widget': 'popup', 'options': look_varient}
                node.getParameter("user.look_varient").setHintString(pprint.pformat(hint))

    else:
        return


eventType = "parameter_finalizeValue"
# eventId = "asset_id"

try:
    Utils.EventModule.RegisterEventHandler(asset_id_update, eventType=eventType, )
except:
    print "error"
    # Utils.EventModule.UnregisterEventHandler(asset_id_update, eventType=eventType, eventID=eventId, )
    # Utils.EventModule.RegisterEventHandler(asset_id_update, eventType=eventType, eventID=eventId, enabled=True)
