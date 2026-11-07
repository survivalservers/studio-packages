# survivalservers-studio

The Python package of Survival Servers Studio, game server hosting for studios by Survival Servers:
https://studio.survivalservers.com/

The Python client for the Studio API is not released yet. It will come as a later version of this package.

This first version has one helper, `docs_url()`, which returns the address of a Studio docs page:

```python
from survivalservers_studio import docs_url

docs_url()                        # 'https://studio.survivalservers.com/docs/'
docs_url("guides/api-clients/")   # 'https://studio.survivalservers.com/docs/guides/api-clients/'
```

It has no dependencies, makes no network calls and runs nothing when installed.

Published from https://github.com/survivalservers/studio-packages. Licence: Apache-2.0.
