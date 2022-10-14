"""
    Draw some plots of scalings of high energy physics
"""
import click
import os
from .plotting import plotscale

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        helpinfo() 

@cli.command()
@click.argument("path")
def plot(path):
    """ plot the data file
    """
    datadir = os.path.join(os.environ["HOME"], ".hepscale/")
    datapath = os.path.join(datadir, path)
    plotscale(datapath)

@cli.command()
@click.argument("path")
def ls(path):
    """ list the data in the path (example: hepscale ls .)
    """
    datadir = os.path.join(os.environ["HOME"], ".hepscale/")
    datapath = os.path.join(datadir, path)
    data = os.listdir(datapath)
    folder = []
    files = []
    for d in data:
        if d.startswith("."):
            continue
        if os.path.isdir(os.path.join(datapath, d)):
            folder.append(d)
        else:
            files.append(d)
    if len(folder) > 0:
        print(">>>> Folders:")
        for f in folder:
            print(f)
    if len(files) > 0:
        print(">>>> Files:")
        for f in files:
            print(f)


def helpinfo():
    print("please use ``hepscale --help'' for help")

def main():
    datadir = os.path.join(os.environ["HOME"], ".hepscale/")
    if (not os.path.exists(datadir)):
        os.makedirs(datafile)
    cli()
