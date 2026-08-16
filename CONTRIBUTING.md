# Contributing

Thank you for helping improve Open I-Lang. This repository is maintained as a specification project, so clarity, compatibility, and reviewability matter more than volume.

## Contribution Types

Useful contributions include:

- Clarifying normative language in `docs/spec/`.
- Adding examples that cover a new implementation scenario.
- Improving the terminology dictionary.
- Tightening validation scripts or CI checks.
- Reporting ambiguity, unsafe assumptions, or compatibility gaps.

## Specification Changes

Before proposing a breaking grammar change, open an issue that describes:

- the problem with the current behavior,
- at least one example message,
- the compatibility impact,
- how existing examples should migrate.

Breaking changes should be reserved for minor or major version updates. Editorial fixes may be submitted directly as pull requests.

## Pull Request Checklist

Before opening a pull request:

1. Run `python scripts/check_repo.py`.
2. Add or update examples when behavior changes.
3. Update `docs/dictionary.md` when introducing a new protocol term.
4. Keep each pull request focused on one topic.
5. Avoid copying text, examples, or grammar from other protocol projects.

## Writing Style

Use direct language. Prefer short normative statements over long explanations. When a rule is mandatory, use `must`. When a rule is recommended but not required, use `should`.

## Review Expectations

Maintainers may ask contributors to split large changes. A proposal is ready to merge when it is understandable, independently written, covered by examples when relevant, and passes CI.
