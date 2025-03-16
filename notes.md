# Types of Chains

## Simple Chain
A simple chain consists of a single step or task.

**Diagram:**
```mermaid
graph TD;
    A[Task 1];
```

**Use Cases:**
- Single-step data processing.
- Simple data retrieval tasks.

## Sequential Chain
A sequential chain consists of multiple steps executed one after another.

**Diagram:**
```mermaid
graph TD;
    A[Task 1] --> B[Task 2] --> C[Task 3];
```

**Use Cases:**
- Data processing pipelines.
- Multi-step data transformation.

## Parallel Chain
A parallel chain consists of multiple steps executed simultaneously.

**Diagram:**
```mermaid
graph TD;
    A[Task 1] --> B[Task 2];
    A --> C[Task 3];
```

**Use Cases:**
- Concurrent data processing.
- Parallel data analysis.

## Conditional Chain
A conditional chain consists of steps executed based on certain conditions.

**Diagram:**
```mermaid
graph TD;
    A[Task 1] --> B{Condition?};
    B -->|Yes| C[Task 2];
    B -->|No| D[Task 3];
```

**Use Cases:**
- Decision-based data processing.
- Conditional data workflows.

