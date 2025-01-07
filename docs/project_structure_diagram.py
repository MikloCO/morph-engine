from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams.programming.language import Python
from diagrams.programming import flowchart
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
with Diagram("Game engine", show=False, filename="docs/architecture") as diag:

    with Cluster("Components"):
        scene = flowchart.Display("Scene graph")
        game_manager = flowchart.Action("Game manager")
        state_synchronization = flowchart.Action("State synchronization")
        main = Python("main")

    with Cluster("Gameplay"):
        with Cluster("Scripting"):
            scripting = flowchart.Display("Scripting")
            game_objects = flowchart.Display("Game objects")
        with Cluster("Art"):
            artworks = flowchart.Display("Animations")
            audio = flowchart.Display("Audio")


    state_synchronization >> scripting



diag.render()
