# Execution Model

Open I-Lang separates intention from execution. A message may ask for work, but an implementation decides whether the sender has authority and whether the receiver is able to perform the action.

## Lifecycle

A typical exchange follows this sequence:

1. `task.request` describes desired work.
2. `receipt` accepts, rejects, or asks for clarification.
3. `tool.request` records any delegated operation.
4. `tool.result` captures the operation result.
5. `agent.reply` returns the final response or next step.

## Receipts

Receipts give a compact state transition.

```oilang
@open-ilang 0.1
message receipt id=rcpt-001
from agent:builder
to human:alice
intent accepted
scope request:req-001
body:
  accepted for implementation; no external credentials required
end
```

Receipt intents:

- `accepted`
- `rejected`
- `needs-clarification`
- `blocked`
- `completed`
- `failed`

## Tool Requests

Tool requests must be bounded. A receiver should reject tool requests that lack scope, authority, or rollback expectations.

Recommended fields:

```oilang
requires write.repository
scope repository:owner/name
@risk writes-remote
```

## Failure Semantics

Failures should be explicit and recoverable. A failed message should include:

- the failed stage,
- the observable error,
- whether retry is safe,
- any partial effects already committed.

## Security Boundary

Open I-Lang does not grant permission. It records requested permission. Implementations must apply their own authorization policy before executing actions.
