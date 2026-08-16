# Open I-Lang Spec

Open I-Lang defines a small message envelope, a shared vocabulary, and portable examples for handing work between assistants, tools, agents, and automation runtimes. It is an open specification for predictable AI-to-AI and human-to-AI task communication.

This repository is an independent rewrite for the `open-ilang-spec` project. It does not copy the wording, grammar, or examples of any upstream protocol project. The goal is to provide a clear, vendor-neutral base that maintainers can evolve in public.在中文团队协作场景里，它也可以作为需求交接、工具调用记录和 Agent 执行回执的统一表达方式。

## What This Project Provides

- A protocol specification for task messages, agent replies, tool requests, and execution receipts.
- A terminology dictionary for consistent discussion across implementations.
- Syntax examples that show conversational, operational, and automation use cases.
- Repository checks that keep Markdown, examples, and metadata consistent.
- Contribution and security policies suitable for an open standards project.

## Who Should Use It

Open I-Lang is designed for:

- AI application developers who need stable handoff formats between assistants and tools.
- Agent framework maintainers who want a simple interchange layer.
- Researchers comparing task protocols without depending on one vendor runtime.
- Documentation authors who need unambiguous examples for AI workflow contracts.
- Security reviewers who need traceable permissions and execution intent.

## Quick Start

Read the overview first:

```text
docs/overview.md
```

Then inspect the core model:

```text
docs/spec/message-envelope.md
docs/spec/directives.md
docs/spec/execution-model.md
```

A minimal Open I-Lang message looks like this:

```oilang
@open-ilang 0.1
message task.request id=req-001
from human:alice
to agent:planner
intent summarize
scope document:brief
body:
  produce a one-page summary with risks and next actions
end
```

Validate repository content locally with:

```bash
python scripts/check_repo.py
```

## Repository Layout

```text
docs/              protocol documentation
examples/          runnable and readable syntax samples
scripts/           lightweight validation scripts
.github/workflows/ continuous integration checks
```

## Maintenance Plan

The initial `0.1` line is documentation-first. Maintainers should treat breaking grammar changes as design proposals, not casual edits.

Planned maintenance cadence:

- Patch updates: typo fixes, clarifications, and new examples as needed.
- Minor updates: vocabulary additions and backward-compatible directive changes.
- Review cycle: every quarter, review open issues and mark accepted, rejected, or deferred proposals.
- Compatibility rule: examples in `examples/` must remain valid for the current documented version.

## License

Released under the MIT License. See `LICENSE`.
