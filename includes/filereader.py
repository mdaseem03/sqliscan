#!/usr/bin/env python3


"""
 * Developed By mdaseem03 
 * Intern
 * Cappricio Securities <https://cappriciosec.com>
 */
 
"""

from . import scan

def reader(input):
    try:
        with open(input,'r') as file:
            for line in file:
                scan.scanner(line.strip())
    except FileNotFoundError:
        print("File not found. Check the file path and name.")

    