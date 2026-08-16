# Message Envelope

The message envelope is the stable outer structure of an Open I-Lang record. It tells a receiver what kind of message is being sent, who produced it, who should process it, and which body content belongs to the request.

## Required Shape

```oilang
@open-ilang 0.1
message <family> id=<stable-id>
from <role>:<name>
to <role>:<name>
intent <verb-or-label>
body:
  <freeform or structured payload>
end
```

## Fields

### `message`

Declares the message family and stable message id.

The id must be unique within the conversation or workflow that carries the record. Implementations may use UUIDs, trace ids, or monotonic local ids.

### `from`

Identifies the sender. The role prefix must be one of:

- `human`
- `agent`
- `tool`
- `system`
- `service`

### `to`

Identifies the intended receiver. Broadcast behavior is transport-specific and is not defined by this specification.

### `intent`

Summarizes the requested or reported action. It should be short, stable, and machine-routable. Examples include `summarize`, `plan`, `execute`, `confirm`, `refuse`, and `audit`.

### `scope`

Optional. Declares the resource or boundary affected by the message. Scope is descriptive; it does not grant permission to read, write, or execute against that boundary.

```oilang
scope repository:ziyuAZY/open-ilang-spec
scope document:architecture-note
scope session:handoff-2026-08-16
```

### `requires`

Optional. Lists named capabilities or permissions required before the receiver can act.

```oilang
requires read.repository
requires write.issue
requires approval.human
```

### `body`

The body starts with `body:` and ends at the matching `end`. Content is interpreted by the message family and implementation.

## Parsing Notes

- Blank lines are allowed between fields.
- Field names are lowercase ASCII identifiers.
- Unknown fields are allowed unless they start with `must.`.
- A receiver must not execute a `tool.request` without checking `requires` and local authorization.
