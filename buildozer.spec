[app]

# (str) Title of your application
title = Sol-Plex-Problems

# (str) Package name
package.name = solplex

# (str) Package domain (needed for android packaging)
package.domain = org.credkellarboop

# (str) Source code where the main.py lives (REQUIRED)
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application version (REQUIRED)
version = 0.1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android Build Tools version
android.build_tools_version = 33.0.2

# (bool) Automatically accept SDK licenses
android.accept_licenses = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
