// Survival Servers Studio, game server hosting for studios by Survival Servers.
// The JavaScript and TypeScript client for the Studio API is not released yet. This first version has one helper.

export const DOCS_URL = "https://studio.survivalservers.com/docs/";

/** Return the address of a Survival Servers Studio docs page, for example docsUrl("guides/api-clients/"). */
export function docsUrl(page = "") {
  return DOCS_URL + String(page).replace(/^\/+/, "");
}
