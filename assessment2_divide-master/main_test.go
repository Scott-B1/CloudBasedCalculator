package divide_main

import (
  "testing"
)

func DivideTest(t *testing.T) {
	answer := divided(4,2)
	if answer != 2 {
		t.Errorf("Dividing is incorrect, Received: %d, Expected: %d", answer, 2)
	}
}

func DivideTestNegative(t *testing.T) {
	answer := divided(8,-2)
	if answer != -4 {
		t.Errorf("Dividing is incorrect, Received: %d, Expected: %d", answer, -4)
	}
}
