"""Console script for morrigan."""
import sys
import click
from morrigan.morrigan import g_inp, g_out


@click.command()
@click.option("-f", "--file")
@click.option("-o", "--output")
def main(file, output):
    """Console script for morrigan."""
    G = g_inp(file)
    return g_out(G, output)
