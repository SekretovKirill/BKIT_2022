Feature: Test Biquadratic equation Functionality

Scenario:Biquadratic equation solver tester
    Given Biquadratic equation solver is running
    When a, b, c are "1", "-7", and "4"
    Then Result is "-2.524, 2.524, -0.792, 0.792"

Scenario: Biquadratic equation solver tester
    Given Biquadratic equation solver is running
    When a, b, c are "1", "-4", and "4"
    Then Result is "-1.414, 1.414"

Scenario: Biquadratic equation solver tester
    Given Biquadratic equation solver is running
    When a, b, c are "1", "0", and "-16"
    Then Result is "-2.0, 2.0"