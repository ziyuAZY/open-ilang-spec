# Security Policy

Open I-Lang is a specification and documentation repository. It does not ship an execution runtime, but protocol wording can still affect downstream security decisions.

## Supported Versions

The current supported specification line is:

| Version | Status |
| --- | --- |
| 0.1 | Draft, actively reviewed |

## Reporting Security Issues

Please report security concerns through a private channel when possible. If GitHub private vulnerability reporting is enabled for this repository, use it. Otherwise, contact the repository owner through the contact method listed on the GitHub profile.

Do not open a public issue for a concern that includes a working exploit, credential, private endpoint, or sensitive operational detail.

## What Counts as Security-Relevant

Examples include:

- Wording that appears to grant authority without an external authorization check.
- Examples that encourage unsafe tool execution.
- Ambiguous handling of remote writes, credentials, or secrets.
- Validation gaps that could hide malformed protocol examples.
- Documentation that makes prompt injection or privilege confusion more likely.

## Maintainer Response

Maintainers should acknowledge a private report, assess impact, prepare a fix, and publish a short advisory when the issue affects downstream implementations.

## Implementation Reminder

Open I-Lang records intent and scope. It never grants permission by itself. Implementations must enforce authentication, authorization, audit logging, and rollback policies outside the protocol layer.
