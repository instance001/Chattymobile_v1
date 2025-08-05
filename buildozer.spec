[app]

title = Chatty
package.name = chatty
package.domain = org.chatty
source.dir = .
source.include_exts = py,txt,json
source.exclude_exts = pyc,pyo
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
osx.kivy_version = 2.3.0

# ✅ Add these:
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.storage = true
android.api = 30
android.minapi = 21
android.target = 30
android.debug = 1

[buildozer]
log_level = 2
warn_on_root = 1

