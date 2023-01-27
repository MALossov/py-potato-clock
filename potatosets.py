import time

import yaml
from rich.console import Console
import os
import sys

console = Console()


def sets(args):
    if args.init:
        init_settings()
        exit(0)
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        pass
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!",
            style="bold red",
        )
        console.print(
            "[bold blue2]Please run ",
            "[italic cyan]potato settings -i",
            " to init the settings",
        )
        exit(1)

    if args.show:
        show_settings()
    elif args.edit:
        edit_settings(args)
    elif args.clear:
        clear_settings()
    else:
        console.print("Error: Invalid settings command!!", style="bold red")
        console.print(
            "[bold blue]Your settings command must be: [italic cyan], -s, -c, -i"
        )
        exit(1)


def init_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        console.print(
            "Error: pttsets.yaml already exists!!",
            style="bold red",
        )
        console.print(
            "[bold blue]Please run ",
            "[italic cyan]potato settings -c",
            "[bold blue] to clear the settings",
        )
        exit(1)
    else:
        with open("pttsets.yaml", "w") as f:
            yaml.dump(
                {
                    "TomatoClocks": {
                        "KeepTime": 25,
                        "NoticingIntervals": 2,
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
            "[Bold blue]Please run [Italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)


def show_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        with open("pttsets.yaml", "r") as f:
            data = yaml.safe_load(f)
        console.print(data, style="white on navy_blue")
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!\n",
            style="bold red",
        )
        console.print(
            "[Bold blue]Please run [Italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)


def edit_settings(args):
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        with open("pttsets.yaml", "r") as f:
            data = yaml.safe_load(f)
        for item in data:
            console.rule(
                "[italic pale_turquoise1]Editing:[/][bold blue]{}[/]?:".format(item),
                style="bold blue",
                align="left",
            )
            for key in data[item]:
                console.print(
                    "[italic pale_turquoise1]Edit[/][bold blue]{}[/]?:".format(key),
                    end="|",
                )
                console.print(
                    "[bold blue]Current value:[/][bold cyan]{}[/]".format(
                        data[item][key]
                    ),
                    end="|",
                )
                console.print("[bold blue]New value:[/]", end="")
                new_value = input()
                if new_value == "":
                    pass
                else:
                    data[item][key] = new_value
        with open("pttsets.yaml", "w") as f:
            yaml.dump(data, f)
        console.rule(
            "Settings file edited successfully!!", style="bold green", align="left"
        )


def load_settings():
    # Check if pttsets.yaml exists
    if os.path.exists("pttsets.yaml"):
        with open("pttsets.yaml", "r") as f:
            data = yaml.safe_load(f)
        return data
    else:
        console.print(
            "Error: pttsets.yaml does not exist!!\n",
            style="bold red",
        )
        console.print(
            "[bold blue]Please run [italic cyan]potato settings -i[/] to init the settings"
        )
        exit(1)


class Settings:
    def __init__(self):
        self.default_confirm = False
        self.default_time = 25
        self.default_intervals = 2
        self.default_aim = "Study"
        self.default_color = "spring_green1"
        self.default_bg = "deep_sky_blue2"
        self.default_pulse = "aquamarine3"
        self.default_queryG = None
        self.default_queryT = None

    def load(self):
        conf = load_settings()
        self.default_confirm = conf["TomatoClocks"]["AutoStart"]
        self.default_time = conf["TomatoClocks"]["KeepTime"]
        self.default_intervals = conf["TomatoClocks"]["NoticingIntervals"]
        self.default_aim = conf["TomatoClocks"]["DefaultAim"]
        self.default_color = conf["ProgressColorSets"]["CompletedColor"]
        self.default_bg = conf["ProgressColorSets"]["BackgroundColor"]
        self.default_pulse = conf["ProgressColorSets"]["PulseColor"]
        self.default_queryG = conf["DefaultQuerySets"]["DefaultQueryAim"]
        self.default_queryT = conf["DefaultQuerySets"]["DefaultDays"]
