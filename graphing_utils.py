import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

COLOR_WHITE = '#F8F1FF'
COLOR_BLACK = '#231942'
COLOR_DARK_BLUE = '#156BB7'
COLOR_LIGHT_BLUE = '#63D1DF'
COLOR_GREEN = '#30DB8D'
COLOR_DARK_GREEN = '#0DAB6C'
COLOR_ORANGE = '#FBAB60'
COLOR_YELLOW = '#F8E16C'
COLOR_RED = '#DA4167'

PLOT_THEME_LIGHT = {
    'text': COLOR_BLACK,
    'axis': COLOR_BLACK,
    'subtitle': COLOR_DARK_BLUE,
    'color+1': COLOR_DARK_GREEN,
    'color+2': COLOR_YELLOW,
    'color+3': COLOR_ORANGE,
    'color+4': COLOR_DARK_BLUE,
    'color-1': COLOR_RED,
    'bg': COLOR_LIGHT_BLUE,
    'inv': COLOR_WHITE,
    'color+1_lower': '#064B30',
    'color+1_higher': '#2EEFA2',
    'gray': '#676076',
}
PLOT_THEME_LIGHT['groups'] = [PLOT_THEME_LIGHT[x] for x in ['color+1', 'color-1', 'color+3', 'color+4', 'color+2']]

PLOT_THEME_DARK = {
    'text': COLOR_WHITE,
    'axis': COLOR_WHITE,
    'subtitle': COLOR_LIGHT_BLUE,
    'color+1': COLOR_GREEN,
    'color+2': COLOR_YELLOW,
    'color+3': COLOR_ORANGE,
    'color+4': COLOR_LIGHT_BLUE,
    'color-1': COLOR_RED,
    'bg': COLOR_DARK_BLUE,
    'inv': COLOR_BLACK,
    'color+1_lower': '#188B57',
    'color+1_higher': '#86EABD',
    'gray': '#D6CFDB',
}
PLOT_THEME_DARK['groups'] = [PLOT_THEME_DARK[x] for x in ['color+1', 'color-1', 'color+3', 'color+4', 'color+2']]

def create_fig(nrows = 1, ncols = 1, width = 10, height = 5):
    fig, ax = plt.subplots(nrows, ncols, figsize = (width, height))
    return fig, ax

def remove_spines(ax, theme = {}):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(theme['axis'])
    ax.spines['left'].set_color(theme['axis'])
    return ax

def remove_all_spines(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    return ax

def set_titles_and_labels(fig, ax, fig_title = "", title = "", xlabel = "", ylabel = "", theme = {}):
    fig.suptitle(fig_title, fontsize = 30, color = theme['text'])
    ax.set_title(title, fontsize = 20, color = theme['subtitle'])
    ax.set_xlabel(xlabel, fontsize = 15, color = theme['text'])
    ax.set_ylabel(ylabel, fontsize = 15, color = theme['text'])
    return fig, ax

def set_ticks(ax, theme):
    ax.tick_params(axis = 'x', colors = theme['axis'])
    ax.tick_params(axis = 'y', colors = theme['axis'])
    return ax

def set_xticklabels(ax, labels, rotate_x = 0, theme = {}):
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, color = theme['text'], rotation = rotate_x)
    return ax

def set_yticklabels(ax, labels, rotate_y = 0, theme = {}):
    ax.set_yticks(np.arange(len(labels)))
    ax.set_yticklabels(labels, color = theme['text'], rotation = rotate_y)
    return ax

def set_bg(fig, ax, theme):
    fig.set_facecolor(theme['bg'])
    ax.set_facecolor(theme['bg'])
    return fig, ax

def select_theme(theme):
    if(theme == 'DARK'):
        return PLOT_THEME_DARK
    else:
        return PLOT_THEME_LIGHT

def set_legend(ax, theme):
    ax.legend(loc = 'best')
    return ax

def plot_decoration():
    return """
    fig, ax = set_bg(fig, ax, theme); ax = set_ticks(ax, theme); ax = remove_spines(ax, theme); fig, ax = set_titles_and_labels(fig, ax, suptitle, title, xlabel, ylabel, theme);
    """.strip()