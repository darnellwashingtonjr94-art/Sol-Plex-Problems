[app]
title = Sol-Plex Problems
package.name = solplex
package.domain = org.solplex
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,md,json
version = 0.1.5

# Match repo requirements (Kivy, Asyncio, Google Cloud libraries)
requirements = python3,kivy,aiohttp,redis,google-cloud-firestore,google-cloud-secretmanager

orientation = portrait
fullscreen = 0

# Network permissions required for API/GCP communication
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
