
### Configuring the failure timeout

You can use the `Timeout` field in the `Task` spec within the `Pipeline` to set the timeout
of the `TaskRun` that executes that `Task` within the `PipelineRun` that executes your `Pipeline.`
The `Timeout` value is a `duration` conforming to Go's [`ParseDuration`](https://golang.org/pkg/time/#ParseDuration)
format. For example, valid values are `1h30m`, `1h`, `1m`, and `60s`.

**Note:** If you do not specify a `Timeout` value, Tekton instead honors the timeout for the [`PipelineRun`](pipelineruns.md#configuring-a-pipelinerun).

**Note:** If the specified `Task` timeout is greater than the Pipeline timeout as configured in the [`PipelineRun`](pipelineruns.md#configuring-a-failure-timeout), the Pipeline will time-out first causing the `Task` to timeout before its configured timeout.
For example, if the `PipelineRun` sets `timeouts.pipeline = 1h` and the `Pipeline` sets `tasks[0].timeout = 3h`, the task will still timeout after `1h`.
See [`PipelineRun - Configuring a failure timeout`](pipelineruns.md#configuring-a-failure-timeout) for details.

In the example below, the `build-the-image` `Task` is configured to time out after 90 seconds:

```yaml
spec:
  tasks:
    - name: build-the-image
      taskRef:
        name: build-push
      timeout: "0h1m30s"
```

## Using variable substitution

Tekton provides variables to inject values into the contents of certain fields.
The values you can inject come from a range of sources including other fields
in the Pipeline, context-sensitive information that Tekton provides, and runtime
information received from a PipelineRun.

The mechanism of variable substitution is quite simple - string replacement is
performed by the Tekton Controller when a PipelineRun is executed.

See the [complete list of variable substitutions for Pipelines](./variables.md#variables-available-in-a-pipeline)
and the [list of fields that accept substitutions](./variables.md#fields-that-accept-variable-substitutions).

For an end-to-end example, see [using context variables](../examples/v1/pipelineruns/using_context_variables.yaml).

### Using the `retries` and `retry-count` variable substitutions

Tekton supports variable substitution for the [`retries`](#using-the-retries-field)
parameter of `PipelineTask`. Variables like `context.pipelineTask.retries` and
`context.task.retry-count` can be added to the parameters of a `PipelineTask`.
`context.pipelineTask.retries` will be replaced by `retries` of the `PipelineTask`, while
`context.task.retry-count` will be replaced by current retry number of the `PipelineTask`.

```yaml
params:
- name: pipelineTask-retries
  value: "$(context.pipelineTask.retries)"
taskSpec:
  params:
  - name: pipelineTask-retries
  steps:
  - image: ubuntu
    name: print-if-retries-exhausted
    script: |
      if [ "$(context.task.retry-count)" == "$(params.pipelineTask-retries)" ]
      then
        echo "This is the last retry."
      fi
      exit 1
```

**Note:** Every `PipelineTask` can only access its own `retries` and `retry-count`. These
values aren't accessible for other `PipelineTask`s.

## Using `Results`

Tasks can emit [`Results`](tasks.md#emitting-results) when they execute. A Pipeline can use these
`Results` for two different purposes:

1. A Pipeline can pass the `Result` of a `Task` into the `Parameters` or `when` expressions of another.
2. A Pipeline can itself emit `Results` and include data from the `Results` of its Tasks.

> **Note** Tekton does not enforce that results are produced at Task level. If a pipeline attempts to
> consume a result that was declared by a Task, but not produced, it will fail. [TEP-0048](https://github.com/tektoncd/community/blob/main/teps/0048-task-results-without-results.md)
> propopses introducing default values for results to help Pipeline authors manage this case.

### Passing one Task's `Results` into the `Parameters` or `when` expressions of another

Sharing `Results` between `Tasks` in a `Pipeline` happens via
[variable substitution](variables.md#variables-available-in-a-pipeline) - one `Task` emits
a `Result` and another receives it as a `Parameter` with a variable such as
`$(tasks.<task-name>.results.<result-name>)`. Pipeline support two new types of
results and parameters: array `[]string` and object `map[string]string`.
Array result is a beta feature and can be enabled by setting `enable-api-fields` to `alpha` or `beta`.

| Result Type | Parameter Type | Specification                                    | `enable-api-fields` |
|-------------|----------------|--------------------------------------------------|---------------------|
| string      | string         | `$(tasks.<task-name>.results.<result-name>)`     | stable              |
| array       | array          | `$(tasks.<task-name>.results.<result-name>[*])`  | alpha or beta       |
| array       | string         | `$(tasks.<task-name>.results.<result-name>[i])`  | alpha or beta       |
| object      | object         | `$(tasks.<task-name>.results.<result-name>[*])`  | alpha or beta              |
| object      | string         | `$(tasks.<task-name>.results.<result-name>.key)` | alpha or beta              |

**Note:** Whole Array and Object `Results` (using star notation) cannot be referred in `script`.

When one `Task` receives the `Results` of another, there is a dependency created between those
two `Tasks`. In order for the receiving `Task` to get data from another `Task's` `Result`,
the `Task` producing the `Result` must run first. Tekton enforces this `Task` ordering
by ensuring that the `Task` emitting the `Result` executes before any `Task` that uses it.

In the snippet below, a param is provided its value from the `commit` `Result` emitted by the
`checkout-source` `Task`. Tekton will make sure that the `checkout-source` `Task` runs
before this one.

```yaml
params:
  - name: foo
    value: "$(tasks.checkout-source.results.commit)"
  - name: array-params
    value: "$(tasks.checkout-source.results.array-results[*])"
  - name: array-indexing-params
    value: "$(tasks.checkout-source.results.array-results[1])"
  - name: object-params
    value: "$(tasks.checkout-source.results.object-results[*])"
  - name: object-element-params
    value: "$(tasks.checkout-source.results.object-results.objectkey)"
```

**Note:** If `checkout-source` exits successfully without initializing `commit` `Result`,
the receiving `Task` fails and causes the `Pipeline` to fail with `InvalidTaskResultReference`:

```
unable to find result referenced by param 'foo' in 'task';: Could not find result with name 'commit' for task run 'checkout-source'
```

In the snippet below, a `when` expression is provided its value from the `exists` `Result` emitted by the
`check-file` `Task`. Tekton will make sure that the `check-file` `Task` runs before this one.

```yaml
when:
  - input: "$(tasks.check-file.results.exists)"
    operator: in
    values: ["yes"]
```

For an end-to-end example, see [`Task` `Results` in a `PipelineRun`](../examples/v1/pipelineruns/task_results_example.yaml).

Note that `when` expressions are whitespace-sensitive.  In particular, when producing results intended for inputs to `when`
expressions that may include newlines at their close (e.g. `cat`, `jq`), you may wish to truncate them.

```yaml
taskSpec:
  params:
  - name: jsonQuery-check
  steps:
  - image: ubuntu
    name: store-name-in-results
    script: |
      curl -s https://my-json-server.typicode.com/typicode/demo/profile | jq -r .name | tr -d '\n' | tee $(results.name.path)
```

### Emitting `Results` from a `Pipeline`

A `Pipeline` can emit `Results` of its own for a variety of reasons - an external
system may need to read them when the `Pipeline` is complete, they might summarise
the most important `Results` from the `Pipeline's` `Tasks`, or they might simply
be used to expose non-critical messages generated during the execution of the `Pipeline`.

A `Pipeline's` `Results` can be composed of one or many `Task` `Results` emitted during
the course of the `Pipeline's` execution. A `Pipeline` `Result` can refer to its `Tasks'`
`Results` using a variable of the form `$(tasks.<task-name>.results.<result-name>)`.

After a `Pipeline` has executed the `PipelineRun` will be populated with the `Results`
emitted by the `Pipeline`. These will be written to the `PipelineRun's`
`status.pipelineResults` field.

In the example below, the `Pipeline` specifies a `results` entry with the name `sum` that
references the `outputValue` `Result` emitted by the `calculate-sum` `Task`.

```yaml
results:
  - name: sum
    description: the sum of all three operands
    value: $(tasks.calculate-sum.results.outputValue)
```

For an end-to-end example, see [`Results` in a `PipelineRun`](../examples/v1/pipelineruns/pipelinerun-results.yaml).

In the example below, the `Pipeline` collects array and object results from `Tasks`.

```yaml
    results:
      - name: array-results
        type: array
        description: whole array
        value: $(tasks.task1.results.array-results[*])
      - name: array-indexing-results
        type: string
        description: array element
        value: $(tasks.task1.results.array-results[1])
      - name: object-results
        type: object
        description: whole object
        value: $(tasks.task2.results.object-results[*])
      - name: object-element
        type: string
        description: object element
        value: $(tasks.task2.results.object-results.foo)
```

For an end-to-end example see [`Array and Object Results` in a `PipelineRun`](../examples/v1/pipelineruns/pipeline-emitting-results.yaml).

A `Pipeline Result` is not emitted if any of the following are true:
- A `PipelineTask` referenced by the `Pipeline Result` failed. The `PipelineRun` will also
have failed.
- A `PipelineTask` referenced by the `Pipeline Result` was skipped.
- A `PipelineTask` referenced by the `Pipeline Result` didn't emit the referenced `Task Result`. This
should be considered a bug in the `Task` and [may fail a `PipelineTask` in future](https://github.com/tektoncd/pipeline/issues/3497).
- The `Pipeline Result` uses a variable that doesn't point to an actual `PipelineTask`. This will
result in an `InvalidTaskResultReference` validation error during `PipelineRun` execution.
- The `Pipeline Result` uses a variable that doesn't point to an actual result in a `PipelineTask`.
This will cause an `InvalidTaskResultReference` validation error during `PipelineRun` execution.

**Note:** Since a `Pipeline Result` can contain references to multiple `Task Results`, if any of those
`Task Result` references are invalid the entire `Pipeline Result` is not emitted.
**Note:** If a `PipelineTask` referenced by the `Pipeline Result` was skipped, the `Pipeline Result` will not be emitted and the `PipelineRun` will not fail due to a missing result.

## Configuring the `Task` execution order

You can connect `Tasks` in a `Pipeline` so that they execute in a Directed Acyclic Graph (DAG).
Each `Task` in the `Pipeline` becomes a node on the graph that can be connected with an edge
so that one will run before another and the execution of the `Pipeline` progresses to completion
without getting stuck in an infinite loop.

This is done using:
- _resource dependencies_:
  - [`results`](#emitting-results-from-a-pipeline) of one `Task` being passed into `params` or `when` expressions of
    another

- _ordering dependencies_:
  - [`runAfter`](#using-the-runafter-field) clauses on the corresponding `Tasks`

For example, the `Pipeline` defined as follows

```yaml
tasks:
- name: lint-repo
  taskRef:
    name: pylint
- name: test-app
  taskRef:
    name: make-test
- name: build-app
  taskRef:
    name: kaniko-build-app
  runAfter:
    - test-app
- name: build-frontend
  taskRef:
    name: kaniko-build-frontend
  runAfter:
    - test-app
- name: deploy-all
  taskRef:
    name: deploy-kubectl
  runAfter:
    - build-app
    - build-frontend
```

executes according to the following graph:

```none
        |            |
        v            v
     test-app    lint-repo
    /        \
   v          v
build-app  build-frontend
   \          /
    v        v
    deploy-all
```

In particular:

1. The `lint-repo` and `test-app` `Tasks` have no `runAfter` clauses
   and start executing simultaneously.
2. Once `test-app` completes, both `build-app` and `build-frontend` start
   executing simultaneously since they both `runAfter` the `test-app` `Task`.
3. The `deploy-all` `Task` executes once both `build-app` and `build-frontend`
   complete, since it is supposed to `runAfter` them both.
4. The entire `Pipeline` completes execution once both `lint-repo` and `deploy-all`
   complete execution.

## Specifying a display name

The `displayName` field is an optional field that allows you to add a user-facing name of the `Pipeline` that can be used to populate a UI. For example:

```yaml
spec:
  displayName: "Code Scan"
  tasks:
    - name: scan
      taskRef:
        name: sonar-scan
```

## Adding a description

The `description` field is an optional field and can be used to provide description of the `Pipeline`.

## Adding `Finally` to the `Pipeline`

You can specify a list of one or more final tasks under `finally` section. `finally` tasks are guaranteed to be executed
in parallel after all `PipelineTasks` under `tasks` have completed regardless of success or error. `finally` tasks are very
similar to `PipelineTasks` under `tasks` section and follow the same syntax. Each `finally` task must have a
[valid](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names) `name` and a [taskRef or
taskSpec](taskruns.md#specifying-the-target-task). For example:

```yaml
spec:
  tasks:
    - name: tests
      taskRef:
        name: integration-test
  finally:
    - name: cleanup-test
      taskRef:
        name: cleanup
```

### Specifying `displayName` in `finally` tasks

Similar to [specifying `displayName` in `pipelineTasks`](#specifying-displayname-in-pipelinetasks), `finally` tasks also
allows to add a user-facing name of the `finally` task that can be used to populate and distinguish in the dashboard.
For example:

```yaml
spec:
  finally:
    - name: notification
      displayName: "Notify"
      taskRef:
        name: notification
    - name: notification-using-context-variable
      displayName: "Notification from $(context.pipeline.name)"
      taskRef:
        name: notification
```

The `displayName` also allows you to parameterize the human-readable name of your choice based on the
[params](#specifying-parameters), [the task results](#consuming-task-execution-results-in-finally),
and [the context variables](#context-variables).

Fully resolved `displayName` is also available in the status as part of the `pipelineRun.status.childReferences`. The
clients such as the dashboard, CLI, etc. can retrieve the `displayName` from the `childReferences`. The `displayName` mainly
drives a better user experience and at the same time it is not validated for the content or length by the controller.

### Specifying `Workspaces` in `finally` tasks

`finally` tasks can specify [workspaces](workspaces.md) which `PipelineTasks` might have utilized
e.g. a mount point for credentials held in Secrets. To support that requirement, you can specify one or more
`Workspaces` in the `workspaces` field for the `finally` tasks similar to `tasks`.

```yaml
spec:
  workspaces:
    - name: shared-workspace
  tasks:
    - name: clone-app-source
      taskRef:
        name: clone-app-repo-to-workspace
      workspaces:
        - name: shared-workspace
          workspace: shared-workspace
  finally:
    - name: cleanup-workspace
      taskRef:
        name: cleanup-workspace
      workspaces:
        - name: shared-workspace
          workspace: shared-workspace
```

### Specifying `Parameters` in `finally` tasks

Similar to `tasks`, you can specify [`Parameters`](tasks.md#specifying-parameters) in `finally` tasks:

```yaml
spec:
  tasks:
    - name: tests
      taskRef:
        name: integration-test
  finally:
    - name: report-results
      taskRef:
        name: report-results
      params:
        - name: url
          value: "someURL"
```

### Specifying `matrix` in `finally` tasks

> :seedling: **`Matrix` is an [beta](additional-configs.md#beta-features) feature.**
> The `enable-api-fields` feature flag can be set to `"beta"` to specify `Matrix` in a `PipelineTask`.

Similar to `tasks`, you can also provide [`Parameters`](tasks.md#specifying-parameters) through `matrix`
in `finally` tasks:

```yaml
spec:
  tasks:
    - name: tests
      taskRef:
        name: integration-test
  finally:
    - name: report-results
      taskRef:
        name: report-results
      params:
        - name: url
          value: "someURL"
      matrix:
        params:
        - name: slack-channel
          value:
          - "foo"
          - "bar"
        include:
          - name: build-1
            params:
              - name: slack-channel
                value: "foo"
              - name: flags
                value: "-v"
```

For further information, read [`Matrix`](./matrix.md).

### Consuming `Task` execution results in `finally`

`finally` tasks can be configured to consume `Results` of `PipelineTask` from the `tasks` section:

```yaml
spec:
  tasks:
    - name: clone-app-repo
      taskRef:
        name: git-clone
  finally:
    - name: discover-git-commit
      params:
        - name: commit
          value: $(tasks.clone-app-repo.results.commit)
```
**Note:** The scheduling of such `finally` task does not change, it will still be executed in parallel with other
`finally` tasks after all non-`finally` tasks are done.

The controller resolves task results before executing the `finally` task `discover-git-commit`. If the task
`clone-app-repo` failed before initializing `commit` or skipped with [when expression](#guard-task-execution-using-when-expressions)
resulting in uninitialized task result `commit`, the `finally` Task `discover-git-commit` will be included in the list of
`skippedTasks` and continues executing rest of the `finally` tasks. The pipeline exits with `completion` instead of
`success` if a `finally` task is added to the list of `skippedTasks`.

### Consuming `Pipeline` result with `finally`

`finally` tasks can emit `Results` and these results emitted from the `finally` tasks can be configured in the
[Pipeline Results](#emitting-results-from-a-pipeline). References of `Results` from `finally` will follow the same naming conventions as referencing `Results` from `tasks`: ```$(finally.<finally-pipelinetask-name>.result.<result-name>)```.

```yaml
results:
  - name: comment-count-validate
    value: $(finally.check-count.results.comment-count-validate)
finally:
  - name: check-count
    taskRef:
      name: example-task-name
```

In this example, `pipelineResults` in `status` will show the name-value pair for the result `comment-count-validate` which is produced in the `Task` `example-task-name`.


### `PipelineRun` Status with `finally`

With `finally`, `PipelineRun` status is calculated based on `PipelineTasks` under `tasks` section and `finally` tasks.

Without `finally`:

| `PipelineTasks` under `tasks`                                                                           | `PipelineRun` status | Reason      |
|---------------------------------------------------------------------------------------------------------|----------------------|-------------|
| all `PipelineTasks` successful                                                                          | `true`               | `Succeeded` |
| one or more `PipelineTasks` [skipped](#guard-task-execution-using-when-expressions) and rest successful | `true`               | `Completed` |
| single failure of `PipelineTask`                                                                        | `false`              | `failed`    |

With `finally`:

| `PipelineTasks` under `tasks`                                                                          | `finally` tasks                        | `PipelineRun` status | Reason      |
|--------------------------------------------------------------------------------------------------------|----------------------------------------|----------------------|-------------|
| all `PipelineTask` successful                                                                          | all `finally` tasks successful         | `true`               | `Succeeded` |
| all `PipelineTask` successful                                                                          | one or more failure of `finally` tasks | `false`              | `Failed`    |
| one or more `PipelineTask` [skipped](#guard-task-execution-using-when-expressions) and rest successful | all `finally` tasks successful         | `true`               | `Completed` |
| one or more `PipelineTask` [skipped](#guard-task-execution-using-when-expressions) and rest successful | one or more failure of `finally` tasks | `false`              | `Failed`    |
| single failure of `PipelineTask`                                                                       | all `finally` tasks successful         | `false`              | `failed`    |
| single failure of `PipelineTask`                                                                       | one or more failure of `finally` tasks | `false`              | `failed`    |

Overall, `PipelineRun` state transitioning is explained below for respective scenarios:

* All `PipelineTask` and `finally` tasks are successful: `Started` -> `Running` -> `Succeeded`
* At least one `PipelineTask` skipped and rest successful:  `Started` -> `Running` -> `Completed`
* One `PipelineTask` failed / one or more `finally` tasks failed: `Started` -> `Running` -> `Failed`

Please refer to the [table](pipelineruns.md#monitoring-execution-status) under Monitoring Execution Status to learn about
what kind of events are triggered based on the `Pipelinerun` status.


### Using Execution `Status` of `pipelineTask`

A `pipeline` can check the status of a specific `pipelineTask` from the `tasks` section in `finally` through the task
parameters:

```yaml
finally:
  - name: finaltask
    params:
      - name: task1Status
        value: "$(tasks.task1.status)"
    taskSpec:
      params:
        - name: task1Status
      steps:
        - image: ubuntu
          name: print-task-status
          script: |
            if [ $(params.task1Status) == "Failed" ]
            then
              echo "Task1 has failed, continue processing the failure"
            fi
```

This kind of variable can have any one of the values from the following table:

| Status      | Description                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------|
| `Succeeded` | `taskRun` for the `pipelineTask` completed successfully                                          |
| `Failed`    | `taskRun` for the `pipelineTask` completed with a failure or cancelled by the user               |
| `None`      | the `pipelineTask` has been skipped or no execution information available for the `pipelineTask` |

For an end-to-end example, see [`status` in a `PipelineRun`](../examples/v1/pipelineruns/pipelinerun-task-execution-status.yaml).

### Using Aggregate Execution `Status` of All `Tasks`

A `pipeline` can check an aggregate status of all the `tasks` section in `finally` through the task parameters:

```yaml
finally:
  - name: finaltask
    params:
      - name: aggregateTasksStatus
        value: "$(tasks.status)"
    taskSpec:
      params:
        - name: aggregateTasksStatus
      steps:
        - image: ubuntu
          name: check-task-status
          script: |
            if [ $(params.aggregateTasksStatus) == "Failed" ]
            then
              echo "Looks like one or more tasks returned failure, continue processing the failure"
            fi
```

This kind of variable can have any one of the values from the following table:

| Status      | Description                                                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `Succeeded` | all `tasks` have succeeded                                                                                                        |
| `Failed`    | one ore more `tasks` failed                                                                                                       |
| `Completed` | all `tasks` completed successfully including one or more skipped tasks                                                            |
| `None`      | no aggregate execution status available (i.e. none of the above), one or more `tasks` could be pending/running/cancelled/timedout |

For an end-to-end example, see [`$(tasks.status)` usage in a `Pipeline`](../examples/v1/pipelineruns/pipelinerun-task-execution-status.yaml).

### Guard `finally` `Task` execution using `when` expressions

Similar to `Tasks`, `finally` `Tasks` can be guarded using [`when` expressions](#guard-task-execution-using-when-expressions)
that operate on static inputs or variables. Like in `Tasks`, `when` expressions in `finally` `Tasks` can operate on
`Parameters` and `Results`. Unlike in `Tasks`, `when` expressions in `finally` `tasks` can also operate on the [`Execution
Status`](#using-execution-status-of-pipelinetask) of `Tasks`.

#### `when` expressions using `Parameters` in `finally` `Tasks`

`when` expressions in `finally` `Tasks` can utilize `Parameters` as demonstrated using [`golang-build`](https://github.com/tektoncd/catalog/tree/main/task/golang-build/0.1)
and [`send-to-channel-slack`](https://github.com/tektoncd/catalog/tree/main/task/send-to-channel-slack/0.1) Catalog
`Tasks`:

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: pipelinerun-
spec:
  pipelineSpec:
    params:
      - name: enable-notifications
        type: string
        description: a boolean indicating whether the notifications should be sent
    tasks:
      - name: golang-build
        taskRef:
          name: golang-build
      # […]
    finally:
      - name: notify-build-failure # executed only when build task fails and notifications are enabled
        when:
          - input: $(tasks.golang-build.status)
            operator: in
            values: ["Failed"]
          - input: $(params.enable-notifications)
            operator: in
            values: ["true"]
        taskRef:
          name: send-to-slack-channel
      # […]
  params:
    - name: enable-notifications
      value: true
```

#### `when` expressions using `Results` in `finally` 'Tasks`

`when` expressions in `finally` `tasks` can utilize `Results`, as demonstrated using [`git-clone`](https://github.com/tektoncd/catalog/tree/main/task/git-clone/0.2)
and [`github-add-comment`](https://github.com/tektoncd/catalog/tree/main/task/github-add-comment/0.2) Catalog `Tasks`:

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: pipelinerun-
spec:
  pipelineSpec:
    tasks:
      - name: git-clone
        taskRef:
          name: git-clone
      - name: go-build
      # […]
    finally:
      - name: notify-commit-sha # executed only when commit sha is not the expected sha
        when:
          - input: $(tasks.git-clone.results.commit)
            operator: notin
            values: [$(params.expected-sha)]
        taskRef:
          name: github-add-comment
      # […]
  params:
    - name: expected-sha
      value: 54dd3984affab47f3018852e61a1a6f9946ecfa
```

If the `when` expressions in a `finally` `task` use `Results` from a skipped or failed non-finally `Tasks`, then the
`finally` `task` would also be skipped and be included in the list of `Skipped Tasks` in the `Status`, [similarly to when using
`Results` in other parts of the `finally` `task`](#consuming-task-execution-results-in-finally).

#### `when` expressions using `Execution Status` of `PipelineTask` in `finally` `tasks`

`when` expressions in `finally` `tasks` can utilize [`Execution Status` of `PipelineTasks`](#using-execution-status-of-pipelinetask),
as demonstrated using [`golang-build`](https://github.com/tektoncd/catalog/tree/main/task/golang-build/0.1) and
[`send-to-channel-slack`](https://github.com/tektoncd/catalog/tree/main/task/send-to-channel-slack/0.1) Catalog `Tasks`:

```yaml
apiVersion: tekton.dev/v1 # or tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: pipelinerun-
spec:
  pipelineSpec:
    tasks:
      - name: golang-build
        taskRef:
          name: golang-build
      # […]
    finally:
      - name: notify-build-failure # executed only when build task fails
        when:
          - input: $(tasks.golang-build.status)
            operator: in
            values: ["Failed"]
        taskRef:
          name: send-to-slack-channel
      # […]
```

For an end-to-end example, see [PipelineRun with `when` expressions](../examples/v1/pipelineruns/pipelinerun-with-when-expressions.yaml).

#### `when` expressions using `Aggregate Execution Status` of `Tasks` in `finally` `tasks`

`when` expressions in `finally` `tasks` can utilize
[`Aggregate Execution Status` of `Tasks`](#using-aggregate-execution-status-of-all-tasks) as demonstrated:

```yaml
finally:
  - name: notify-any-failure # executed only when one or more tasks fail
    when:
      - input: $(tasks.status)
        operator: in
        values: ["Failed"]
    taskRef:
      name: notify-failure
```

For an end-to-end example, see [PipelineRun with `when` expressions](../examples/v1/pipelineruns/pipelinerun-with-when-expressions.yaml).

### Known Limitations

#### Cannot configure the `finally` task execution order

It's not possible to configure or modify the execution order of the `finally` tasks. Unlike `Tasks` in a `Pipeline`,
all `finally` tasks run simultaneously and start executing once all `PipelineTasks` under `tasks` have settled which means
no `runAfter` can be specified in `finally` tasks.

## Using Custom Tasks

Custom Tasks have been promoted from `v1alpha1` to `v1beta1`. Starting from `v0.43.0` to `v0.46.0`, Pipeline Controller is able to create either `v1alpha1` or `v1beta1` Custom Task gated by a feature flag `custom-task-version`, defaulting to `v1beta1`. You can set `custom-task-version` to `v1alpha1` or `v1beta1` to control which version to create.

Starting from `v0.47.0`, feature flag `custom-task-version` is removed and only `v1beta1` Custom Task will be supported. See the [migration doc](migrating-v1alpha1.Run-to-v1beta1.CustomRun.md) for details.

[Custom Tasks](https://github.com/tektoncd/community/blob/main/teps/0002-custom-tasks.md)
can implement behavior that doesn't correspond directly to running a workload in a `Pod` on the cluster.
For example, a custom task might execute some operation outside of the cluster and wait for its execution to complete.

A `PipelineRun` starts a custom task by creating a [`CustomRun`](https://github.com/tektoncd/pipeline/blob/main/docs/customruns.md) instead of a `TaskRun`.
In order for a custom task to execute, there must be a custom task controller running on the cluster
that is responsible for watching and updating `CustomRun`s which reference their type.

### Specifying the target Custom Task

To specify the custom task type you want to execute, the `taskRef` field
must include the custom task's `apiVersion` and `kind` as shown below.
Using `apiVersion` will always create a `CustomRun`. If `apiVersion` is set, `kind` is required as well.

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
```

This creates a `Run/CustomRun` of a custom task of type `Example` in the `example.dev` API group with the version `v1alpha1`.

Validation error will be returned if `apiVersion` or `kind` is missing.

You can also specify the `name` of a custom task resource object previously defined in the cluster.

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
```

If the `taskRef` specifies a name, the custom task controller should look up the
`Example` resource with that name and use that object to configure the execution.

If the `taskRef` does not specify a name, the custom task controller might support
some default behavior for executing unnamed tasks.

### Specifying a Custom Task Spec in-line (or embedded)

**For `v1alpha1.Run`**
```yaml
spec:
  tasks:
    - name: run-custom-task
      taskSpec:
        apiVersion: example.dev/v1alpha1
        kind: Example
        spec:
          field1: value1
          field2: value2
```

**For `v1beta1.CustomRun`**
```yaml
spec:
  tasks:
    - name: run-custom-task
      taskSpec:
        apiVersion: example.dev/v1alpha1
        kind: Example
        customSpec:
          field1: value1
          field2: value2
```

If the custom task controller supports the in-line or embedded task spec, this will create a `Run/CustomRun` of a custom task of
type `Example` in the `example.dev` API group with the version `v1alpha1`.

If the `taskSpec` is not supported, the custom task controller should produce proper validation errors.

Please take a look at the
developer guide for custom controllers supporting `taskSpec`:
- [guidance for `Run`](runs.md#developer-guide-for-custom-controllers-supporting-spec)
- [guidance for `CustomRun`](customruns.md#developer-guide-for-custom-controllers-supporting-customspec)

`taskSpec` support for `pipelineRun` was designed and discussed in
[TEP-0061](https://github.com/tektoncd/community/blob/main/teps/0061-allow-custom-task-to-be-embedded-in-pipeline.md)

### Specifying parameters

If a custom task supports [`parameters`](tasks.md#specifying-parameters), you can use the
`params` field to specify their values:

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
      params:
        - name: foo
          value: bah
```

## Context Variables

The `Parameters` in the `Params` field will accept
[context variables](variables.md) that will be substituted, including:

* `PipelineRun` name, namespace and uid
* `Pipeline` name
* `PipelineTask` retries

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
      params:
        - name: foo
          value: $(context.pipeline.name)
```

### Specifying matrix

> :seedling: **`Matrix` is an [alpha](additional-configs.md#alpha-features) feature.**
> The `enable-api-fields` feature flag must be set to `"alpha"` to specify `Matrix` in a `PipelineTask`.

If a custom task supports [`parameters`](tasks.md#specifying-parameters), you can use the
`matrix` field to specify their values, if you want to fan:

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
      params:
        - name: foo
          value: bah
      matrix:
        params:
        - name: bar
          value:
            - qux
            - thud
        include:
          - name: build-1
            params:
            - name: common-package
              value: path-to-common-pkg
```

For further information, read [`Matrix`](./matrix.md).

### Specifying workspaces

If the custom task supports it, you can provide [`Workspaces`](workspaces.md#using-workspaces-in-tasks) to share data with the custom task.

```yaml
spec:
  tasks:
    - name: run-custom-task
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
      workspaces:
        - name: my-workspace
```

Consult the documentation of the custom task that you are using to determine whether it supports workspaces and how to name them.

### Using `Results`

If the custom task produces results, you can reference them in a Pipeline using the normal syntax,
`$(tasks.<task-name>.results.<result-name>)`.

### Specifying `Timeout`

#### `v1alpha1.Run`
If the custom task supports it as [we recommended](runs.md#developer-guide-for-custom-controllers-supporting-timeout), you can provide `timeout` to specify the maximum running time of a `CustomRun` (including all retry attempts or other operations).

#### `v1beta1.CustomRun`
If the custom task supports it as [we recommended](customruns.md#developer-guide-for-custom-controllers-supporting-timeout), you can provide `timeout` to specify the maximum running time of one `CustomRun` execution.

```yaml
spec:
  tasks:
    - name: run-custom-task
      timeout: 2s
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
```

Consult the documentation of the custom task that you are using to determine whether it supports `Timeout`.

### Specifying `Retries`
If the custom task supports it, you can provide `retries` to specify how many times you want to retry the custom task.

```yaml
spec:
  tasks:
    - name: run-custom-task
      retries: 2
      taskRef:
        apiVersion: example.dev/v1alpha1
        kind: Example
        name: myexample
```

Consult the documentation of the custom task that you are using to determine whether it supports `Retries`.

### Known Custom Tasks

We try to list as many known Custom Tasks as possible here so that users can easily find what they want. Please feel free to share the Custom Task you implemented in this table.

#### v1beta1.CustomRun

| Custom Task                      | Description                                                                                                                      |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| [Wait Task Beta][wait-task-beta] | Waits a given amount of time before succeeding, specified by an input parameter named duration. Support `timeout` and `retries`. |
| [Approvals][approvals-beta]| Pauses the execution of `PipelineRuns` and waits for manual approvals. Version 0.6.0 and up. |

#### v1alpha1.Run

| Custom Task                                      | Description                                                                                                |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [Pipeline Loops][pipeline-loops]                 | Runs a `Pipeline` in a loop with varying `Parameter` values.                                               |
| [Common Expression Language][cel]                | Provides Common Expression Language support in Tekton Pipelines.                                           |
| [Wait][wait]                                     | Waits a given amount of time, specified by a `Parameter` named "duration", before succeeding.              |
| [Approvals][approvals-alpha]                     | Pauses the execution of `PipelineRuns` and waits for manual approvals. Version up to (and including) 0.5.0 |
| [Pipelines in Pipelines][pipelines-in-pipelines] | Defines and executes a `Pipeline` in a `Pipeline`.                                                         |
| [Task Group][task-group]                         | Groups `Tasks` together as a `Task`.                                                                       |
| [Pipeline in a Pod][pipeline-in-pod]             | Runs `Pipeline` in a `Pod`.                                                                                |

[pipeline-loops]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/pipeline-loops
[task-loops]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/task-loops
[cel]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/cel
[wait]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/wait-task
[approvals-alpha]: https://github.com/automatiko-io/automatiko-approval-task/tree/v0.5.0
[approvals-beta]: https://github.com/automatiko-io/automatiko-approval-task/tree/v0.6.1
[task-group]: https://github.com/openshift-pipelines/tekton-task-group/tree/39823f26be8f59504f242a45b9f2e791d4b36e1c
[pipelines-in-pipelines]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/pipelines-in-pipelines
[pipeline-in-pod]: https://github.com/tektoncd/experimental/tree/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/pipeline-in-pod
[wait-task-beta]: https://github.com/tektoncd/pipeline/tree/a127323da31bcb933a04a6a1b5dbb6e0411e3dc1/test/custom-task-ctrls/wait-task-beta

## Code examples

For a better understanding of `Pipelines`, study [our code examples](https://github.com/tektoncd/pipeline/tree/main/examples).

---

Except as otherwise noted, the content of this page is licensed under the
[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/),
and code samples are licensed under the
[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
