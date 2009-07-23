from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel

from OpenMaps import OpenMap, OpenWMSLayer

class SimpleMap:
    def onModuleLoad(self):
        panel = VerticalPanel()

        self.map = OpenMap(Width="50%", Height="50%")

        self.wms = OpenWMSLayer("OpenLayers WMS",
            "http://labs.metacarta.com/wms/vmap0", layers="basic")

        self.map.addLayer(self.wms)

        panel.add(self.map)

        RootPanel().add(self.map)

if __name__ == '__main__':
    app = SimpleMap()
    app.onModuleLoad()
