from libqtile import bar, layout, qtile, widget, hook
from libqtile.widget.backlight import Backlight
from libqtile.widget.battery import BatteryIcon
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
import json

# Load Pywal colors
# def load_pywal_colors():
#     with open(os.path.expanduser('~/.cache/wal/colors.json')) as f:
#         colors = json.load(f)
#     return colors
# Load colors from Pywal
# colors = load_pywal_colors()


mod = "mod4"
terminal = "alacritty"
# A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
#MAKE A COLOR DICTIONARY
my_colors = [
    
]

keys = [   
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    #OR
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    
    #Full-Focus/Reload/Kill
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
    #    [mod, "shift"],
    #    "Return",
    #    lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack",
    #),

    #Program LazySpawns
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod, "control"], "d", lazy.spawn("rofi -show run")),
    Key([mod], "p", lazy.spawn("vscodium")),
    Key([mod], "o", lazy.spawn("obsidian")),
    Key([mod], "i", lazy.spawn("firefox")),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Toggle between different layouts as defined below

]

# Add key bindings to switch VTs in Wayland.
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# Groups(Workspaces)
groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
# Coloring for focused border
border_colors = {
    "focus": "#8a817c",   # Green for focused borders
    "normal": "#000000"   # Black for unfocused borders
}

# Layouts
layouts = [
    layout.Columns(    
        border_focus=border_colors["focus"],
        #border_normal=border_colors["normal"],
        border_width=1,
        margin=5,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=2,
)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Set wallpaper on startup
@hook.subscribe.startup_once
def set_wallpaper():
    home = os.path.expanduser('~')
    wallpaper_path = os.path.join(home, 'Pictures', 'do_0my-cli-dash.jpg')
    subprocess.Popen(['wal', '-q', '-i', wallpaper_path])

@hook.subscribe.startup_once
def autostart():
    # You can add more programs like this:
    # os.system("program_name &")
    os.system("picom &")
    os.system("nm-applet &")

# Qtile Bar Config
extension_defaults = widget_defaults.copy()
screens = [
 Screen(
        top=bar.Bar(
            [
               widget.GroupBox(
                    active="#ffffff",  # Active group text color
                    inactive="#ffffff",  # Inactive group text color
                    highlight_method='block',
                    this_current_screen_border="#8a817c",  # Current screen border color
                    this_screen_border="#8a817c",  # Other screen border color
                    other_current_screen_border="#8a817c",
                    other_screen_border="#8a817c",
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Battery(format='{percent:2.0%}'),
                widget.BatteryIcon(
                    background= None,
                    battery=0,
                    padding=0,
                    scale=1,
                ),
                widget.Systray(),
                widget.Clock(format=" %I:%M %p"),

            ],
            24,
            background=["#041013"],  # Background color of the bar
            foreground="#ffffff",  # Foreground (text) color of the bar
            border_width=[1, 0, 1, 0],  # Draw top and bottom borders
            border_color=["#ffffff", "000000", "#8a817c", "000000"], 
        ),
           
    ),
]





# MISC
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string
