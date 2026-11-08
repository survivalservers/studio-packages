# survivalservers-studio

The Rust crate of Survival Servers Studio, game server hosting for studios by Survival Servers:
https://studio.survivalservers.com/

The Rust client for the Studio API is not released yet. It will come as a later version of this crate.

This first version has one helper, `docs_url()`, which returns the address of a Studio docs page:

```rust
use survivalservers_studio::docs_url;

assert_eq!(docs_url(""), "https://studio.survivalservers.com/docs/");
assert_eq!(docs_url("guides/api-clients/"), "https://studio.survivalservers.com/docs/guides/api-clients/");
```

It has no dependencies, no build script and makes no network calls.

Published from https://github.com/survivalservers/studio-packages. Licence: Apache-2.0.
