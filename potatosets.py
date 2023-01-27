import yaml
from rich.console import Console
import os
import sys

console = Console()


def sets(args):
    if args.init:
        init_settings()
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        pass
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!\n",
            style="bold red",
        )
        console.print(
            "[Bold dark_blue]Please run [Italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)

    if args.load:
        load_settings()
    elif args.show:
        show_settings()
    elif args.clear:
        clear_settings()
    else:
        console.print("Error: Invalid settings command!!\n", style="bold red")
        console.print(
            "[Bold dark_blue]Your settings command must be: [Italic cyan]-l, -s, -c, -i"
        )
        exit(1)


def init_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        console.print(
            "Error: pttsets.yaml already exists!!\n",
            style="bold red",
        )
        console.print(
            "[Bold dark_blue]Please run [Italic cyan]potato settings -c[/] to clear the settings"
        )
        exit(1)
    else:
        with open("pttsets.yaml", "w") as f:
            yaml.dump(
                {
                    "TomatoClocks": {
                        "KeepTime": 25,
                        "NoticingIntervals": 5,
                        "DefaultAim": "Study",
                        "AutoStart": False,
                    },
                    "ProgressColorSets": {
                        "BackgroundColor": "deep_sky_blue4",
                        "PulseColor": "aquamarine3",
                        "CompletedColor": "spring_green1",
                    },
                    "DefaultQuerySets": {
                        "DefaultDays": 7,
                        "DefaultQueryAim": "Study",
                    },
                },
                f,
            )
        console.print("Settings file created successfully!!", style="bold green")


def clear_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        os.remove("pttsets.yaml")
        console.print("Settings file cleared successfully!!", style="bold green")
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!\n",
            style="bold red",
        )
        console.print(
            "[Bold dark_blue]Please run [Italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)


def show_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        with open("pttsets.yaml", "r") as f:
            data = yaml.safe_load(f)
        console.print(data, style="auto")
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!\n",
            style="bold red",
        )
        console.print(
            "[Bold dark_blue]Please run [Italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)
