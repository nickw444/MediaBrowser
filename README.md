# MediaBrowser
A basic Flask based HTTP file browser/downloader/zipper

## Running in Docker
```
docker pull nickw444/mediabrowser
```

```
docker create -p 8080:8080 -v /mnt/my-host-media-volume/:/mnt/media1  -v /mnt/my-host-media-volume2/:/mnt/media2 -e ROOT_PATHS="/mnt/media:Media;/mnt/media2:Media2" --name="mediabrowser" nickw444/mediabrowser
```

You can specify unlimited media folders to share on the web interface. You will need to mount each volume from the host, however. 

```
docker start mediabrowser
```

#### Env Variables:

- `ROOT_PATHS`: List of volumes to display on the web interface in the format of: path:name;path:name;path:name. Omit the trailing semicolon. 
- `MAX_FOLDER_DL_GB`: Maximum size of a directory to ZIP. Defaults to `2` (2GB)
- `IGNORE_FILES_RE`: A regular expression of files to ignore. Defaults to `(^\..*$|^lost\+found$|^Temporary Items$|^Network Trash Folder$)`
