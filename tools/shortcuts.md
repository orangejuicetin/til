# Vim Setup + Shortcuts

Included my `.vimrc` in my
[.dotfiles](https://github.com/orangejuicetin/dotfiles)
repo, but current setup includes
[`ripgrep`](https://github.com/BurntSushi/ripgrep),
[`fzf`](https://github.com/junegunn/fzf) with the
[`fzf.vim`](https://github.com/junegunn/fzf.vim)
plugin, and `tmux` as a good 'ol reliable multiplexer. 

Thought that I'd write down any shortcuts that I find really helpful so that 
I don't have to repetitively look em up in the future. 

## `vim`
- Using `<C-c>` instead of Esc definitely quicker, get used to it 
- `<C-r>` as a "Undo" in Normal mode
- `:set paste!` to toggle the paste mode, when `PASTE` mode is on then 
Vim won't mangle the formatting of pasted code from auto-indenting 
- `=` will fix indentation, `=G` at top of file will re-indent til the end
- `gq{motion}` will format the line that `{motion}` moves over (e.g. `gqq` 
for single line, `gqip` for whole paragraph, 3 lines is `gq2j`, etc.)
    - `gw` is an alternate that puts your cursor back to where it originally
      was before-hand
- `<C-o>` puts you in `NORMAL` mode for one command before putting you back in 
`INSERT` mode.

### Ex commands (shoutout to fzf.vim)
- `:Rg` in order to bring up the general search command
- `:Files` in order to fuzzy find your files
- `:Rg <C-r><C-w>` to look up the word that's under your cursor in Normal mode 
- `:Man` in order to open `man` pages on a given sys call in Unix

## `fzf`
- `<C-r>` has been improved with `fzf` installation to be a more interactive
fuzzy backwards find of your command history woot woot

## `tmux`
- `<C-b>` prefix!
- `<C-b> $` to rename session
- `<C-b> ,` to rename window
- `<C-b> &` to close window 
- `<C-b> c` to create new window
- `<C-b> l` to toggle last active window
- `<C-b> x` to close pane
- `<C-b> %` to open pane vertically
- `<C-b> "` to open pane horizontally

