//! Survival Servers Studio, game server hosting for studios by Survival Servers.
//!
//! The Rust client for the Studio API is not released yet. This first version has one helper, [`docs_url`].

/// The address of the Survival Servers Studio docs.
pub const DOCS_URL: &str = "https://studio.survivalservers.com/docs/";

/// Return the address of a Survival Servers Studio docs page, for example `docs_url("guides/api-clients/")`.
pub fn docs_url(page: &str) -> String {
    format!("{}{}", DOCS_URL, page.trim_start_matches('/'))
}

#[cfg(test)]
mod tests {
    #[test]
    fn docs_url_joins_the_page() {
        assert_eq!(super::docs_url(""), "https://studio.survivalservers.com/docs/");
        assert_eq!(
            super::docs_url("/guides/api-clients/"),
            "https://studio.survivalservers.com/docs/guides/api-clients/"
        );
    }
}
