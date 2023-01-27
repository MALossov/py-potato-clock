"""
Description: 
Author: MALossov
Date: 2023-01-27 16:53:44
LastEditTime: 2023-01-27 23:26:31
LastEditors: MALossov
Reference: 
"""
import rich.progress
from rich.console import Console
import os
import sys
import time
import potatodb
import datetime

console = Console()


def potato_clock(args):
    # 首先打印当前时间,预计结束的时间,定时的时间和提醒的间隔.
    # 所有时间用不同彩色的字体打印
    # 打印分行符之后打印进度条,进度条的颜色和字体颜色一致
    console.print(
        "Present time:",
        "[yellow underline]" + time.strftime("%H:%M:%S", time.localtime()),
        end="\t\t|\t",
    )
    console.print(
        "Schedule end time:",
        "[blue underline]"
        + time.strftime(
            "%H:%M:%S",
            time.localtime(time.time() + args.time * 60),
        ),
        end="\t|\n",
    )
    console.print(
        "[bold blue]Notify intervals:", args.Intervals, "minutes", end="\t|\t"
    )
    console.print("[bold red]potato clock:", args.time, "minutes", end="\t|\n")
    console.rule("[bold blue]Potato Aim:[cyan2]" + args.aim, style="bold cyan")

    # 使用定时器
    # 每隔0.25秒刷新一次进度条
    # 每隔args.Intervals分钟提醒一次
    # 进度条到达100%时,打印完成信息,并退出程序
    with rich.progress.Progress(
        "[progress.description]{task.description}",
        rich.progress.BarColumn(
            bar_width=None,
            style="bold " + args.back,
            complete_style="bold " + args.color,
            pulse_style="bold" + args.pulse,
        ),
        "[progress.percentage]{task.percentage:>3.0f}%",
        rich.progress.TimeRemainingColumn(),
        console=console,
    ) as progress:
        tomatoClkTask = progress.add_task(
            "[bold blue]PotatoClock",
            total=args.time * 60,
            start=False,
        )
        if args.start:
            pass
        else:
            print("Press [italic magenta]Y/n [/]to start/absorb:", end="")
            if input() == "Y" or "y" or "":
                console.rule(
                    "\r[magenta]Tasking:{}\t|\t[cyan]Total:{}\t".format(
                        args.aim, args.time
                    )
                )
            else:
                print("[bold red]PotatoClock absorbed!")
                sys.exit(0)
        progress.start_task(tomatoClkTask)
        for i in range(args.time * 60):
            progress.advance(tomatoClkTask)
            time.sleep(1)
            if i % (args.Intervals * 60) == 0:
                # 构建通知字符串
                notify_str = """notify-send \"potatoClock!\" \"You passed one Interval for {} minutes!\nNow your time 
                left is: {:.1f} minutes\"""".format(
                    args.Intervals, float(args.time - i / 60)
                )
                # 使用notify-send发送通知
                os.system(notify_str)
    console.rule("[bold green]potato clock is over!")
    console.print(
        "[italic blue]Cool!!",
        "\t[yellow]You did a :",
        args.time,
        "[yellow]minutes [bold red]potato CLOCK!!\n",
        end="",
    )
    # 将本次的番茄钟信息存入数据库
    try:
        potatodb.create_table()
        potatodb.insert_potato(args.time, args.aim, datetime.datetime.now())
        console.print("[bold green italic]Time well remember Everything~")
    except Exception as e:
        console.print("[bold red]Failed to insert data into database!")
