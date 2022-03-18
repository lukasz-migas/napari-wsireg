from qtpy.QtCore import Qt
from qtpy.QtGui import QFont
from qtpy.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabWidget
from superqt.collapsible import QCollapsible

from napari_wsireg.gui.setup_sub.modality import ModalityControl
from napari_wsireg.gui.setup_sub.paths import RegistrationPathControl
from napari_wsireg.gui.setup_sub.preprocessing import PreprocessingControl
from napari_wsireg.gui.setup_sub.project import ProjectControl
from napari_wsireg.gui.setup_sub.graph import RegGraphViewer
from napari_wsireg.gui.queue import QueueControl

from napari_wsireg.gui.utils.colors import ATTACHMENTS_COL, IMAGES_COL, SHAPES_COL


class SetupTab(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        setup_layout = QVBoxLayout()
        setup_layout.setSpacing(10)
        setup_layout.addStretch()
        setup_layout.setAlignment(Qt.AlignTop)
        self.setLayout(setup_layout)
        mod_header = QLabel()
        mod_header.setText(
            f'<font color="{IMAGES_COL}"><b>Registration images</b></font> | '
            f'<font color="{ATTACHMENTS_COL}"><b>Attachment images</b> '
            f'</font>| <font color="{SHAPES_COL}"><b>Attachment shapes</b></font>'
        )

        mod_header.setFont(QFont("Arial", 14))
        mod_header.setAlignment(Qt.AlignTop)

        self.mod_ctrl = ModalityControl()
        self.prepro_ctrl = PreprocessingControl()
        self.path_ctrl = RegistrationPathControl()
        self.graph_view = RegGraphViewer()
        self.proj_ctrl = ProjectControl()
        self.queue_ctrl = QueueControl()

        self.layout().addWidget(mod_header)
        self.layout().setAlignment(mod_header, Qt.AlignTop)

        self.layout().addWidget(self.mod_ctrl)
        self.layout().setAlignment(self.mod_ctrl, Qt.AlignTop)

        self.prepro_collapse = QCollapsible(title="Preprocessing")
        self.prepro_collapse.addWidget(self.prepro_ctrl)
        self.layout().addWidget(self.prepro_collapse)
        self.layout().setAlignment(self.prepro_ctrl, Qt.AlignTop)

        reg_path_tabs = QTabWidget()
        reg_path_tabs.addTab(self.path_ctrl, "Define paths")
        reg_path_tabs.addTab(self.graph_view, "View graph")
        self.layout().addWidget(reg_path_tabs)
        self.layout().setAlignment(reg_path_tabs, Qt.AlignTop)

        project_tabs = QTabWidget()
        project_tabs.addTab(self.proj_ctrl, "Current graph")
        project_tabs.addTab(self.queue_ctrl, "Reg. queue")

        self.layout().addWidget(project_tabs)
        self.layout().setAlignment(project_tabs, Qt.AlignTop)
        setup_layout.addStretch()
        setup_layout.setSpacing(10)
