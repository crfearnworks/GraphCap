# Test Overview

Tests are split into three main categories:

- `unit` tests: these are tests that test individual components or functions in isolation.
- `integration` tests: these are tests that test the interaction between components or services.
- `e2e` tests: these are tests that test the entire application, including the user interface, backend, and external systems.

Unit tests should be able to run in any environment. To install test dependencies, run `uv pip install -e ./server[dev]`

Integration tests need providers to be set up. Copy the `provider.example.config.toml` file to `provider.test.config.toml` into this directory and configure to include the providers you want to test.

To run tests, cd into the `server` directory and run :

Unit test watch : `uv run ptw . -c pytest.ini -v -m "not integration"`
Unit test : `uv run pytest -v -c pytest.ini -m "not integration"`
Integration test : `uv run pytest -v -c pytest.ini`


## Test Policy 

### Conventions
- Tests should include a `GIVEN`, `WHEN`, `THEN` structure focusing on the behavior of the code under tested.

### Unit Tests
**Purpose:** To test the smallest units of code, typically functions or methods, in isolation.

**When to Use:**
- For complex algorithms, data transformations, or business logic
- For utility functions or components that are reused throughout the application
- When there's a clear "black box" input/output relationship
- To drive development, especially when dealing with complex logic and a need for immediate feedback
- When manually testing is too time consuming and frustrating
- For any code that will cause a lot of manual testing to be repeated

**Characteristics:** Fast to run, focused, and easy to maintain.

**Avoid:**
- Over-mocking dependencies, especially databases or external APIs. Focus on testing real code, the code that runs in production. If you are reaching for a mock, step back and determine if this should be an integration test instead.
- Creating tests that are too tightly coupled to implementation details, or that will break with each refactoring. Test the functionality, not the implementation.

### Integration Tests
**Purpose:** To test interactions between different components or modules within the application.

**When to Use:**
- To verify that different services or components interact with each other correctly
- To test interactions with real databases or external APIs
- To test data flow through the application
- When unit testing is insufficient to verify the correctness of a more complex interaction

**Characteristics:** Slower than unit tests but verify higher-level interactions.

**Avoid:**
- Overly broad integration tests that try to test too much functionality at once
- Duplicating logic that is already tested with unit tests

### End-to-End (E2E) Tests
**Purpose:** To test the entire application, including the user interface, backend, and external systems.

**When to Use:**
- To verify the most critical user journeys
- To ensure that changes to the different parts of the system haven't broken the whole application
- To catch issues that may not be apparent in unit or integration tests

**Characteristics:** Slowest to run and can be complex to maintain but are very valuable.

**Avoid:**
- Too many end-to-end tests, because they can slow down the development process and make it difficult to pinpoint issues
- End-to-end tests that duplicate integration or unit test coverage