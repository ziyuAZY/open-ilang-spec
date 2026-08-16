# Terminology Dictionary

This dictionary defines the vocabulary used by Open I-Lang documents and examples.

## Agent

A software participant that can interpret a message, decide a next step, and return a structured reply.

## Authority

The permission boundary that decides whether a participant may perform a requested action. Authority is external to the protocol.

## Body

The message section between `body:` and `end`. It carries the human-readable or structured payload.

## Directive

A line beginning with `@` that changes processing expectations for a message.

## Envelope

The required outer structure of an Open I-Lang message, including version, family, sender, receiver, intent, and body.

## Evidence

Material used to justify a reply, such as logs, file paths, citations, traces, or command output summaries.

## Family

The category after the `message` keyword, such as `task.request`, `tool.result`, or `receipt`.

## Intent

A compact action label that helps route or classify a message.

## Participant

Any sender or receiver in an exchange. A participant may be a human, agent, tool, system, or service.

## Receipt

A message that records acceptance, rejection, completion, failure, or the need for clarification.

## Scope

The declared boundary affected by a message. Scope does not grant access; it describes what the message refers to.

## Tool

A bounded executor that performs an operation on behalf of a participant and reports a result.

## Transport

The channel that carries messages, such as a file, HTTP endpoint, queue, repository issue, or chat session.
