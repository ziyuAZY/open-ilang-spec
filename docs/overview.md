# Overview

Open I-Lang describes how participants express work, constraints, evidence, and results in a form that is easy for both humans and AI systems to inspect.

The protocol is intentionally small. It does not define model behavior, prompt strategy, authentication, or transport. Those concerns belong to implementations. Open I-Lang only defines the shape and meaning of exchanged task records.

## Design Goals

1. Be readable before it is executable.
2. Make intent, authority, and expected output explicit.
3. Preserve enough structure for validation and automated routing.
4. Keep transport neutral so the same message can travel through files, APIs, queues, or chat systems.
5. Avoid hidden control flow. A receiver should be able to inspect the message and understand the requested action.

## Non-Goals

Open I-Lang is not:

- A prompt injection defense by itself.
- A replacement for application authorization.
- A binary serialization format.
- A model training data format.
- A workflow engine.

## Version Line

Every standalone document starts with a version line:

```oilang
@open-ilang 0.1
```

The version identifies the grammar and vocabulary expectations for the rest of the document.

## Message Families

Open I-Lang uses message families instead of many unrelated object types:

- `task.request`: asks another participant to perform work.
- `task.update`: changes scope, priority, or constraints.
- `tool.request`: asks a tool executor to perform a bounded action.
- `tool.result`: reports the result of a tool execution.
- `agent.reply`: returns reasoning summary, output, or refusal.
- `receipt`: records acceptance, rejection, completion, or failure.

## Compatibility

A receiver may ignore unknown optional fields. A receiver must reject unknown required directives when the directive name starts with `must.`.
