# Directives

Directives are line-oriented controls that refine how a receiver should process a message. They are optional unless the selected message family requires them.

## Syntax

```oilang
@directive-name value
```

Directive names use lowercase words separated by hyphens. Values are plain text unless a directive defines a stricter format.

## Standard Directives

### `@priority`

Communicates scheduling preference.

Allowed values:

- `low`
- `normal`
- `high`
- `urgent`

### `@deadline`

Declares an expected completion time in ISO 8601 form.

```oilang
@deadline 2026-08-20T12:00:00Z
```

### `@format`

Requests a result format.

```oilang
@format markdown
@format json
@format patch
```

### `@evidence`

Requires the receiver to attach or cite supporting material in the reply.

```oilang
@evidence required
```

### `@risk`

Marks the expected operational risk of the request.

Allowed values:

- `read-only`
- `writes-local`
- `writes-remote`
- `security-sensitive`

## Required Directives

A directive beginning with `@must-` is mandatory for receivers that claim compatibility with the surrounding message. Unknown `@must-` directives cause rejection.

Example:

```oilang
@must-review-owner security
```

## Conflict Handling

If two directives conflict, the receiver should prefer the safer interpretation and return a `receipt` describing the conflict.
