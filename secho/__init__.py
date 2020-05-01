"""Top-level package for Style Echo."""
# -*- coding: utf-8 -*-

import click

__author__ = "José Antonio Puértolas Montañés"
__email__ = 'j5pu@icloud.com'
__version__ = '0.1.0'


def black(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='black', err=err)


def red(msg=str(), bold=False, underline=False, blink=False, err=True):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='red', err=err)


def green(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='green', err=err)


def yellow(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='yellow', err=err)


def blue(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='blue', err=err)


def magenta(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='magenta', err=err)


def cyan(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='cyan', err=err)


def white(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='white', err=err)


def bblack(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_black', err=err)


def bred(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_red', err=err)


def bgreen(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_green', err=err)


def byellow(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_yellow', err=err)


def bblue(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_blue', err=err)


def bmagenta(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_magenta', err=err)


def bcyan(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_cyan', err=err)


def bwhite(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='bright_white', err=err)


def reset(msg=str(), bold=False, underline=False, blink=False, err=False):
    click.secho(msg, bold=bold, underline=underline, blink=blink, color=True, fg='reset', err=err)
