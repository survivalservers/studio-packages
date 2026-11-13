// The module path is a placeholder: it changes to the public repository's address when the tool is published.
module github.com/survivalservers/studio-go/cli

go 1.25.0

toolchain go1.27.3

require (
	github.com/survivalservers/studio-go v0.0.0
	github.com/survivalservers/studio-go/localapi v0.0.0
	github.com/survivalservers/studio-go/mcp v0.0.0
)

require (
	github.com/google/jsonschema-go v0.4.3 // indirect
	github.com/modelcontextprotocol/go-sdk v1.8.0 // indirect
	github.com/segmentio/asm v1.1.3 // indirect
	github.com/segmentio/encoding v0.5.4 // indirect
	github.com/yosida95/uritemplate/v3 v3.0.2 // indirect
	golang.org/x/oauth2 v0.35.0 // indirect
	golang.org/x/sync v0.20.0 // indirect
	golang.org/x/sys v0.41.0 // indirect
	golang.org/x/time v0.15.0 // indirect
)

// The shared API client, the local API (survivalservers dev) and the MCP server (survivalservers mcp) live next to
// this module until they are published.
replace (
	github.com/survivalservers/studio-go => ../client
	github.com/survivalservers/studio-go/localapi => ../localapi
	github.com/survivalservers/studio-go/mcp => ../mcp
)
