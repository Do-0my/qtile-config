# qtile-config
Qtile configuration with custom keybindings, themes, autostart scripts, and enhancements.

## ToC
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Autostart](#autostart)
- [Themes](#themes)
- [Scripts](#scripts)

## Introduction
This repository contains my personal configuration for the Qtile window manager. It includes custom keybindings, themes, autostart scripts, and other enhancements to improve the Qtile experience.

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/Do-0my/qtile-config.git
    cd qtile-config
    ```

2. **Copy the configuration files**:
    ```sh
    mkdir -p ~/.config/qtile
    cp -r qtile/* ~/.config/qtile/
    ```

3. **Install necessary dependencies**:
    Make sure you have the required dependencies installed:
    - `qtile`
    - `python`
    - `libpulse`
    - `dmenu`

## Configuration
The main configuration file is `config.py` located in the `qtile` directory. You can customize keybindings, layout settings, and other options in this file.

## Autostart
The `autostart.sh` script is used to start applications and services when Qtile starts. You can add your own startup applications to this script.

## Themes
Themes are stored in the `themes` directory. You can switch themes by modifying the `config.py` file to point to the desired theme file.

## Scripts
Custom scripts used within Qtile are stored in the `scripts` directory. These scripts can be used for various tasks such as locking the screen, changing the wallpaper, etc.
