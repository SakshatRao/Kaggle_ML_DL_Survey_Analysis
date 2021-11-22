import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from graphing_utils import *
from utils import *

def plot_lineplot(x_vals, y_vals, width = 15, height = 7, labels = [], suptitle = "Lineplot", title = "Demo", xlabel = "", ylabel = "", theme = 'DARK', x_names = [], rotate_x = 0):
    theme = select_theme(theme)
    fig, ax = create_fig(1, 1, width, height)
    if(len(y_vals) > len(theme['groups'])):
        group_colors = [(np.random.random(), np.random.random(), np.random.random()) for _ in range(len(y_vals))]
    else:
        group_colors = theme['groups'][:len(y_vals)]
    for y_val_idx, y_val in enumerate(y_vals):
        if(len(labels) == 0):
            ax.plot(x_vals, y_val, lw = 3, color = group_colors[y_val_idx], label = f'line #{y_val_idx + 1}')
        else:
            ax.plot(x_vals, y_val, lw = 3, color = group_colors[y_val_idx], label = labels[y_val_idx])
    ax = set_legend(ax, theme)
    ax = set_xticklabels(ax, x_names, rotate_x = rotate_x, theme = theme)
    exec(plot_decoration())
    plt.show()

def plot_barplot(x_names, y_vals, cats = [], width = 15, height = 7, suptitle = "Barplot", title = "Demo", xlabel = '', ylabel = '', theme = 'DARK', rotate_x = 0, rotate_y = 0):
    theme = select_theme(theme)
    fig, ax = create_fig(1, 1, width, height)
    x_vals = np.arange(len(x_names))
    if(len(cats) > 0):
        uniq_cats = list(sorted(pd.Series(cats).unique()))
        if(len(uniq_cats) > len(theme['groups'])):
            group_colors = [(np.random.random(), np.random.random(), np.random.random()) for _ in range(len(uniq_cats))]
        else:
            group_colors = theme['groups'][:len(uniq_cats)]
        group_colors = [group_colors[uniq_cats.index(x)] for x in cats]
    else:
        if(len(y_vals) > len(theme['groups'])):
            group_colors = [(np.random.random(), np.random.random(), np.random.random()) for _ in range(len(y_vals))]
        else:
            group_colors = theme['groups'][:len(y_vals)]
    ax.bar(x_vals, y_vals, color = group_colors)
    ax = set_xticklabels(ax, x_names, rotate_x = rotate_x, theme = theme)
    exec(plot_decoration())
    plt.show()

def plot_scatterplot(x_vals, y_vals, cats = [1], width = 15, height = 7, suptitle = "Scatterplot", title = 'Demo', xlabel = '', ylabel = '', theme = 'DARK', annotate = False, annotate_texts = []):
    theme = select_theme(theme)
    fig, ax = create_fig(1, 1, width, height)
    no_cats_passed = False
    if(len(cats) == 1):
        cats = np.ones(len(x_vals))
        no_cats_passed = True
    uniq_cats = pd.Series(cats).unique()
    if(len(uniq_cats) > len(theme['groups'])):
        group_colors = [(np.random.random(), np.random.random(), np.random.random()) for _ in range(len(uniq_cats))]
    else:
        group_colors = theme['groups'][:len(uniq_cats)]
    for cat_idx, cat in enumerate(uniq_cats):
        ax.scatter(x_vals[cats == cat], y_vals[cats == cat], color = group_colors[cat_idx], label = cat)
    if(annotate == True):
        for idx in range(len(x_vals)):
            ax.annotate(annotate_texts[idx], (x_vals[idx], y_vals[idx]), color = theme['text'])
    if(no_cats_passed == False):
        ax = set_legend(ax, theme)
    exec(plot_decoration())
    plt.show()

def plot_us_map(state_vals_df, title, val_col, val_label, range_min_val = 0, range_max_val = 1, theme = 'DARK', state_col = 'STATE_ABBR'):
    
    theme = select_theme(theme)

    layout = dict(
        font_family = 'Source Sans Pro',
        font_color = theme['text'],
        title_text = title,
        # To change
        title_font = dict(
            family = "Source Sans Pro",
            size = 25,
            color = theme['axis']
        ),
        geo_scope = 'usa',
        paper_bgcolor = theme['bg'],
        geo_bgcolor = theme['bg'],
        geo = dict(
            landcolor = theme['inv'],
            subunitcolor = theme['gray'],
            lakecolor = theme['bg'],
        ),
    )

    fig = px.choropleth(
        state_vals_df,
        locations = state_col,
        color = val_col,
        color_continuous_scale = [theme['color-1'], theme['color+1_higher']],
        range_color = (range_min_val, range_max_val),
        locationmode = "USA-states",
        labels = {val_col : val_label, state_col: 'State'},
    )

    fig.update_layout(layout)
    fig.update_layout(margin = {"r": 0, "l": 0, "b": 15})
    fig.show()