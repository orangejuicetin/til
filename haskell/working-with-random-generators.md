# Setting up random number generators using State Transformers

Was having trouble figuring out a replacement for `PureMT` from `Data.Random.Source`, but shoutout to Alex Chen SP1'20 from RC, because he essentially helped me walk through State Transformers properly for the first time in trying to set this up 

[uniformR](https://hackage.haskell.org/package/random-1.2.1.1/docs/System-Random.html#v:uniformR) is the best way to partially apply with a range input, and from there have something that takes in a state (in this case, our `RandomGen` g) - this state is of type `StdGen`, an instance of the `RandomGen` interface, which we instantiate with [initStdGen](https://hackage.haskell.org/package/random-1.2.1.1/docs/System-Random.html#v:initStdGen). 

Taking the partially applied/curried `uniformR` function, we can then pass that into [`state`](https://hackage.haskell.org/package/transformers-0.6.1.1/docs/Control-Monad-Trans-State-Lazy.html#v:state) from the monad transfomrers package (in our case, we stuck with the lazy `StateT` monad.) in order to get us a `Double` value for our RGB values

All code can be found in the [functional_art repo](https://github.com/orangejuicetin/functional_art) for further reference in `Main.hs` 
