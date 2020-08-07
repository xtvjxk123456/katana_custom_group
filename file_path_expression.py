path.join(self.getNode().getParent().getParameter("user.asset_root").getValue(0),
self.getNode().getParent().getParameter("user.assetType").getValue(0),
self.getNode().getParent().getParameter("user.ID").getValue(0),
"mod\\geo",
self.getNode().getParent().getParameter("user.geo_varient").getValue(0),
"ok\\{}_geo_{}.abc".format(self.getNode().getParent().getParameter("user.ID").getValue(0),
self.getNode().getParent().getParameter("user.geo_varient").getValue(0))

)