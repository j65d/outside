#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple Python script that prints a greeting message.
"""

def greet(name: str = "World") -> None:
    """Print a greeting message.
    
    Args:
        name: Name to greet (default: "World")
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet()