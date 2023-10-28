# YouFuckTube - UNBLOCK YOUTUBE ADBLOCK-BLOCK Browser Extension
Simply replaces the youtube video by embedded one. 

## Quick start using uploaded version
Install browser extension from GitHub releases <releases/latest>

## Quick start using repository
1. Clone repository
2. Open Firefox
3. Navigate to `about:debugging#/runtime/this-firefox`
4. "Load Temporary Add-on..."
5. Select the manifest in browser-extension folder
6. Note, the extension is only loaded until you close your firefox

## Compatibility
- Firefox Version >= 48.0
- Android für Firefox Version >= 120.0a1
- Google Chome (untested)
- Microsoft Edge (untested)

## Known bugs
- Pages are reloaded even if normal youtube do not requires to (hotfix)
- Ad-Free Player appears only after ~1s
- If video is started before the ad-free player is loaded, the video runs in background (->reload page)