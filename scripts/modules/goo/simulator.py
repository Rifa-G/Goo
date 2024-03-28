import bpy

from goo.handler import TimingHandler
from datetime import datetime


class Simulator:
    def __init__(self, celltypes, physics_dt=1):
        self.handlers = []
        self.celltypes = celltypes
        self.physics_dt = physics_dt

    def get_cells(self):
        return [cell for celltype in self.celltypes for cell in celltype.cells]

    def add_handler(self, handler):
        handler.setup(self.get_cells, self.physics_dt)
        self.handlers.append(handler.run)

    def run_simulation(self):
        start_time = datetime.now()
        bpy.app.handlers.frame_change_post.extend(self.handlers)
