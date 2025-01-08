from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3
from diagrams.generic.network import Firewall
from diagrams.generic.os import Windows
from diagrams.programming.language import Python
from diagrams.azure.network import PublicIpAddresses
from diagrams.programming.language import C
from diagrams.elastic.elasticsearch import Monitoring


import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

with Diagram("Game Engine Architecture", show=False, direction="TB", filename="docs/architecture") as diag:

    # Render Engine
    with Cluster("Render Engine"):
        render = Python("Rendering Engine")
        graphics = C("Graphics: Vulkan")
        audio = S3("Audio")
        ui = PublicIpAddresses("UI")

        render >> [graphics, audio, ui]

    # Resource Handling
    with Cluster("Resource Handling"):
        state_synchronization = Monitoring("Game Loop")
        resources = S3("Asset Management")
        scene = S3("Scene Graph")
        artworks = S3("Animations")
        game_objects = S3("Game Objects")

        state_synchronization >> [resources, scene, artworks, game_objects]

    # Physics
    with Cluster("Physics"):
        math = Sagemaker("Math")
        physics = Firewall("Physics Engine")
        collision = Firewall("Collision Handler")


    # Gameplay
    with Cluster("Gameplay"):
        scripting = Python("Scripting")
        npc = Lambda("NPC Logic")
        input_io = PublicIpAddresses("Input System")
        game_events = Lambda("Events")

        scripting >> [npc, input_io, game_events]



    diag.render()
