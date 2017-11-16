# how to run this example?

```
radish -b calculator/radish/ calculator/features/SumNumbers.feature
```

the expected result:

```
❯❯❯ radish -b calculator/radish/ calculator/features/SumNumbers.feature
Feature: The calculator should be able to sum numbers  # calculator/features/SumNumbers.feature
    In order to make sure the calculator

    sums numbers correctly I have the following
    test scenarios:

    Scenario: Test my calculator
        Given I have the numbers 5.0 and 6.0
        When I sum them
        Then I expect the result to be 11

1 features (1 passed)
1 scenarios (1 passed)
3 steps (3 passed)
Run 1510846125 finished within a moment
```
