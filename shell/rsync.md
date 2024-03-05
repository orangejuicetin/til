# `rsync` vs `scp`

`rsync` more modern and recommended by OpenSSH (or `sftp` too), so it's more
ideal for us to use this one instead. 

- `--archive, -a` is useful over `--recursive` because it additionally copies
  symlinks without resolving
    - if you're syncing over a folder, MAKE SURE TO PUT A `\` AT THE END OF THE
      SOURCE FOLDER NAME, otherwise it'll copy over that folder directly instead of its
      contents. (the dst doesn't matter as much)
    - e.g. `rsync --archive --rsh 'ssh' -v ~/folder/src 192.0.<etc.>:~/dst`
- `-P` as `--partial --progress` lets you run it again if process was
  interrupted midway through as it'll keep partially transferred files if
  interrupted
- `--rsh 'ssh -p <port>'` lets you specify different port than default of 22 and
  makes sure that it uses SSH protocol

