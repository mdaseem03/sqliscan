#!/usr/bin/env python3


"""
 * Developed By mdaseem03 
 * Intern
 * Cappricio Securities <https://cappriciosec.com>
 */
 
"""
import click 
from .utils import helpers
from .includes import scan
from .includes import filereader
from .utils import const
import os


def helpbanner(ctx, params, value):
    if value:
        helpers.display_help()
        ctx.exit()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--url', type=str, help="URL to scan")
@click.option('-i', '--input', type=str, help="lost of input file")
@click.option('-h', '--help', 'helpbanner', is_flag=True, expose_value=False, is_eager=True, callback=helpbanner, help="help menu")

def main(url, input):
    if url:
       helpers.banner()
       scan.scanner(url)

    if input:
       helpers.banner()
       filereader.reader(input)
    
    
    
    
    
if __name__ == "__main__":
    main()
