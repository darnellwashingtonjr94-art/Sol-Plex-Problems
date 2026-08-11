[app]
title = Sol-Plex
package.name = solplex
package.domain = org.solplex
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,md,json
version = 0.1.7

requirements = python3,kivy,aiohttp,redis,google-cloud-firestore

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_licenses = True
