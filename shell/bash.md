# Useful tidbits to know for bash scripting

- `>` is just the same thing as `1>`, which says "direct stdout to _____", while
  2 refers to stderr and so we always have to write `2>` to redirect it
  elsewhere.
    - adding in & just means to refer to wherever the stderr is at now, so &1,
      &2, &3 refer to stdin, stdout, and stderr respectively (or whatever file
      they've been redirected to)
- `>>` means to append whatever message to the respective file, rather than
  redirecting and overwriting the existing content

