Feature: testing the function get_roots
	Scenario: get roots of biquadratic equation for coef. [1, -10, 9]
		Given I put coefficients [-4, 16, 0] into the function
		Then I get roots [3.0, -3.0, 1.0, -1.0]

	Scenario: get roots of biquadratic equation for coef. [1, 1, -2]
		Given I put coefficsients [1, 1, -2] into the function
		Then I get roots [1.0, -1.0]

    Scenario: get roots of biquadratic equation for coef. [1, 1, 1]
		Given I put coefficients [1, 1, 1] into the function
		Then I get roots []