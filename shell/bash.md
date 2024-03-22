# Useful tidbits to know for bash scripting

- &> means to send both stderr and stdout to some file. `1>` (abbreviated as just
  `>` most commonly) means redirect stdout to a different file, `2>` = redirect
  stderr in a similar manner
    - adding in `&` means something is a file descriptor and not a filename, so
      when you do `>&2` it means redirect to the stderr file descriptor
- `>>` means to append whatever message to the respective file, rather than
  redirecting and overwriting the existing content

