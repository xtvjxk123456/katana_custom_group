import os
import pprint
import glob


def get_assets(asset_root, charType):
    path = os.path.join(asset_root, charType)
    return os.listdir(path)


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
    print eventType,eventType
    # monitor asset id
    if node.getType() != "Group":
        return
    typeParm = node.getParameter("user.type")
    if typeParm:
        print("type")
        typeValue = typeParm.getValue(0)
        if typeValue == "AssetLoader":
            print("AssetLoader")
            if param.getFullName().endswith("user.ID"):
                print("user.ID")
                asset_root = node.getParameter("user.asset_root").getValue(0)
                asset_type = node.getParameter("user.assetType").getValue(0)
                asset = node.getParameter("user.ID").getValue(0)
                geo_varient = get_varient(asset_root, asset_type, asset, "geo")
                look_varient = get_varient(asset_root, asset_type, asset, "look")
                hint = {'widget': 'popup', 'options': geo_varient}
                node.getParameter("user.geo_varient").setHintString(pprint.pformat(hint))
                hint = {'widget': 'popup', 'options': look_varient}
                node.getParameter("user.look_varient").setHintString(pprint.pformat(hint))
                Utils.EventModule.ProcessAllEvents()
            if param.getFullName().endswith("user.assetType"):
                print("user.assetType")
                asset_root = node.getParameter("user.asset_root").getValue(0)
                asset_type = node.getParameter("user.assetType").getValue(0)
                assets = get_assets(asset_root, asset_type)
                hint = {'widget': 'popup', 'options': assets}
                node.getParameter("user.ID").setHintString(pprint.pformat(hint))
                


    else:
        return


eventType = "parameter_finalizeValue"
# eventId = "asset_id"

try:
    Utils.EventModule.RegisterEventHandler(asset_id_update, eventType=eventType,)
except:
    print "error"
    # Utils.EventModule.UnregisterEventHandler(asset_id_update, eventType=eventType, eventID=eventId, )
    # Utils.EventModule.RegisterEventHandler(asset_id_update, eventType=eventType, eventID=eventId, enabled=True)