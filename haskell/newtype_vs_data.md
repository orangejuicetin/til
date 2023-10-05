# `newtype` vs `data`

**tl;dr** - `newtype` has performance benefits as it erases the constructor at runtime, and your data will have the exact represetentation as the type that you wrap. However, it is thus limited in that you are allowed only a single data constructor on the right hand side. 

[This SO](https://stackoverflow.com/a/5889784) answer is where this differentiation was fleshed out – though `newtype` and `data` are similar, `data` has more overhead because it's more flexible and can be used to define more things, e.g. `data Maybe a = Nothing | Just a` would not be possible with just `newtype`, since `newtype` is limited, again, to one data constructor!!
