from importlib import reload
import goo
from goo.division import *
from goo.handler import *

reload(goo)
goo.reset_modules()
goo.reset_scene()

celltype = goo.OpaqueType("A")
cell = celltype.create_cell("cellA", (0, 0, 0))

sim = goo.Simulator(celltypes=[celltype])
sim.setup_world()

sim.add_handlers(
    [
        GrowthPIDHandler(target_volume=30),
        RemeshHandler(voxel_size=0),
        AdhesionLocationHandler(),
    ]
)
