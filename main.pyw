import pystray
import collector as cl
from PIL import Image
import config
from dashboard import generate_window

# collector
collector = cl.Collector(config.INDEX_FILE)

# icon setup
def icon_setup(icon):
    icon.visible = True

    # starting the collector thread
    collector.begin(icon)

# click callback
def click_callback(icon, item):
    if str(item) == "Exit MKSC":
        collector.finished = True
        icon.stop()
    if str(item) == "Open dashboard":
        generate_window()

# icon
image = Image.open('icon.png')
icon = pystray.Icon(
    'MKSC', image, menu=pystray.Menu(
        pystray.MenuItem('Exit MKSC', click_callback),
        pystray.MenuItem('Open dashboard', click_callback)
    )
)
icon.run(setup=icon_setup)

collector.finished = True