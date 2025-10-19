<!--
---
linkTitle: "Pipelines"
weight: 203
---
-->

# Pipelines

- [Pipelines](#pipelines)
  - [Overview](#overview)
  - [Configuring a `Pipeline`](#configuring-a-pipeline)
  - [Specifying `Workspaces`](#specifying-workspaces)
  - [Specifying `Parameters`](#specifying-parameters)
  - [Adding `Tasks` to the `Pipeline`](#adding-tasks-to-the-pipeline)
    - [Specifying Display Name](#specifying-displayname-in-pipelinetasks)
    - [Specifying Remote Tasks](#specifying-remote-tasks)
    - [Specifying `Pipelines` in `PipelineTasks`](#specifying-pipelines-in-pipelinetasks)
    - [Specifying `Parameters` in `PipelineTasks`](#specifying-parameters-in-pipelinetasks)
    - [Specifying `Matrix` in `PipelineTasks`](#specifying-matrix-in-pipelinetasks)
    - [Specifying `Workspaces` in `PipelineTasks`](#specifying-workspaces-in-pipelinetasks)
    - [Tekton Bundles](#tekton-bundles)
    - [Using the `runAfter` field](#using-the-runafter-field)
    - [Using the `retries` field](#using-the-retries-field)
    - [Using the `onError` field](#using-the-onerror-field)
    - [Produce results with `OnError`](#produce-results-with-onerror)
    - [Guard `Task` execution using `when` expressions](#guard-task-execution-using-when-expressions)
      - [Guarding a `Task` and its dependent `Tasks`](#guarding-a-task-and-its-dependent-tasks)
        - [Cascade `when` expressions to the specific dependent `Tasks`](#cascade-when-expressions-to-the-specific-dependent-tasks)
        - [Compose using Pipelines in Pipelines](#compose-using-pipelines-in-pipelines)
      - [Guarding a `Task` only](#guarding-a-task-only)
    - [Configuring the failure timeout](#configuring-the-failure-timeout)
  - [Using variable substitution](#using-variable-substitution)
    - [Using the `retries` and `retry-count` variable substitutions](#using-the-retries-and-retry-count-variable-substitutions)
  - [Using `Results`](#using-results)
    - [Passing one Task's `Results` into the `Parameters` or `when` expressions of another](#passing-one-tasks-results-into-the-parameters-or-when-expressions-of-another)
    - [Emitting `Results` from a `Pipeline`](#emitting-results-from-a-pipeline)
  - [Configuring the `Task` execution order](#configuring-the-task-execution-order)
  - [Adding a description](#adding-a-description)
  - [Adding `Finally` to the `Pipeline`](#adding-finally-to-the-pipeline)
    - [Specifying Display Name](#specifying-displayname-in-finally-tasks)
    - [Specifying `Workspaces` in `finally` tasks](#specifying-workspaces-in-finally-tasks)
    - [Specifying `Parameters` in `finally` tasks](#specifying-parameters-in-finally-tasks)
    - [Specifying `matrix` in `finally` tasks](#specifying-matrix-in-finally-tasks)
    - [Consuming `Task` execution results in `finally`](#consuming-task-execution-results-in-finally)
    - [Consuming `Pipeline` result with `finally`](#consuming-pipeline-result-with-finally)
    - [`PipelineRun` Status with `finally`](#pipelinerun-status-with-finally)
    - [Using Execution `Status` of `pipelineTask`](#using-execution-status-of-pipelinetask)
    - [Using Aggregate Execution `Status` of All `Tasks`](#using-aggregate-execution-status-of-all-tasks)
    - [Guard `finally` `Task` execution using `when` expressions](#guard-finally-task-execution-using-when-expressions)
      - [`when` expressions using `Parameters` in `finally` `Tasks`](#when-expressions-using-parameters-in-finally-tasks)
      - [`when` expressions using `Results` in `finally` 'Tasks`](#when-expressions-using-results-in-finally-tasks)
      - [`when` expressions using `Execution Status` of `PipelineTask` in `finally` `tasks`](#when-expressions-using-execution-status-of-pipelinetask-in-finally-tasks)
      - [`when` expressions using `Aggregate Execution Status` of `Tasks` in `finally` `tasks`](#when-expressions-using-aggregate-execution-status-of-tasks-in-finally-tasks)
    - [Known Limitations](#known-limitations)
      - [Cannot configure the `finally` task execution order](#cannot-configure-the-finally-task-execution-order)
  - [Using Custom Tasks](#using-custom-tasks)
    - [Specifying the target Custom Task](#specifying-the-target-custom-task)
    - [Specifying a Custom Task Spec in-line (or embedded)](#specifying-a-custom-task-spec-in-line-or-embedded)
    - [Specifying parameters](#specifying-parameters-1)
    - [Specifying matrix](#specifying-matrix)
    - [Specifying workspaces](#specifying-workspaces-1)
    - [Using `Results`](#using-results-1)
    - [Specifying `Timeout`](#specifying-timeout)
    - [Specifying `Retries`](#specifying-retries)
    - [Known Custom Tasks](#known-custom-tasks)
  - [Code examples](#code-examples)

## Overview

A `Pipeline` is a collection of `Tasks` that you define and arrange in a specific order
of execution as part of your continuous integration flow. Each `Task` in a `Pipeline`
executes as a `Pod` on your Kubernetes cluster. You can configure various execution
conditions to fit your business needs.

## Configuring a `Pipeline`

A `Pipeline` definition supports the following fields:

- Required:
  - [`apiVersion`][kubernetes-overview] - Specifies the API version, for example
    `tekton.dev/v1beta1`.
  - [`kind`][kubernetes-overview] - Identifies this resource object as a `Pipeline` object.
  - [`metadata`][kubernetes-overview] - Specifies metadata that uniquely identifies the
    `Pipeline` object. For example, a `name`.
  - [`spec`][kubernetes-overview] - Specifies the configuration information for
    this `Pipeline` object. This must include:
      - [`tasks`](#adding-tasks-to-the-pipeline) - Specifies the `Tasks` that comprise the `Pipeline`
        and the details of their execution.
- Optional:
  - [`params`](#specifying-parameters) - Specifies the `Parameters` that the `Pipeline` requires.
  - [`workspaces`](#specifying-workspaces) - Specifies a set of Workspaces that the `Pipeline` requires.
  - [`tasks`](#adding-tasks-to-the-pipeline):
      - [`name`](#adding-tasks-to-the-pipeline) - the name of this `Task` within the context of this `Pipeline`.
      - [`displayName`](#specifying-displayname-in-pipelinetasks) - a user-facing name of this `Task` within the context of this `Pipeline`.
      - [`description`](#adding-tasks-to-the-pipeline) - a description of this `Task` within the context of this `Pipeline`.
      - [`taskRef`](#adding-tasks-to-the-pipeline) - a reference to a `Task` definition.
      - [`taskSpec`](#adding-tasks-to-the-pipeline) - a specification of a `Task`.
      - [`runAfter`](#using-the-runafter-field) - Indicates that a `Task` should execute after one or more other
        `Tasks` without output linking.
      - [`retries`](#using-the-retries-field) - Specifies the number of times to retry the execution of a `Task` after
        a failure. Does not apply to execution cancellations.
      - [`when`](#guard-finally-task-execution-using-when-expressions) - Specifies `when` expressions that guard
        the execution of a `Task`; allow execution only when all `when` expressions evaluate to true.
      - [`timeout`](#configuring-the-failure-timeout) - Specifies the timeout before a `Task` fails.
      - [`params`](#specifying-parameters-in-pipelinetasks) - Specifies the `Parameters` that a `Task` requires.
      - [`workspaces`](#specifying-workspaces-in-pipelinetasks) - Specifies the `Workspaces` that a `Task` requires.
      - [`matrix`](#specifying-matrix-in-pipelinetasks) - Specifies the `Parameters` used to fan out a `Task` into
        multiple `TaskRuns` or `Runs`.
  - [`results`](#emitting-results-from-a-pipeline) - Specifies the location to which the `Pipeline` emits its execution
    results.
  - [`displayName`](#specifying-a-display-name) - is a user-facing name of the pipeline that may be used to populate a UI.
  - [`description`](#adding-a-description) - Holds an informative description of the `Pipeline` object.
  - [`finally`](#adding-finally-to-the-pipeline) - Specifies one or more `Tasks` to be executed in parallel after
    all other tasks have completed.
    - [`name`](#adding-finally-to-the-pipeline) - the name of this `Task` within the context of this `Pipeline`.
    - [`displayName`](#specifying-displayname-in-finally-tasks) - a user-facing name of this `Task` within the context of this `Pipeline`.
    - [`description`](#adding-finally-to-the-pipeline) - a description of this `Task` within the context of this `Pipeline`.
    - [`taskRef`](#adding-finally-to-the-pipeline) - a reference to a `Task` definition.
    - [`taskSpec`](#adding-finally-to-the-pipeline) - a specification of a `Task`.
    - [`retries`](#using-the-retries-field) - Specifies the number of times to retry the execution of a `Task` after
      a failure. Does not apply to execution cancellations.
    - [`when`](#guard-finally-task-execution-using-when-expressions) - Specifies `when` expressions that guard
      the execution of a `Task`; allow execution only when all `when` expressions evaluate to true.
    - [`timeout`](#configuring-the-failure-timeout) - Specifies the timeout before a `Task` fails.
    - [`params`](#specifying-parameters-in-finally-tasks) - Specifies the `Parameters` that a `Task` requires.
    - [`workspaces`](#specifying-workspaces-in-finally-tasks) - Specifies the `Workspaces` that a `Task` requires.
    - [`matrix`](#specifying-matrix-in-finally-tasks) - Specifies the `Parameters` used to fan out a `Task` into
      multiple `TaskRuns` or `Runs`.

[kubernetes-overview]:
  https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/#required-fields

## Specifying `Workspaces`

`Workspaces` allow you to specify one or more volumes that each `Task` in the `Pipeline`
requires during execution. You specify one or more `Workspaces` in the `workspaces` field.
For example:

```yaml
spec:
  workspaces:
    - name: pipeline-ws1 # The name of the workspace in the Pipeline
  tasks:
    - name: use-ws-from-pipeline
      taskRef:
        name: gen-code # gen-code expects a workspace with name "output"
      workspaces:
        - name: output
          workspace: pipeline-ws1
    - name: use-ws-again
      taskRef:
        name: commit # commit expects a workspace with name "src"
      runAfter:
        - use-ws-from-pipeline # important: use-ws-from-pipeline writes to the workspace first
      workspaces:
        - name: src
          workspace: pipeline-ws1
```

For simplicity you can also map the name of the `Workspace` in `PipelineTask` to match with
the `Workspace` from the `Pipeline`.
For example:

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: pipeline
spec:
  workspaces:
    - name: source
  tasks:
    - name: gen-code
      taskRef:
        name: gen-code # gen-code expects a Workspace named "source"
      workspaces:
        - name: source # <- mapping workspace name
    - name: commit
      taskRef:
        name: commit # commit expects a Workspace named "source"
      workspaces:
        - name: source # <- mapping workspace name
      runAfter:
        - gen-code
```

For more information, see:
- [Using `Workspaces` in `Pipelines`](workspaces.md#using-workspaces-in-pipelines)
- The [`Workspaces` in a `PipelineRun`](../examples/v1/pipelineruns/workspaces.yaml) code example
- The [variables available in a `PipelineRun`](variables.md#variables-available-in-a-pipeline), including `workspaces.<name>.bound`.
- [Mapping `Workspaces`](https://github.com/tektoncd/community/blob/main/teps/0108-mapping-workspaces.md)

## Specifying `Parameters`

(See also [Specifying Parameters in Tasks](tasks.md#specifying-parameters))

You can specify global parameters, such as compilation flags or artifact names, that you want to supply
to the `Pipeline` at execution time. `Parameters` are passed to the `Pipeline` from its corresponding
`PipelineRun` and can replace template values specified within each `Task` in the `Pipeline`.

Parameter names:
- Must only contain alphanumeric characters, hyphens (`-`), and underscores (`_`).
- Must begin with a letter or an underscore (`_`).

For example, `fooIs-Bar_` is a valid parameter name, but `barIsBa$` or `0banana` are not.

Each declared parameter has a `type` field, which can be set to either `array` or `string`.
`array` is useful in cases where the number of compilation flags being supplied to the `Pipeline`
varies throughout its execution. If no value is specified, the `type` field defaults to `string`.
When the actual parameter value is supplied, its parsed type is validated against the `type` field.
The `description` and `default` fields for a `Parameter` are optional.

The following example illustrates the use of `Parameters` in a `Pipeline`.

The following `Pipeline` declares two input parameters :

- `context` which passes its value (a string) to the `Task` to set the value of the `pathToContext` parameter within the `Task`.
- `flags` which passes its value (an array) to the `Task` to set the value of
  the `flags` parameter within the `Task`. The `flags` parameter within the
`Task` **must** also be an array.
If you specify a value for the `default` field and invoke this `Pipeline` in a `PipelineRun`
without specifying a value for `context`, that value will be used.

**Note:** Input parameter values can be used as variables throughout the `Pipeline`
by using [variable substitution](variables.md#variables-available-in-a-pipeline).

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: pipeline-with-parameters
spec:
  params:
    - name: context
      type: string
      description: Path to context
      default: /some/where/or/other
    - name: flags
      type: array
      description: List of flags
  tasks:
    - name: build-skaffold-web
      taskRef:
        name: build-push
      params:
        - name: pathToDockerFile
          value: Dockerfile
        - name: pathToContext
          value: "$(params.context)"
        - name: flags
          value: ["$(params.flags[*])"]
```

The following `PipelineRun` supplies a value for `context`:

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: pipelinerun-with-parameters
spec:
  pipelineRef:
    name: pipeline-with-parameters
  params:
    - name: "context"
      value: "/workspace/examples/microservices/leeroy-web"
    - name: "flags"
      value:
        - "foo"
        - "bar"
```

#### Param enum
> :seedling: **`enum` is an [alpha](additional-configs.md#alpha-features) feature.** The `enable-param-enum` feature flag must be set to `"true"` to enable this feature.

Parameter declarations can include `enum` which is a predefine set of valid values that can be accepted by the `Pipeline` `Param`. If a `Param` has both `enum` and default value, the default value must be in the `enum` set. For example, the valid/allowed values for `Param` "message" is bounded to `v1` and `v2`:

``` yaml
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-param-enum
spec:
  params:
  - name: message
    enum: ["v1", "v2"]
    default: "v1"
  tasks:
  - name: task1
    params:
      - name: message
        value: $(params.message)
    steps:
    - name: build
      image: bash:3.2
      script: |
        echo "$(params.message)"
```

If the `Param` value passed in by `PipelineRun` is **NOT** in the predefined `enum` list, the `PipelineRun` will fail with reason `InvalidParamValue`.

If a `PipelineTask` references a `Task` with `enum`, the `enums` specified in the Pipeline `spec.params` (pipeline-level `enum`) must be
a **subset** of the `enums` specified in the referenced `Task` (task-level `enum`). An empty pipeline-level `enum` is invalid
in this scenario since an empty `enum` set indicates a "universal set" which allows all possible values. The same rules apply to `Pipelines` with embbeded `Tasks`.

In the below example, the referenced `Task` accepts `v1` and `v2` as valid values, the `Pipeline` further restricts the valid value to `v1`.

``` yaml
apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: param-enum-demo
spec:
  params:
  - name: message
    type: string
    enum: ["v1", "v2"]
  steps:
  - name: build
    image: bash:latest
    script: |
      echo "$(params.message)"
```

``` yaml
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-param-enum
spec:
  params:
  - name: message
    enum: ["v1"]  # note that an empty enum set is invalid
  tasks:
  - name: task1
    params:
      - name: message
        value: $(params.message)
    taskRef:
      name: param-enum-demo
```

Note that this subset restriction only applies to the task-level `params` with a **direct single** reference to pipeline-level `params`. If a task-level `param` references multiple pipeline-level `params`, the subset validation is not applied.

``` yaml
apiVersion: tekton.dev/v1
kind: Pipeline
...
spec:
  params:
  - name: message1
    enum: ["v1"]
  - name: message2
    enum: ["v2"]
  tasks:
  - name: task1
    params:
      - name: message
        value: "$(params.message1) and $(params.message2)"
    taskSpec:
      params: message
      enum: [...] # the message enum is not required to be a subset of message1 or message2
    ...
```

Tekton validates user-provided values in a `PipelineRun` against the `enum` specified in the `PipelineSpec.params`. Tekton also validates
any resolved `param` value against the `enum` specified in each `PipelineTask` before creating the `TaskRun`.

See usage in this [example](../examples/v1/pipelineruns/alpha/param-enum.yaml)

#### Propagated Params

Like with embedded [pipelineruns](pipelineruns.md#propagated-parameters), you can propagate `params` declared in the `pipeline` down to the inlined `pipelineTasks` and its inlined `Steps`. Wherever a resource (e.g. a `pipelineTask`) or a `StepAction` is referenced, the parameters need to be passed explicitly. 

For example, the following is a valid yaml.

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: pipelien-propagated-params
spec:
  params:
    - name: HELLO
      default: "Hello World!"
    - name: BYE
      default: "Bye World!"
  tasks:
    - name: echo-hello
      taskSpec:
        steps:
          - name: echo
            image: ubuntu
            script: |
              #!/usr/bin/env bash
              echo "$(params.HELLO)"
    - name: echo-bye
      taskSpec:
        steps:
          - name: echo-action
            ref:
              name: step-action-echo
            params:
              - name: msg
                value: "$(params.BYE)" 
```
The same rules defined in [pipelineruns](pipelineruns.md#propagated-parameters) apply here.


## Adding `Tasks` to the `Pipeline`

 Your `Pipeline` definition must reference at least one [`Task`](tasks.md).
Each `Task` within a `Pipeline` must have a [valid](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names)
`name` and a `taskRef` or a `taskSpec`. For example:

```yaml
tasks:
  - name: build-the-image
    taskRef:
      name: build-push
```

**Note:** Using both `apiVersion` and `kind` will create [CustomRun](customruns.md), don't set `apiVersion` if only referring to [`Task`](tasks.md).

or

```yaml
tasks:
  - name: say-hello
    taskSpec:
      steps:
      - image: ubuntu
        script: echo 'hello there'
```

Note that any `task` specified in `taskSpec` will be the same version as the `Pipeline`.

### Specifying `displayName` in `PipelineTasks`

The `displayName` field is an optional field that allows you to add a user-facing name of the `PipelineTask` that can be
used to populate and distinguish in the dashboard. For example:

```yaml
spec:
  tasks:
    - name: scan
      displayName: "Code Scan"
      taskRef:
        name: sonar-scan
```

The `displayName` also allows you to parameterize the human-readable name of your choice based on the
[params](#specifying-parameters), [the task results](#passing-one-tasks-results-into-the-parameters-or-when-expressions-of-another),
and [the context variables](#context-variables). For example:

```yaml
spec:
  params:
    - name: application
  tasks:
    - name: scan
      displayName: "Code Scan for $(params.application)"
      taskRef:
        name: sonar-scan
    - name: upload-scan-report
      displayName: "Upload Scan Report $(tasks.scan.results.report)"
      taskRef:
        name: upload
```

Specifying task results in the `displayName` does not introduce an inherent resource dependency among `tasks`. The
pipeline author is responsible for specifying dependency explicitly either using [runAfter](#using-the-runafter-field)
or rely on [whenExpressions](#guard-task-execution-using-when-expressions) or [task results in params](#using-results).

Fully resolved `displayName` is also available in the status as part of the `pipelineRun.status.childReferences`. The
clients such as the dashboard, CLI, etc. can retrieve the `displayName` from the `childReferences`. The `displayName` mainly
drives a better user experience and at the same time it is not validated for the content or length by the controller.

### Specifying Remote Tasks

**([beta feature](https://github.com/tektoncd/pipeline/blob/main/docs/install.md#beta-features))**

A `taskRef` field may specify a Task in a remote location such as git.
Support for specific types of remote will depend on the Resolvers your
cluster's operator has installed. For more information including a tutorial, please check [resolution docs](resolution.md). The below example demonstrates referencing a Task in git:

```yaml
tasks:
- name: "go-build"
  taskRef:
    resolver: git
    params:
    - name: url
      value: https://github.com/tektoncd/catalog.git
    - name: revision
      # value can use params declared at the pipeline level or a static value like main
      value: $(params.gitRevision)
    - name: pathInRepo
      value: task/golang-build/0.3/golang-build.yaml
```

### Specifying `Pipelines` in `PipelineTasks`

> :seedling: **Specifying `pipelines` in `PipelineTasks` is an [alpha](additional-configs.md#alpha-features) feature.**
> The `enable-api-fields` feature flag must be set to `"alpha"` to specify `PipelineRef` or `PipelineSpec` in a `PipelineTask`.
> This feature is in **Preview Only** mode and not yet supported/implemented.

Apart from `taskRef` and `taskSpec`, `pipelineRef` and `pipelineSpec` allows you to specify a `pipeline`  in `pipelineTask`.
This allows you to generate a child `pipelineRun` which is inherited by the parent `pipelineRun`.

```
kind: Pipeline
metadata:
  name: security-scans
spec:
  tasks:
    - name: scorecards
      taskSpec:
        steps:
          - image: alpine
            name: step-1
            script: |
              echo "Generating scorecard report ..."
    - name: codeql
      taskSpec:
        steps:
          - image: alpine
            name: step-1
            script: |
              echo "Generating codeql report ..."
---
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: clone-scan-notify
spec:
  tasks:
    - name: git-clone
      taskSpec:
        steps:
          - image: alpine
            name: step-1
            script: |
              echo "Cloning a repo to run security scans ..."
    - name: security-scans
      runAfter:
        - git-clone
      pipelineRef:
        name: security-scans
---
```
For further information read [Pipelines in Pipelines](./pipelines-in-pipelines.md)


### Specifying `Parameters` in `PipelineTasks`

You can also provide [`Parameters`](tasks.md#specifying-parameters):

```yaml
spec:
  tasks:
    - name: build-skaffold-web
      taskRef:
        name: build-push
      params:
        - name: pathToDockerFile
          value: Dockerfile
        - name: pathToContext
          value: /workspace/examples/microservices/leeroy-web
```

### Specifying `Matrix` in `PipelineTasks`

> :seedling: **`Matrix` is an [beta](additional-configs.md#beta-features) feature.**
> The `enable-api-fields` feature flag can be set to `"beta"` to specify `Matrix` in a `PipelineTask`.

You can also provide [`Parameters`](tasks.md#specifying-parameters) through the `matrix` field:

```yaml
spec:
  tasks:
    - name: browser-test
      taskRef:
        name: browser-test
      matrix:
        params:
        - name: browser
          value:
          - chrome
          - safari
          - firefox
        include:
          - name: build-1
            params:
              - name: browser
                value: chrome
              - name: url
                value: some-url
```

For further information, read [`Matrix`](./matrix.md).

### Specifying `Workspaces` in `PipelineTasks`

You can also provide [`Workspaces`](tasks.md#specifying-workspaces):

```yaml
spec:
  tasks:
    - name: use-workspace
      taskRef:
        name: gen-code # gen-code expects a workspace with name "output"
      workspaces:
        - name: output
          workspace: shared-ws
```

### Tekton Bundles

A `Tekton Bundle` is an OCI artifact that contains Tekton resources like `Tasks` which can be referenced within a `taskRef`.

There is currently a hard limit of 20 objects in a bundle.

You can reference a `Tekton bundle` in a `TaskRef` in both `v1` and `v1beta1` using [remote resolution](./bundle-resolver.md#pipeline-resolution). The example syntax shown below for `v1` uses remote resolution and requires enabling [beta features](./additional-configs.md#beta-features).

```yaml
spec:
  tasks:
    - name: hello-world
      taskRef:
        resolver: bundles
        params:
        - name: bundle
          value: docker.io/myrepo/mycatalog
        - name: name
          value: echo-task
        - name: kind
          value: Task
```

You may also specify a `tag` as you would with a Docker image which will give you a fixed,
repeatable reference to a `Task`.

```yaml
spec:
  taskRef:
    resolver: bundles
    params:
    - name: bundle
      value: docker.io/myrepo/mycatalog:v1.0.1
    - name: name
      value: echo-task
    - name: kind
      value: Task
```

You may also specify a fixed digest instead of a tag.

```yaml
spec:
  taskRef:
    resolver: bundles
    params:
    - name: bundle
      value: docker.io/myrepo/mycatalog@sha256:abc123
    - name: name
      value: echo-task
    - name: kind
      value: Task
```

Any of the above options will fetch the image using the `ImagePullSecrets` attached to the
`ServiceAccount` specified in the `PipelineRun`.
See the [Service Account](pipelineruns.md#specifying-custom-serviceaccount-credentials) section
for details on how to configure a `ServiceAccount` on a `PipelineRun`. The `PipelineRun` will then
run that `Task` without registering it in the cluster allowing multiple versions of the same named
`Task` to be run at once.

`Tekton Bundles` may be constructed with any toolsets that produce valid OCI image artifacts
so long as the artifact adheres to the [contract](tekton-bundle-contracts.md).

### Using the `runAfter` field

If you need your `Tasks` to execute in a specific order within the `Pipeline`,
use the `runAfter` field to indicate that a `Task` must execute after
one or more other `Tasks`.

In the example below, we want to test the code before we build it. Since there
is no output from the `test-app` `Task`, the `build-app` `Task` uses `runAfter`
to indicate that `test-app` must run before it, regardless of the order in which
they are referenced in the `Pipeline` definition.

```yaml
workspaces:
- name: source
tasks:
- name: test-app
  taskRef:
    name: make-test
  workspaces:
  - name: source
    workspace: source
- name: build-app
  taskRef:
    name: kaniko-build
  runAfter:
    - test-app
  workspaces:
  - name: source
    workspace: source
```

### Using the `retries` field

For each `Task` in the `Pipeline`, you can specify the number of times Tekton
should retry its execution when it fails. When a `Task` fails, the corresponding
`TaskRun` sets its `Succeeded` `Condition` to `False`. The `retries` field
instructs Tekton to retry executing the `Task` when this happens. `retries` are executed
even when other `Task`s in the `Pipeline` have failed, unless the `PipelineRun` has
been [cancelled](./pipelineruns.md#cancelling-a-pipelinerun) or
[gracefully cancelled](./pipelineruns.md#gracefully-cancelling-a-pipelinerun).

If you expect a `Task` to encounter problems during execution (for example,
you know that there will be issues with network connectivity or missing
dependencies), set its `retries` field to a suitable value greater than 0.
If you don't explicitly specify a value, Tekton does not attempt to execute
the failed `Task` again.

In the example below, the execution of the `build-the-image` `Task` will be
retried once after a failure; if the retried execution fails, too, the `Task`
execution fails as a whole.

```yaml
tasks:
  - name: build-the-image
    retries: 1
    taskRef:
      name: build-push
```

### Using the `onError` field

When a `PipelineTask` fails, the rest of the `PipelineTasks` are skipped and the `PipelineRun` is declared a failure. If you would like to
ignore such `PipelineTask` failure and continue executing the rest of the `PipelineTasks`, you can specify `onError` for such a `PipelineTask`.

`OnError` can be set to `stopAndFail` (default) and `continue`. The failure of a `PipelineTask` with `stopAndFail` would stop and fail the whole `PipelineRun`.  A `PipelineTask` fails with `continue` does not fail the whole `PipelineRun`, and the rest of the `PipelineTask` will continue to execute.

To ignore a `PipelineTask` failure, set `onError` to `continue`:

``` yaml
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: demo
spec:
  tasks:
    - name: task1
      onError: continue
      taskSpec:
        steps:
          - name: step1
            image: alpine
            script: |
              exit 1
```

At runtime, the failure is ignored to determine the `PipelineRun` status. The `PipelineRun` `message` contains the ignored failure info:

``` yaml
status:
  conditions:
  - lastTransitionTime: "2023-09-28T19:08:30Z"
    message: 'Tasks Completed: 1 (Failed: 1 (Ignored: 1), Cancelled 0), Skipped: 0'
    reason: Succeeded
    status: "True"
    type: Succeeded
  ...
```

Note that the `TaskRun` status remains as it is irrelevant to `OnError`. Failed but ignored `TaskRuns` result in a `failed` status with reason
`FailureIgnored`.

For example, the `TaskRun` created by the above `PipelineRun` has the following status:

``` bash
$ kubectl get tr demo-run-task1
NAME                                SUCCEEDED   REASON           STARTTIME   COMPLETIONTIME
demo-run-task1                      False       FailureIgnored   12m         12m
```

To specify `onError` for a `step`, please see [specifying onError for a step](./tasks.md#specifying-onerror-for-a-step).

**Note:** Setting [`Retry`](#specifying-retries) and `OnError:continue` at the same time is **NOT** allowed.

### Produce results with `OnError`

When a `PipelineTask` is set to ignore error and the `PipelineTask` is able to initialize a result before failing, the result is made available to the consumer `PipelineTasks`.

``` yaml
  tasks:
    - name: task1
      onError: continue
      taskSpec:
        results:
          - name: result1
        steps:
          - name: step1
            image: alpine
            script: |
              echo -n 123 | tee $(results.result1.path)
              exit 1
```

The consumer `PipelineTasks` can access the result by referencing `$(tasks.task1.results.result1)`.

If the result is **NOT** initialized before failing, and there is a `PipelineTask` consuming it:

``` yaml
  tasks:
    - name: task1
      onError: continue
      taskSpec:
        results:
          - name: result1
        steps:
          - name: step1
            image: alpine
            script: |
              exit 1
              echo -n 123 | tee $(results.result1.path)
```

- If the consuming `PipelineTask` has `OnError:stopAndFail`, the `PipelineRun` will fail with `InvalidTaskResultReference`.
- If the consuming `PipelineTask` has `OnError:continue`, the consuming `PipelineTask` will be skipped with reason `Results were missing`,
and the `PipelineRun` will continue to execute.

### Guard `Task` execution using `when` expressions

To run a `Task` only when certain conditions are met, it is possible to _guard_ task execution using the `when` field. The `when` field allows you to list a series of references to `when` expressions.

The components of `when` expressions are `input`, `operator` and `values`:

| Component  | Description                                                                                                | Syntax                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `input`    | Input for the `when` expression, defaults to an empty string if not provided.                              | * Static values e.g. `"ubuntu"`<br/> * Variables ([parameters](#specifying-parameters) or [results](#using-results)) e.g. `"$(params.image)"` or `"$(tasks.task1.results.image)"` or `"$(tasks.task1.results.array-results[1])"`                                                                                                                                                                                                                                               |
| `operator` | `operator` represents an `input`'s relationship to a set of `values`, a valid `operator` must be provided. | `in` or `notin`                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `values`   | An array of string values, the `values` array must be provided and has to be non-empty.                    | * An array param e.g. `["$(params.images[*])"]`<br/> * An array result of a task `["$(tasks.task1.results.array-results[*])"]`<br/> * `values` can contain static values e.g. `"ubuntu"`<br/> * `values` can contain variables ([parameters](#specifying-parameters) or [results](#using-results)) or [a Workspaces's `bound` state](#specifying-workspaces) e.g. `["$(params.image)"]` or `["$(tasks.task1.results.image)"]` or `["$(tasks.task1.results.array-results[1])"]` |


The [`Parameters`](#specifying-parameters) are read from the `Pipeline` and [`Results`](#using-results) are read directly from previous [`Tasks`](#adding-tasks-to-the-pipeline). Using [`Results`](#using-results) in a `when` expression in a guarded `Task` introduces a resource dependency on the previous `Task` that produced the `Result`.

The declared `when` expressions are evaluated before the `Task` is run. If all the `when` expressions evaluate to `True`, the `Task` is run. If any of the `when` expressions evaluate to `False`, the `Task` is not run and the `Task` is listed in the [`Skipped Tasks` section of the `PipelineRunStatus`](pipelineruns.md#monitoring-execution-status).

In these examples, `first-create-file` task will only be executed if the `path` parameter is `README.md`, `echo-file-exists` task will only be executed if the `exists` result from `check-file` task is `yes` and `run-lint` task will only be executed if the `lint-config` optional workspace has been provided by a PipelineRun.

```yaml
tasks:
  - name: first-create-file
    when:
      - input: "$(params.path)"
        operator: in
        values: ["README.md"]
    taskRef:
      name: first-create-file
---
tasks:
  - name: echo-file-exists
    when:
      - input: "$(tasks.check-file.results.exists)"
        operator: in
        values: ["yes"]
    taskRef:
      name: echo-file-exists
---
tasks:
  - name: run-lint
    when:
      - input: "$(workspaces.lint-config.bound)"
        operator: in
        values: ["true"]
    taskRef:
      name: lint-source
---
tasks:
  - name: deploy-in-blue
    when:
      - input: "blue"
        operator: in
        values: ["$(params.deployments[*])"]
    taskRef:
      name: deployment
```

For an end-to-end example, see [PipelineRun with `when` expressions](../examples/v1/pipelineruns/pipelinerun-with-when-expressions.yaml).

There are a lot of scenarios where `when` expressions can be really useful. Some of these are:
- Checking if the name of a git branch matches
- Checking if the `Result` of a previous `Task` is as expected
- Checking if a git file has changed in the previous commits
- Checking if an image exists in the registry
- Checking if the name of a CI job matches
- Checking if an optional Workspace has been provided

#### Use CEL expression in WhenExpression

> :seedling: **`CEL in WhenExpression` is an [alpha](additional-configs.md#alpha-features) feature.**
> The `enable-cel-in-whenexpression` feature flag must be set to `"true"` to enable the use of `CEL` in `WhenExpression`.

CEL (Common Expression Language) is a declarative language designed for simplicity, speed, safety, and portability which can be used to express a wide variety of conditions and computations.

You can define a CEL expression in `WhenExpression` to guard the execution of a `Task`.  The CEL expression must evaluate to either `true` or `false`. You can use a single line of CEL string to replace current `WhenExpressions`'s `input`+`operator`+`values`. For example:

```yaml
# current WhenExpressions
when:
  - input: "foo"
    operator: "in"
    values: ["foo", "bar"]
  - input: "duh"
    operator: "notin"
    values: ["foo", "bar"]

# with cel
when:
  - cel: "'foo' in ['foo', 'bar']"
  - cel: "!('duh' in ['foo', 'bar'])"
```

CEL can offer more conditional functions, such as numeric comparisons (e.g. `>`, `<=`, etc), logic operators (e.g. `OR`, `AND`), Regex Pattern Matching. For example:

```yaml
  when:
    # test coverage result is larger than 90%
    - cel: "'$(tasks.unit-test.results.test-coverage)' > 0.9"
    # params is not empty, or params2 is 8.5 or 8.6
    - cel: "'$(params.param1)' != '' || '$(params.param2)' == '8.5' || '$(params.param2)' == '8.6'"
    # param branch matches pattern `release/.*`
    - cel: "'$(params.branch)'.matches('release/.*')"
```

##### Variable substitution in CEL

`CEL` supports [string substitutions](https://github.com/tektoncd/pipeline/blob/main/docs/variables.md#variables-available-in-a-pipeline), you can reference string, array indexing or object value of a param/result. For example:

```yaml
  when:
    # string result
    - cel: "$(tasks.unit-test.results.test-coverage) > 0.9"
    # array indexing result
    - cel: "$(tasks.unit-test.results.test-coverage[0]) > 0.9"
    # object result key
    - cel: "'$(tasks.objectTask.results.repo.url)'.matches('github.com/tektoncd/.*')"
    # string param
    - cel: "'$(params.foo)' == 'foo'"
    # array indexing
    - cel: "'$(params.branch[0])' == 'foo'"
    # object param key
    - cel: "'$(params.repo.url)'.matches('github.com/tektoncd/.*')"
```

**Note:** the reference needs to be wrapped with single quotes.
Whole `Array` and `Object` replacements are not supported yet. The following usage is not supported:

```yaml
  when:
    - cel: "'foo' in '$(params.array_params[*])'"
    - cel: "'foo' in '$(params.object_params[*])'"
```
<!-- wokeignore:rule=master -->
In addition to the cases listed above, you can craft any valid CEL expression as defined by the [cel-spec language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md)


`CEL` expression is validated at admission webhook and a validation error will be returned if the expression is invalid.

**Note:** To use Tekton's [variable substitution](variables.md), you need to wrap the reference with single quotes. This also means that if you pass another CEL expression via `params` or `results`, it won't be executed. Therefore CEL injection is disallowed.

For example:
```
This is valid: '$(params.foo)' == 'foo'
This is invalid: $(params.foo) == 'foo'
CEL's variable substitution is not supported yet and thus invalid: params.foo == 'foo'
```

#### Guarding a `Task` and its dependent `Tasks`

To guard a `Task` and its dependent Tasks:
- cascade the `when` expressions to the specific dependent `Tasks` to be guarded as well
- compose the `Task` and its dependent `Tasks` as a unit to be guarded and executed together using `Pipelines` in `Pipelines`

##### Cascade `when` expressions to the specific dependent `Tasks`

Pick and choose which specific dependent `Tasks` to guard as well, and cascade the `when` expressions to those `Tasks`.

Taking the use case below, a user who wants to guard `manual-approval` and its dependent `Tasks`:

```
                                     tests
                                       |
                                       v
                                 manual-approval
                                 |            |
                                 v        (approver)
                            build-image       |
                                |             v
                                v          slack-msg
                            deploy-image
```

The user can design the `Pipeline` to solve their use case as such:

```yaml
tasks:
#...
- name: manual-approval
  runAfter:
    - tests
  when:
    - input: $(params.git-action)
      operator: in
      values:
        - merge
  taskRef:
    name: manual-approval

- name: build-image
  when:
    - input: $(params.git-action)
      operator: in
      values:
        - merge
  runAfter:
    - manual-approval
  taskRef:
    name: build-image

- name: deploy-image
  when:
    - input: $(params.git-action)
      operator: in
      values:
        - merge
  runAfter:
    - build-image
  taskRef:
    name: deploy-image

- name: slack-msg
  params:
    - name: approver
      value: $(tasks.manual-approval.results.approver)
  taskRef:
    name: slack-msg
```

##### Compose using Pipelines in Pipelines

Compose a set of `Tasks` as a unit of execution using `Pipelines` in `Pipelines`, which allows for guarding a `Task` and
its dependent `Tasks` (as a sub-`Pipeline`) using `when` expressions.

**Note:** `Pipelines` in `Pipelines` is an [experimental feature](https://github.com/tektoncd/experimental/tree/main/pipelines-in-pipelines)

Taking the use case below, a user who wants to guard `manual-approval` and its dependent `Tasks`:

```
                                     tests
                                       |
                                       v
                                 manual-approval
                                 |            |
                                 v        (approver)
                            build-image       |
                                |             v
                                v          slack-msg
                            deploy-image
```

The user can design the `Pipelines` to solve their use case as such:

```yaml
## sub pipeline (approve-build-deploy-slack)
tasks:
  - name: manual-approval
    runAfter:
      - integration-tests
    taskRef:
      name: manual-approval

  - name: build-image
    runAfter:
      - manual-approval
    taskRef:
      name: build-image

  - name: deploy-image
    runAfter:
      - build-image
    taskRef:
      name: deploy-image

  - name: slack-msg
    params:
      - name: approver
        value: $(tasks.manual-approval.results.approver)
    taskRef:
      name: slack-msg

---
## main pipeline
tasks:
#...
- name: approve-build-deploy-slack
  runAfter:
    - tests
  when:
    - input: $(params.git-action)
      operator: in
      values:
        - merge
  taskRef:
    apiVersion: tekton.dev/v1beta1
    kind: Pipeline
    name: approve-build-deploy-slack
```

#### Guarding a `Task` only

When `when` expressions evaluate to `False`, the `Task` will be skipped and:
- The ordering-dependent `Tasks` will be executed
- The resource-dependent `Tasks` (and their dependencies) will be skipped because of missing `Results` from the skipped
  parent `Task`. When we add support for [default `Results`](https://github.com/tektoncd/community/pull/240), then the
  resource-dependent `Tasks` may be executed if the default `Results` from the skipped parent `Task` are specified. In
  addition, if a resource-dependent `Task` needs a file from a guarded parent `Task` in a shared `Workspace`, make sure
  to handle the execution of the child `Task` in case the expected file is missing from the `Workspace` because the
  guarded parent `Task` is skipped.

On the other hand, the rest of the `Pipeline` will continue executing.

```
                                     tests
                                       |
                                       v
                                 manual-approval
                                 |            |
                                 v        (approver)
                            build-image       |
                                |             v
                                v          slack-msg
                            deploy-image
```

Taking the use case above, a user who wants to guard `manual-approval` only can design the `Pipeline` as such:

```yaml
tasks:
#...
- name: manual-approval
  runAfter:
    - tests
  when:
    - input: $(params.git-action)
      operator: in
      values:
        - merge
  taskRef:
    name: manual-approval

- name: build-image
  runAfter:
    - manual-approval
  taskRef:
    name: build-image

- name: deploy-image
  runAfter:
    - build-image
  taskRef:
    name: deploy-image

- name: slack-msg
  params:
    - name: approver
      value: $(tasks.manual-approval.results.approver)
  taskRef:
    name: slack-msg
```

If `manual-approval` is skipped, execution of its dependent `Tasks` (`slack-msg`, `build-image` and `deploy-image`)
would be unblocked regardless:
- `build-image` and `deploy-image` should be executed successfully
- `slack-msg` will be skipped because it is missing the `approver` `Result` from `manual-approval`
  - dependents of `slack-msg` would have been skipped too if it had any of them
  - if `manual-approval` specifies a default `approver` `Result`, such as "None", then `slack-msg` would be executed
    ([supporting default `Results` is in progress](https://github.com/tektoncd/community/pull/240))
