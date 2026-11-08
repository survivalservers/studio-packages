# @survivalservers/studio

The JavaScript and TypeScript package of Survival Servers Studio, game server hosting for studios by Survival
Servers: https://studio.survivalservers.com/

The client for the Studio API is not released yet. It will come as a later version of this package.

This first version has one helper, `docsUrl()`, which returns the address of a Studio docs page:

```js
import { docsUrl } from "@survivalservers/studio";

docsUrl();                        // 'https://studio.survivalservers.com/docs/'
docsUrl("guides/api-clients/");   // 'https://studio.survivalservers.com/docs/guides/api-clients/'
```

It has no dependencies, makes no network calls and runs nothing when installed.

Published from https://github.com/survivalservers/studio-packages. Licence: Apache-2.0.
